#!/usr/bin/env bash

set -euo pipefail

template_repo_url="https://github.com/dynamsoft-docs/Docs-Template-Repo.git"
template_branch="preview"
port="5555"
bind_host="localhost"
no_template_update="false"
no_serve="false"

write_step() {
  echo "==> $1"
}

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Required command '$1' was not found in PATH." >&2
    exit 1
  fi
}

show_help() {
  cat <<'EOF'
Usage: ./scripts/dev.sh [options]

Options:
  --template-repo-url URL   Template repository URL
  --template-branch NAME    Template branch (default: preview)
  --port N                  Jekyll port (default: 5555)
  --bind-host HOST          Jekyll bind host (default: localhost)
  --no-template-update      Skip template fetch/pull
  --no-serve                Prepare workspace only (do not start Jekyll)
  -h, --help                Show this help message
EOF
}

require_option_value() {
  if [[ $# -lt 2 || -z "${2:-}" || "${2:-}" == --* ]]; then
    echo "Missing value for option: $1" >&2
    show_help
    exit 1
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --template-repo-url)
      require_option_value "$@"
      template_repo_url="$2"
      shift 2
      ;;
    --template-branch)
      require_option_value "$@"
      template_branch="$2"
      shift 2
      ;;
    --port)
      require_option_value "$@"
      port="$2"
      shift 2
      ;;
    --bind-host)
      require_option_value "$@"
      bind_host="$2"
      shift 2
      ;;
    --no-template-update)
      no_template_update="true"
      shift
      ;;
    --no-serve)
      no_serve="true"
      shift
      ;;
    -h|--help)
      show_help
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      show_help
      exit 1
      ;;
  esac
done

require_cmd git
require_cmd rsync
require_cmd bundle
require_cmd find
require_cmd sed

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "$script_dir/.." && pwd)"
dev_root="$repo_root/.dev"
template_root="$dev_root/Docs-Template-Repo"
doc_home="$dev_root/DocHome"
bundle_path="$dev_root/vendor/bundle"
bundle_config="$dev_root/.bundle"
bundle_user_home="$dev_root/.bundle-user"
jekyll_cache="$dev_root/.jekyll-cache"
site_dir="$dev_root/_site"

write_step "Preparing local workspace in $dev_root"
mkdir -p "$dev_root"

if [[ ! -d "$template_root/.git" ]]; then
  write_step "Cloning template repo ($template_branch)"
  git clone --depth 1 --branch "$template_branch" "$template_repo_url" "$template_root"
elif [[ "$no_template_update" != "true" ]]; then
  write_step "Syncing template repo ($template_branch)"
  git -C "$template_root" fetch origin "$template_branch" --depth 1
  git -C "$template_root" reset --hard
  git -C "$template_root" clean -fd
  git -C "$template_root" checkout -B "$template_branch" "origin/$template_branch"
else
  write_step "Skipping template update"
fi

write_step "Rebuilding merged site workspace"
rm -rf "$doc_home"
mkdir -p "$doc_home"
rsync -a --delete \
  --exclude '.git' \
  --exclude '.dev' \
  --exclude '.vs' \
  --exclude 'node_modules' \
  --exclude '_site' \
  --exclude '.bundle' \
  --exclude '.jekyll-cache' \
  --exclude '.sass-cache' \
  --exclude 'vendor' \
  "$repo_root"/ "$doc_home"/
rsync -a \
  --exclude '.git' \
  --exclude '.github' \
  --exclude '_site' \
  --exclude 'node_modules' \
  "$template_root"/ "$doc_home"/

write_step "Applying local assetsPath replacements"
search="assetsPath = '/webres/wwwroot'"
replace="assetsPath = 'https://www.dynamsoft.com/webres/wwwroot'"
for dir_name in "_includes" "_layouts"; do
  dir_path="$doc_home/$dir_name"
  if [[ ! -d "$dir_path" ]]; then
    continue
  fi

  while IFS= read -r -d '' file_path; do
    sed -i "s|$search|$replace|g" "$file_path"
  done < <(find "$dir_path" -type f -print0)
done

write_step "Configuring Bundler and Jekyll local paths"
export BUNDLE_PATH="$bundle_path"
export BUNDLE_APP_CONFIG="$bundle_config"
export BUNDLE_USER_HOME="$bundle_user_home"
export BUNDLE_USER_CACHE="$bundle_user_home/cache"
export JEKYLL_CACHE_DIR="$jekyll_cache"
export JEKYLL_ENV="development"
mkdir -p "$bundle_path" "$bundle_config" "$bundle_user_home" "$jekyll_cache" "$site_dir"

pushd "$doc_home" >/dev/null
write_step "Installing Ruby dependencies"
bundle install

if [[ "$no_serve" == "true" ]]; then
  write_step "Build workspace prepared. Start server with:"
  echo "bundle exec jekyll serve -P $port --trace --host=$bind_host --livereload --destination \"$site_dir\""
else
  write_step "Starting Jekyll server on port $port"
  bundle exec jekyll serve -P "$port" --trace --host="$bind_host" --livereload --destination "$site_dir"
fi
popd >/dev/null
