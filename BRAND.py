import os, sys, time, json, string, random, pyfiglet
from ssl import CERT_NONE
from gzip import decompress
from concurrent.futures import ThreadPoolExecutor
from random import choice, choices
from json import dumps

try:
    from websocket import create_connection
except:
    os.system('pip install websocket-client')
    from websocket import create_connection

# --- PRO COLORS (Yellow/Green Theme) ---
Y = '\033[1;33m'  # Yellow
G = '\033[1;32m'  # Green
W = '\033[1;37m'  # White
R = '\033[1;31m'  # Red
C = '\033[1;36m'  # Cyan

# --- STATS ---
success = 0
failed = 0
retry = 0
az_994 = 0
uk_380 = 0
lv_371 = 0
accounts = []

def pro_logo():
    os.system('clear')
    banner = pyfiglet.figlet_format("CHARSI-PRO")
    print(Y + banner)
    print(G + " (+) " + "="*45 + " (+)")
    print(Y + "  [•] OWNER    : MR. GHOST (PRO EDITION)")
    print(Y + "  [•] METHODS  : MULTI-NODE / WSS-BYPASS / AUTO-SORT")
    print(Y + "  [•] TARGET   : AZERBAIJAN / UKRAINE / LATVIA")
    print(Y + "  [•] PASS     : mmmm")
    print(G + " (+) " + "="*45 + " (+)")

def save_data(user, psw, phone):
    global az_994, uk_380, lv_371
    entry = f"{user}:mmmm | {phone}\n"
    
    # Auto-Sorting logic based on Country Code
    if phone.startswith('994'):
        az_994 += 1
        with open('Pro_Azerbaijan_994.txt', 'a') as f: f.write(entry)
    elif phone.startswith('380'):
        uk_380 += 1
        with open('Pro_Ukraine_380.txt', 'a') as f: f.write(entry)
    else:
        lv_371 += 1
        with open('Pro_Latvia_371.txt', 'a') as f: f.write(entry)

def heavy_work():
    global success, failed, retry
    # Username Format: hsjakaoqworiiww
    user = ''.join(choices(string.ascii_lowercase, k=14))
    
    # Method 1: Multiple Node Rotation (Heavy IPs)
    nodes = ["193.200.173.45", "51.79.208.190", "164.92.111.139", "185.242.118.188"]
    selected_node = random.choice(nodes)

    try:
        con = create_connection(
            f"wss://{selected_node}/Auth", 
            header={"app": "com.safeum.android", "remoteIp": selected_node},
            sslopt={"cert_reqs": CERT_NONE}, 
            timeout=12
        )

        # Method 2: Random Device UID & Push Token (Bypass Rejection)
        device_uid = os.urandom(8).hex()
        push_token = "APA91b" + ''.join(choices(string.ascii_letters + string.digits, k=120))

        # Method 3: Hardcoded Encrypted Keys (From your original script)
        payload = {
            "action": "Register",
            "subaction": "Desktop",
            "locale": "en_GB",
            "gmt": "+02",
            "password": {
                "m1x": "503c73d12b354f86ff9706b2114704380876f59f1444133e62ca27b5ee8127cc",
                "m1y": "6387ae32b7087257452ae27fc8a925ddd6ba31d955639838249c02b3de175dfc",
                "m2": "219d1d9b049550f26a6c7b7914a44da1b5c931eff8692dbfe3127eeb1a922fcf",
                "iv": os.urandom(16).hex(),
                "message": os.urandom(64).hex()
            },
            "login": user,
            "devicename": choice(["Xiaomi Redmi Note 10", "Samsung S21 Ultra", "Pixel 6 Pro"]),
            "softwareversion": "1.1.0.1640",
            "os": "AND",
            "deviceuid": device_uid,
            "devicepushuid": f"*{push_token}",
            "osversion": "and_12.0.0",
            "id": str(random.randint(111111111, 999999999))
        }

        con.send(dumps(payload))
        raw_res = con.recv()
        res = decompress(raw_res).decode('utf-8')

        if '"status":"Success"' in res:
            success += 1
            # Extract Phone Number from Response
            import re
            p_find = re.findall(r'"phoneNumber":"(.*?)"', res)
            phone = p_find[0] if p_find else "Unknown"
            
            save_data(user, "mmmm", phone)
            accounts.append(f"{Y}{user}:mmmm {G}[{phone}]")
        else:
            failed += 1
        con.close()
    except:
        retry += 1

# --- RUNNER ---
pro_logo()
# Professional Thread Pool for speed
with ThreadPoolExecutor(max_workers=50) as engine:
    while True:
        engine.submit(heavy_work)
        # Professional Dashboard Print
        sys.stdout.write(
            f"\r {G}OK:[{success}] {Y}994:[{az_994}] {C}380:[{uk_380}] {W}371:[{lv_371}] {R}ERR:[{failed}] {Y}TRY:[{retry}]"
        )
        sys.stdout.flush()
        
        # Periodic Clear to show recent hits
        if success > 0 and success % 10 == 0:
            print(f"\n {G}[RECENT]: {accounts[-1]}")
            time.sleep(0.5)
