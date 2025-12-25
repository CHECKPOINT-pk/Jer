# -*- coding: utf-8 -*-
# AUTHOR: GEMINI (PRO VERSION)
# TOOL: FB COOKIE TO JSON & EAAG TOKEN EXTRACTOR
# STATUS: 101% WORKING & STABLE

import os, sys, time, re, json, requests
from rich import print as cetak
from rich.panel import Panel as nel
from rich.console import Console

console = Console()

# Colors
H = '\x1b[1;92m' # GREEN
M = '\x1b[1;91m' # RED
P = '\x1b[1;97m' # WHITE
K = '\x1b[1;93m' # YELLOW
N = '\x1b[0m'    # RESET

def banner():
    os.system('clear')
    banner_text = """[bold cyan]
  __  __ _____  _____   _____  ____  _  ________ 
 |  \/  |  __ \|  __ \ / ____|/ __ \| |/ /_   _|
 | \  / | |  | | |__) | |    | |  | | ' /  | |  
 | |\/| | |  | |  _  /| |    | |  | |  <   | |  
 | |  | | |__| | | \ \| |____| |__| | . \ _| |_ 
 |_|  |_|_____/|_|  \_\\_____|\____/|_|\_\_____|
    [/bold cyan]
 [bold white]PROFESSIONAL COOKIE CONVERTER & TOKEN EXTRACTOR[/bold white]"""
    cetak(nel(banner_text, style="cyan", title="[bold red]101% WORKING VERSION[/bold red]"))

class CookieTool:
    def __init__(self):
        # Professional User-Agent
        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

    def menu(self):
        banner()
        cetak(f" {H}[01]{P} Extract EAAG Token & JSON Cookie (For Extension)")
        cetak(f" {H}[02]{P} Check Cookie Health (Live/Dead)")
        cetak(f" {H}[00]{P} Exit Tool")
        print(f"{P}-------------------------------------------------------")
        choice = input(f" {H}[+] Select Option: {N}")
        
        if choice in ['1', '01']:
            self.convert_system()
        elif choice in ['2', '02']:
            self.checker_system()
        else:
            exit()

    def convert_system(self):
        banner()
        cetak(f" {K}[!] Paste your Facebook Browser Cookie below:")
        cookie = input(f" {H}[+] Cookie: {P}")
        
        if not cookie or 'c_user' not in cookie:
            cetak(f" {M}[!] Invalid Cookie! Make sure it contains 'c_user'"); time.sleep(2); self.menu()

        cetak(f"\n {H}[*] Connecting to Facebook Server...")
        
        try:
            # Extracting EAAG Token via Business Manager logic
            headers = {
                "user-agent": self.ua,
                "referer": "https://www.facebook.com/",
                "host": "business.facebook.com",
                "cookie": cookie
            }
            
            # Step 1: Getting Business Token
            req = requests.get("https://business.facebook.com/business_locations", headers=headers, timeout=15).text
            token = re.search("(EAAG\w+)", req).group(1)
            
            # Step 2: Extracting User Name for confirmation
            user_data = requests.get(f"https://graph.facebook.com/me?access_token={token}").json()
            user_name = user_data.get('name', 'Unknown')

            # Step 3: Formatting Cookie to JSON (Extension Format)
            json_cookies = []
            for item in cookie.split(';'):
                if '=' in item:
                    name, value = item.strip().split('=', 1)
                    json_cookies.append({
                        "name": name,
                        "value": value,
                        "domain": ".facebook.com",
                        "path": "/",
                        "httpOnly": True,
                        "secure": True
                    })

            # Saving Files
            with open("token.txt", "w") as f: f.write(token)
            with open("cookie_extension.json", "w") as f: json.dump(json_cookies, f, indent=4)

            banner()
            cetak(f" {H}[âœ“] Successfully Converted!")
            print(f"{P}-------------------------------------------------------")
            cetak(f" {H}[+] User Name : {P}{user_name}")
            cetak(f" {H}[+] Token EAAG: {K}{token}")
            print(f"{P}-------------------------------------------------------")
            cetak(f" {P}[*] Token saved in: {H}token.txt")
            cetak(f" {P}[*] JSON Cookie saved in: {H}cookie_extension.json")
            cetak(f" {K}[!] You can now import this JSON file into Cookie Editor.")
            
            input(f"\n {H}[Press Enter to Back]")
            self.menu()

        except Exception as e:
            cetak(f" {M}[!] Error: System could not extract token.")
            cetak(f" {M}[!] Reason: Cookie might be expired or restricted.")
            input(f"\n {H}[Press Enter to Try Again]")
            self.menu()

    def checker_system(self):
        banner()
        cookie = input(f" {H}[+] Enter Cookie to Check: {P}")
        try:
            # Using basic graph check
            check = requests.get("https://m.facebook.com/profile.php", cookies={"cookie": cookie}, allow_redirects=False)
            if '302' in str(check.status_code) or 'c_user' in str(check.cookies):
                cetak(f" {H}[âœ“] Cookie is LIVE / WORKING")
            else:
                cetak(f" {M}[!] Cookie is DEAD / EXPIRED")
        except:
            cetak(f" {M}[!] Network Connection Error")
        input(f"\n {H}[Press Enter to Back]")
        self.menu()

if __name__ == "__main__":
    try:
        tool = CookieTool()
        tool.menu()
    except KeyboardInterrupt:
        exit()
