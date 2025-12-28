import os, sys, time, json, string, random, pyfiglet
from ssl import CERT_NONE
from gzip import decompress
from concurrent.futures import ThreadPoolExecutor
from random import choice, choices
from json import dumps

# --- PRO COLORS ---
Y = '\033[1;33m'  # Yellow
G = '\033[1;32m'  # Green
W = '\033[1;37m'  # White
R = '\033[1;31m'  # Red

try:
    from websocket import create_connection
except:
    os.system('pip install websocket-client')
    from websocket import create_connection

# --- GLOBAL STATS ---
success, failed, retry = 0, 0, 0

def change_ip():
    """Telenor IP Rotation via ADB/Root"""
    print(f"\n{Y}[!] Rotating Telenor IP Address...")
    try:
        # Airplane Mode ON
        os.system("settings put global airplane_mode_on 1")
        os.system("am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true")
        time.sleep(3)
        # Airplane Mode OFF
        os.system("settings put global airplane_mode_on 0")
        os.system("am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false")
        print(f"{G}[+] IP Changed Successfully. Waiting for network...")
        time.sleep(10) # Network restore hone ka wait
    except:
        print(f"{R}[!] Root/ADB Permission Denied. Switch Airplane Mode Manually!")

def work_engine():
    global success, failed, retry
    user = ''.join(choices(string.ascii_lowercase, k=15))
    nodes = ["193.200.173.45", "51.79.208.190", "164.92.111.139"]
    node = random.choice(nodes)

    try:
        con = create_connection(f"wss://{node}/Auth", header={"app": "com.safeum.android"}, sslopt={"cert_reqs": CERT_NONE}, timeout=15)
        
        payload = {
            "action": "Register",
            "subaction": "Desktop",
            "login": user,
            "password": {"m1x":os.urandom(32).hex(),"m1y":os.urandom(32).hex(),"iv":os.urandom(16).hex(),"message":os.urandom(64).hex()},
            "devicename": "Telenor Pro Max",
            "softwareversion": "1.1.0.1650",
            "os": "AND",
            "deviceuid": os.urandom(8).hex(),
            "osversion": "and_12.0.0",
            "id": str(random.randint(111111111, 999999999))
        }

        con.send(dumps(payload))
        res = decompress(con.recv()).decode('utf-8')

        if '"status":"Success"' in res:
            success += 1
            print(f"\n{G}[SUCCESS] {user}:mmmm")
            with open('Charsi_Telenor_Auto.txt', 'a') as f:
                f.write(f"{user}:mmmm\n")
        else:
            failed += 1
        con.close()
    except:
        retry += 1

# --- RUNNER ---
print(Y + pyfiglet.figlet_format("AUTO-IP-CHARSI"))

attempt_count = 0
while True:
    with ThreadPoolExecutor(max_workers=10) as exe:
        for _ in range(10): # 10 accounts ke baad IP change hogi
            exe.submit(work_engine)
            attempt_count += 1
            sys.stdout.write(f"\r {W}SUCCESS:[{G}{success}{W}] {R}FAILED:[{failed}] {W}TOTAL:[{attempt_count}]")
            sys.stdout.flush()
    
    # Har 10 attempts ke baad IP rotation function call hoga
    change_ip()
