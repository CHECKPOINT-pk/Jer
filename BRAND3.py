import os, sys, time, json, string, random, pyfiglet, requests, hashlib
from ssl import CERT_NONE
from gzip import decompress
from concurrent.futures import ThreadPoolExecutor
from random import choice, choices
from json import dumps

# --- PRO COLORS (Yellow & Green Dashboard) ---
Y = '\033[1;33m'  # Yellow
G = '\033[1;32m'  # Green
W = '\033[1;37m'  # White
R = '\033[1;31m'  # Red
C = '\033[1;36m'  # Cyan
B = '\033[1;34m'  # Blue

try:
    from websocket import create_connection
except:
    os.system('pip install websocket-client')
    from websocket import create_connection

# --- GLOBAL VARIABLES & DATA ---
success, failed, retry = 0, 0, 0
accounts_log = []
nodes = [
    "193.200.173.45", "51.79.208.190", "164.92.111.139", 
    "185.242.118.188", "193.200.173.34"
]

# --- FUNCTIONS ---

def generate_charsi_id(length=15):
    """Generates a random login ID similar to hsjakaoqworiiww"""
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(1)) + \
           ''.join(random.choice(chars) for _ in range(length-1))

def get_random_device():
    """Simulates real Android hardware signatures"""
    devices = [
        {"model": "SM-G998B", "brand": "samsung", "os": "12"},
        {"model": "Pixel 7 Pro", "brand": "google", "os": "13"},
        {"model": "Xiaomi 12T", "brand": "Xiaomi", "os": "12"},
        {"model": "OnePlus 10 Pro", "brand": "OnePlus", "os": "13"}
    ]
    return random.choice(devices)

def charsi_banner():
    os.system('clear')
    ascii_art = pyfiglet.figlet_format("CHARSI-GOD", font="slant")
    print(Y + ascii_art)
    print(G + " ╔" + "═"*46 + "╗")
    print(Y + " ║  OWNER    : MR. GHOST (LONG SCRIPT EDITION)  ║")
    print(Y + " ║  METHOD   : WSS-ULTRA-BYPASS / TELENOR FIX   ║")
    print(Y + " ║  VERSION  : v9.0 (ULTRA HARD)                ║")
    print(G + " ╚" + "═"*45 + "╝" + W)

def save_result(username, phone):
    """Saves and sorts accounts by country code"""
    path = "SafeUM_Charsi_God.txt"
    country = "994" if phone.startswith("994") else ("380" if phone.startswith("380") else "371")
    with open(path, "a") as f:
        f.write(f"{username}:mmmm | {phone} | {country}\n")

def core_engine():
    """The main heavy-lifting registration logic"""
    global success, failed, retry
    
    login_id = generate_charsi_id()
    password_fix = "mmmm"
    device = get_random_device()
    target_node = random.choice(nodes)
    
    # Advanced GitHub Trick: Custom Salt for Encryption Simulation
    salt_m1x = hashlib.sha256(os.urandom(16)).hexdigest()
    salt_m1y = hashlib.sha256(os.urandom(16)).hexdigest()
    
    try:
        # Step 1: Secure Handshake with Heavy Headers
        ws = create_connection(
            f"wss://{target_node}/Auth",
            header={
                "app": "com.safeum.android",
                "User-Agent": f"SafeUM/1.1.0.1650 (Android {device['os']}; {device['model']})",
                "Accept-Encoding": "gzip",
                "Host": target_node
            },
            sslopt={"cert_reqs": CERT_NONE},
            timeout=20
        )

        # Step 2: Complex Payload (The 'Hard' part)
        registration_data = {
            "action": "Register",
            "subaction": "Desktop",
            "locale": "en_US",
            "gmt": f"+0{random.randint(3,8)}",
            "login": login_id,
            "password": {
                "m1x": salt_m1x,
                "m1y": salt_m1y,
                "m2": hashlib.sha256(os.urandom(24)).hexdigest(),
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
            "devicename": f"{device['brand']} {device['model']}",
            "softwareversion": "1.1.0.1650",
            "nickname": "charsi_" + "".join(random.choices(string.digits, k=4)),
            "os": "AND",
            "deviceuid": os.urandom(8).hex(),
            "devicepushuid": f"*APA91b{os.urandom(75).hex()}",
            "osversion": f"and_{device['os']}.0.0",
            "id": str(random.randint(1000000000, 9999999999))
        }

        # Step 3: Send & Decompress Response
        ws.send(dumps(registration_data))
        response_bytes = ws.recv()
        response_text = decompress(response_bytes).decode('utf-8')

        # Step 4: Validate Success
        if '"status":"Success"' in response_text:
            import re
            phone_search = re.findall(r'"phoneNumber":"(.*?)"', response_text)
            phone_num = phone_search[0] if phone_search else "371000000"
            
            success += 1
            save_result(login_id, phone_num)
            print(f"\n{G}[GOD-HIT] {login_id}:{password_fix} | {phone_num}")
        else:
            failed += 1
        
        ws.close()

    except Exception as e:
        retry += 1

# --- MULTI-THREADED RUNNER ---

def start_charsi_system():
    charsi_banner()
    # Telenor users k liye 15-20 threads best hain takay IP jaldi ban na ho
    with ThreadPoolExecutor(max_workers=20) as executor:
        while True:
            executor.submit(core_engine)
            # Dashboard update
            sys.stdout.write(
                f"\r {W}[{G}OK:{success}{W}] [{R}FAIL:{failed}{W}] [{Y}RETRY:{retry}{W}] {C}• NODE:{random.choice(nodes)[:5]}..."
            )
            sys.stdout.flush()
            time.sleep(0.02)

if __name__ == "__main__":
    try:
        start_charsi_system()
    except KeyboardInterrupt:
        print(f"\n{R}[!] System Stopped. Accounts saved in SafeUM_Charsi_God.txt")
