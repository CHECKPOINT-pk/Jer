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

# --- PRO COLORS ---
Y = '\033[1;33m'  # Yellow
G = '\033[1;32m'  # Green
R = '\033[1;31m'  # Red
W = '\033[1;37m'  # White

# --- CONFIG ---
VERSION = "1.1.0.1640"  # Same as your file
FILE_NAME = "Charsi_SafeUM_Success.txt"

def charsi_banner():
    os.system('clear')
    print(Y + pyfiglet.figlet_format("GHOST-1640"))
    print(G + " ╔" + "═"*46 + "╗")
    print(Y + f" ║ VERSION : {VERSION} (MATCHED WITH YOUR FILE) ║")
    print(Y + " ║ NETWORK : TELENOR BYPASS ACTIVE             ║")
    print(Y + " ║ FORMAT  : username:mmmm                      ║")
    print(G + " ╚" + "═"*45 + "╝" + W)

def work():
    global success, failed, retry
    # Generate random 15-char username
    user = ''.join(choices(string.ascii_lowercase, k=15))
    
    # SafeUM Servers
    nodes = ["193.200.173.45", "51.79.208.190", "164.92.111.139"]
    node = random.choice(nodes)

    try:
        # Step 1: Secure Connection
        con = create_connection(
            f"wss://{node}/Auth",
            header={
                "app": "com.safeum.android",
                "remoteIp": node,
                "remotePort": "8080",
                "softwareversion": VERSION
            },
            sslopt={"cert_reqs": CERT_NONE},
            timeout=15
        )

        # Step 2: Payload (Matched with login-acount.py logic)
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
            "nickname": "charsi_" + str(random.randint(100, 999)),
            "os": "AND",
            "deviceuid": os.urandom(8).hex(),
            "devicepushuid": f"*eL-{os.urandom(60).hex()}",
            "osversion": "and_12.0.0",
            "id": str(random.randint(1111111111, 1999999999))
        }

        con.send(dumps(payload))
        response = decompress(con.recv()).decode('utf-8')

        if '"status":"Success"' in response:
            # Format: username:mmmm
            account_hit = f"{user}:mmmm"
            print(f"\n{G}[SUCCESS] {account_hit}")
            with open(FILE_NAME, "a") as f:
                f.write(account_hit + "\n")
        
        con.close()
    except:
        pass

# --- MAIN ---
success, failed, retry = 0, 0, 0
charsi_banner()

# Telenor ke liye 20 threads stable hain
with ThreadPoolExecutor(max_workers=20) as ghost:
    while True:
        ghost.submit(work)
        sys.stdout.write(f"\r {W}[{G}v1640{W}] Engine Running... Check {FILE_NAME}")
        sys.stdout.flush()
        time.sleep(0.05)
