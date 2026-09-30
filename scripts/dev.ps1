[CmdletBinding()]
param(
    [string]$TemplateRepoUrl = "https://github.com/dynamsoft-docs/Docs-Template-Repo.git",
    [string]$TemplateBranch = "preview",
    [int]$Port = 5555,
    [string]$BindHost = "localhost",
    [switch]$NoTemplateUpdate,
    [switch]$NoServe
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-Step {
    param([string]$Message)
    Write-Host "==> $Message"
}

function Ensure-Command {
    param([string]$Name)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command '$Name' was not found in PATH."
    }
}

function Invoke-Native {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath,
        [string[]]$Arguments = @()
    )

    & $FilePath @Arguments
    $code = $LASTEXITCODE
    if ($code -ne 0) {
        $argText = ($Arguments -join " ")
        throw "Command failed with exit code ${code}: $FilePath $argText"
    }
}

function Invoke-Robocopy {
    param(
        [string]$Source,
        [string]$Destination,
        [string[]]$ExtraArgs
    )

    $baseArgs = @(
        $Source,
        $Destination,
        "/R:2",
        "/W:2",
        "/NFL",
        "/NDL",
        "/NJH",
        "/NJS",
        "/NP"
    )
    $allArgs = $baseArgs + $ExtraArgs
    & robocopy @allArgs | Out-Null
    $code = $LASTEXITCODE
    if ($code -ge 8) {
        throw "robocopy failed with exit code $code. Source: $Source Destination: $Destination"
    }
}

Ensure-Command "git"
Ensure-Command "robocopy"
Ensure-Command "bundle"

$repoRoot = Split-Path -Parent $PSScriptRoot
$devRoot = Join-Path $repoRoot ".dev"
$templateRoot = Join-Path $devRoot "Docs-Template-Repo"
$docHome = Join-Path $devRoot "DocHome"
$bundlePath = Join-Path $devRoot "vendor\bundle"
$bundleConfig = Join-Path $devRoot ".bundle"
$bundleUserHome = Join-Path $devRoot ".bundle-user"
$jekyllCache = Join-Path $devRoot ".jekyll-cache"
$siteDir = Join-Path $devRoot "_site"

Write-Step "Preparing local workspace in $devRoot"
New-Item -ItemType Directory -Force -Path $devRoot | Out-Null

if (-not (Test-Path $templateRoot)) {
    Write-Step "Cloning template repo ($TemplateBranch)"
    Invoke-Native -FilePath "git" -Arguments @("clone", "--depth", "1", "--branch", $TemplateBranch, $TemplateRepoUrl, $templateRoot)
} elseif (-not $NoTemplateUpdate) {
    Write-Step "Syncing template repo ($TemplateBranch)"
    Invoke-Native -FilePath "git" -Arguments @("-C", $templateRoot, "fetch", "origin", $TemplateBranch, "--depth", "1")
    Invoke-Native -FilePath "git" -Arguments @("-C", $templateRoot, "reset", "--hard")
    Invoke-Native -FilePath "git" -Arguments @("-C", $templateRoot, "clean", "-fd")
    Invoke-Native -FilePath "git" -Arguments @("-C", $templateRoot, "checkout", "-B", $TemplateBranch, "origin/$TemplateBranch")
} else {
    Write-Step "Skipping template update"
}

Write-Step "Rebuilding merged site workspace"
New-Item -ItemType Directory -Force -Path $docHome | Out-Null
Invoke-Robocopy -Source $repoRoot -Destination $docHome -ExtraArgs @(
    "/MIR",
    "/XD", ".git", ".dev", ".vs", "node_modules", "_site", ".bundle", ".jekyll-cache", ".sass-cache", "vendor"
)
Invoke-Robocopy -Source $templateRoot -Destination $docHome -ExtraArgs @(
    "/E",
    "/XD", ".git", ".github", "_site", "node_modules"
)

Write-Step "Applying local assetsPath replacements"
$search = "assetsPath = '/webres/wwwroot'"
$replace = "assetsPath = 'https://www.dynamsoft.com/webres/wwwroot'"
foreach ($dirName in @("_includes", "_layouts")) {
    $dirPath = Join-Path $docHome $dirName
    if (-not (Test-Path $dirPath)) {
        continue
    }

    Get-ChildItem -Path $dirPath -Recurse -File | ForEach-Object {
        $path = $_.FullName
        try {
            $content = [System.IO.File]::ReadAllText($path)
        } catch {
            return
        }
        if ($content.Contains($search)) {
            $updated = $content.Replace($search, $replace)
            [System.IO.File]::WriteAllText($path, $updated)
        }
    }
}

Write-Step "Configuring Bundler and Jekyll local paths"
$env:BUNDLE_PATH = $bundlePath
$env:BUNDLE_APP_CONFIG = $bundleConfig
$env:BUNDLE_USER_HOME = $bundleUserHome
$env:BUNDLE_USER_CACHE = Join-Path $bundleUserHome "cache"
$env:JEKYLL_CACHE_DIR = $jekyllCache
$env:JEKYLL_ENV = "development"
New-Item -ItemType Directory -Force -Path $bundlePath, $bundleConfig, $bundleUserHome, $jekyllCache, $siteDir | Out-Null

Push-Location $docHome
try {
    Write-Step "Installing Ruby dependencies"
    Invoke-Native -FilePath "bundle" -Arguments @("install")

    if ($NoServe) {
        Write-Step "Build workspace prepared. Start server with:"
        Write-Host "bundle exec jekyll serve -P $Port --trace --host=$BindHost --livereload --destination `"$siteDir`""
    } else {
        Write-Step "Starting Jekyll server on port $Port"
        Invoke-Native -FilePath "bundle" -Arguments @("exec", "jekyll", "serve", "-P", "$Port", "--trace", "--host=$BindHost", "--livereload", "--destination", "$siteDir")
    }
} finally {
    Pop-Location
}
