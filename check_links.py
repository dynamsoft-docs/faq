import os
import re
import urllib.request
import urllib.error
import ssl
import concurrent.futures

# Configuration
ROOT_DIR = os.getcwd()
MAX_THREADS = 20
SOFT_404_KEYWORDS = [
    'id="pageNotFound"',
    "Oops! That page can't be found.",
    "alt=\"Page Not Found\"",
    "illus-404.png",
]


# Context for https requests
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE 

def find_md_files(root_dir):
    md_files = []
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs: dirs.remove('.git')
        if '_site' in dirs: dirs.remove('_site')
        if '.dev' in dirs: dirs.remove('.dev')
        
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

DS_SOFT_404_MARKERS = [
    'id="pagenotfound"',                 # DOM id（你 lower() 了，所以用小写）
    'illus-404.png',                     # 404 图片
    "oops! that page can't be found.",   # 404 H1 文案
    'alt="page not found"',              # 图片 alt
]

def is_soft_404(content_lower: str) -> str | None:
    # 返回命中的 marker，便于 debug
    for m in DS_SOFT_404_MARKERS:
        if m in content_lower:
            return m
    return None

def check_url(url):
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        )
        with urllib.request.urlopen(req, timeout=15, context=ctx) as response:
            code = response.getcode()

            # 3xx 也算 OK（已允许重定向则一般拿到最终 200，这里保留逻辑）
            if 200 <= code < 400:
                try:
                    # 建议读多一点，Dynamsoft 的 pageNotFound 区块可能不在前 15KB
                    content = response.read(50000).decode('utf-8', errors='ignore').lower()

                    # ✅ 先做“强特征” soft-404 判断（更准）
                    hit = is_soft_404(content)
                    if hit:
                        return False, code, f"Soft 404 (marker: {hit})"

                    # ✅ 再做你原来的 title/h1 关键词检测（兜底）
                    if "<title>" in content:
                        title_part = content.split("<title>", 1)[1].split("</title>", 1)[0]
                        for keyword in SOFT_404_KEYWORDS:
                            if keyword in title_part:
                                return False, code, f"Soft 404 (Title: '{keyword}')"

                    # h1 可能有属性，例如 <h1 class="...">，所以用更宽松的方式找
                    if "<h1" in content and "</h1>" in content:
                        h1_block = content.split("<h1", 1)[1].split("</h1>", 1)[0]
                        for keyword in SOFT_404_KEYWORDS:
                            if keyword in h1_block:
                                return False, code, f"Soft 404 (H1: '{keyword}')"

                except Exception:
                    pass

                return True, code, "OK"
            else:
                return False, code, f"Status {code}"

    except urllib.error.HTTPError as e:
        return False, e.code, f"HTTP Error {e.code}"
    except urllib.error.URLError as e:
        return False, 0, f"URL Error: {e.reason}"
    except Exception as e:
        return False, 0, f"Error: {str(e)}"

def scan_file_for_https_links(file_path):
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        md_links = re.findall(r'\[.*?\]\((https://.*?)\)', content)
        html_srcs = re.findall(r'src=["\'](https://.*?)["\']', content)
        
        for link in md_links + html_srcs:
            clean_link = link.split()[0].strip('()')
            links.append(clean_link)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return links

def main():
    print(f"Scanning for HTTPS links in: {ROOT_DIR}")
    files = find_md_files(ROOT_DIR)
    
    file_links_map = {} 
    all_urls = set()
    
    for file_path in files:
        links = scan_file_for_https_links(file_path)
        if links:
            file_links_map[file_path] = links
            all_urls.update(links)
    
    print(f"Found {len(all_urls)} unique HTTPS links to check.")
    print(f"Checking links (Concurrent Status + Soft 404 Check) ...")
    
    url_status = {} 
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in all_urls}
        completed = 0
        total = len(all_urls)
        
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                url_status[url] = result
            except Exception as e:
                url_status[url] = (False, 0, str(e))
            
            completed += 1
            if completed % 10 == 0 or completed == total:
                print(f"Progress: {completed}/{total}", end='\r')
                
    print(f"\nProgress: {total}/{total}")
    print("\n--- Broken or Soft 404 Links Report ---\n")
    
    broken_count = 0
    files_with_issues = 0
    
    for file_path, links in file_links_map.items():
        issues_in_file = []
        for link in links:
            if link in url_status:
                is_valid, code, msg = url_status[link]
                if not is_valid:
                    issues_in_file.append((link, code, msg))
        
        if issues_in_file:
            files_with_issues += 1
            rel_path = os.path.relpath(file_path, ROOT_DIR)
            print(f"📄 {rel_path}")
            for link, code, msg in issues_in_file:
                print(f"  ❌ [{code}] {link} -> {msg}")
                broken_count += 1
            print("")

    if broken_count == 0:
        print("✅ No broken links found!")
    else:
        print(f"❌ Found {broken_count} issues in {files_with_issues} files.")

if __name__ == "__main__":
    main()
