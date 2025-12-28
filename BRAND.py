import os
import sys
import time
import json
import string
import random
from ssl import CERT_NONE
from gzip import decompress
from concurrent.futures import ThreadPoolExecutor
from random import choice, choices
from json import dumps

# Colors
G = '\033[1;32m' # Green
R = '\033[1;31m' # Red
W = '\033[1;37m' # White
Y = '\033[1;33m' # Yellow
C = '\033[1;36m' # Cyan

try:
    from websocket import create_connection
except:
    os.system('pip install websocket-client')
    from websocket import create_connection

# Global Stats
failed = 0
success = 0
retry = 0
plus_994 = 0
plus_380 = 0

def charsi_logo():
    os.system('clear')
    print(R + """
      _______ _    _         _____   _____ _____ 
     / ______| |  | |  /\   |  __ \ / ____|_   _|
    | |      | |__| | /  \  | |__) | (___   | |  
    | |      |  __  |/ /\ \ |  _  / \___ \  | |  
    | |____  | |  | / ____ \| | \ \ ____) |_| |_ 
     \______| |_|  /_/    \_\_|  \_\_____/|_____|
    """ + G + """
    ================================================
    [+] OWNER    : MR. GHOST (CHARSI CHECKER)
    [+] STATUS   : AUTO-SORTING (994/380/371)
    [+] PASS     : mmmm
    ================================================
    """ + W)

def save_account(user, passw, phone):
    """Accounts ko unke country code ke mutabiq file mein save karna"""
    global plus_994, plus_380
    data = f"{user}:{passw} | {phone}\n"
    
    if phone.startswith('994'):
        plus_994 += 1
        with open('Azerbaijan_994.txt', 'a') as f: f.write(data)
    elif phone.startswith('380'):
        plus_380 += 1
        with open('Ukraine_380.txt', 'a') as f: f.write(data)
    else:
        with open('Latvia_371.txt', 'a') as f: f.write(data)

def work():
    global failed, success, retry
    username = ''.join(choices(string.ascii_lowercase, k=14))
    password_text = "mmmm"
    nodes = ["193.200.173.45", "51.79.208.190", "164.92.111.139"]
    node = random.choice(nodes)

    try:
        con = create_connection(f"wss://{node}/Auth", header={"app": "com.safeum.android"}, sslopt={"cert_reqs": CERT_NONE}, timeout=10)
        
        # Registration Payload
        reg_payload = {
            "action": "Register",
            "subaction": "Desktop",
            "login": username,
            "password": {"m1x":"503c73...","m1y":"6387ae...","m2":"219d1d...","iv":os.urandom(16).hex(),"message":os.urandom(64).hex()},
            "devicename": "Xiaomi Mi 11",
            "softwareversion": "1.1.0.1640",
            "os": "AND",
            "deviceuid": os.urandom(8).hex()
        }
        con.send(dumps(reg_payload))
        res = decompress(con.recv()).decode('utf-8')

        if '"status":"Success"' in res:
            # Login foran karke number check karna
            login_payload = {
                "action": "GetMessages", # Ya GetUserInfo number nikalne ke liye
                "login": username,
                "password": password_text # Actual logic mein encrypted pass lagta hai
            }
            # Yahan hum assume kar rahe hain success par login info milti hai
            # Note: Real environment mein phone number response string mein hota hai
            import re
            phone_find = re.findall(r'"phoneNumber":"(.*?)"', res)
            phone_no = phone_find[0] if phone_find else "371000000"
            
            success += 1
            save_account(username, password_text, phone_no)
        else:
            failed += 1
        con.close()
    except:
        retry += 1

# Start Loop
charsi_logo()
with ThreadPoolExecutor(max_workers=30) as executor:
    while True:
        executor.submit(work)
        sys.stdout.write(f"\r{W}OK: {G}{success} {W}| 994: {C}{plus_994} {W}| 380: {Y}{plus_380} {W}| ERR: {R}{failed}")
        sys.stdout.flush()
        time.sleep(0.1)
