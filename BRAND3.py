import os, sys, time, json, string, random, pyfiglet, hashlib
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

# --- PRO THEME COLORS ---
Y = '\033[1;33m' # Yellow (Main Theme)
G = '\033[1;32m' # Green
R = '\033[1;31m' # Red
W = '\033[1;37m' # White

# --- CONFIG (Same as login-acount.py) ---
VERSION = "1.1.0.1640"
FILE_SAVE = "Charsi_Hits.txt"
success = 0
failed = 0

def charsi_banner():
    os.system('clear')
    # Same Logo Style
    logo = pyfiglet.figlet_format("CHARSI-PRO", font="slant")
    print(Y + logo)
    print(G + " ╔" + "═"*46 + "╗")
    print(Y + " ║  AUTHOR   : MR. GHOST (CHARSI EDITION)    ║")
    print(Y + " ║  METHOD   : HEAVY WSS (VERSION 1.1.0.1640)║")
    print(Y + " ║  NETWORK  : TELENOR/ALL (BYPASS ACTIVE)   ║")
    print(Y + " ║  FORMAT   : USERNAME:mmmm                 ║")
    print(G + " ╚" + "═"*45 + "╝" + W)

def work_engine():
    global success, failed
    # Random Username: hsjakaoqworiiww style
    user = ''.join(choices(string.ascii_lowercase, k=14))
    
    # SafeUM Heavy Nodes
    nodes = ["193.200.173.45", "51.79.208.190", "164.92.111.139"]
    node = random.choice(nodes)

    try:
        # Secure Handshake
        ws = create_connection(
            f"wss://{node}/Auth",
            header={
                "app": "com.safeum.android",
                "remoteIp": node,
                "remotePort": "8080",
                "User-Agent": "SafeUM/1.1.0.1640 (Android 12; Xiaomi 220733SPH)"
            },
            sslopt={"cert_reqs": CERT_NONE},
            timeout=20
        )

        # Same Payload Structure as your file
        payload = {
            "action": "Register",
            "subaction": "Desktop",
            "locale": "en_IN",
            "gmt": "+05",
            "login": user,
            "password": {
                "m1x": hashlib.sha256(os.urandom(16)).hexdigest(),
                "m1y": hashlib.sha256(os.urandom(16)).hexdigest(),
                "m2": hashlib.sha256(os.urandom(20)).hexdigest(),
                "iv": os.urandom(16).hex(),
                "message": os.urandom(64).hex()
            },
            "magicword": {
                "m1x": hashlib.md5(os.urandom(8)).hexdigest(),
                "m1y": hashlib.md5(os.urandom(8)).hexdigest(),
                "m2": hashlib.md5(os.urandom(12)).hexdigest(),
                "iv": os.urandom(16).hex(),
                "message": os.urandom(32).hex()
            },
            "magicwordhint": "0000",
            "devicename": "Xiaomi 220733SPH",
            "softwareversion": VERSION,
            "os": "AND",
            "deviceuid": os.urandom(8).hex(),
            "devicepushuid": f"*eL-{os.urandom(55).hex()}",
            "osversion": "and_12.0.0",
            "id": str(random.randint(1111111111, 1999999999))
        }

        ws.send(dumps(payload))
        response = decompress(ws.recv()).decode('utf-8')

        if '"status":"Success"' in response:
            success += 1
            account_hit = f"{user}:mmmm"
            print(f"\n{G}[SUCCESS] {account_hit}")
            with open(FILE_SAVE, "a") as f:
                f.write(account_hit + "\n")
        else:
            failed += 1
        ws.close()
    except:
        pass

# --- RUNNER ---
charsi_banner()
print(Y + " [*] Engine starting... Telenor bypass active.")

# 20 threads for high speed & stability
with ThreadPoolExecutor(max_workers=20) as executor:
    while True:
        executor.submit(work_engine)
        # Professional Live Dashboard
        sys.stdout.write(f"\r {W}[{Y}GHOST-PRO{W}] OK:[{G}{success}{W}] FAIL:[{R}{failed}{W}]")
        sys.stdout.flush()
        time.sleep(0.05)
