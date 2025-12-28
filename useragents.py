# -*- coding: utf-8 -*-
# AUTHOR : CHARSI MASTER (ULTRA PRO)
# UPDATE : UNLIMITED API + 30 METHODS
# AGENTS : SAMSUNG + FB-APP + GLOBAL MIX

import os, sys, time, re, json, requests, bs4, random, datetime
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

# --- 10 Samsung VIP User-Agents ---
def samsung_ua():
    return random.choice([
        "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; SM-J600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; SM-X906B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.0.0 Mobile Safari/537.36"
    ])

# --- 10 Facebook App User-Agents ---
def fb_app_ua():
    return random.choice([
        "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/340.0.0.0;]",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBAV/415.0.0.0;]",
        "Mozilla/5.0 (Linux; Android 11; Infinix X6811) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/315.0.0.0;]",
        "Mozilla/5.0 (Linux; Android 13; SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/415.0.0.0;]",
        "Mozilla/5.0 (Linux; Android 10; Mi A3) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/280.0.0.0;]",
        "Mozilla/5.0 (Linux; Android 12; Oppo Reno7) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/365.0.0.0;]",
        "Mozilla/5.0 (Linux; Android 11; TECNO KG5k) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/330.0.0.0;]",
        "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.0;]",
        "Mozilla/5.0 (Linux; Android 13; OnePlus 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.0;]",
        "Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/170.0.0.0;]"
    ])

# --- 10 Global Country Special Agents (Pak, Ind, etc.) ---
def country_ua():
    return random.choice([
        "Mozilla/5.0 (Linux; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; Lenovo TB-X606F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; V2124) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; RMX3363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; moto g(8) power) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; HONOR ANY-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; Sony XQ-CT54) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; LG-H930) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36"
    ])

# --- Charsi Professional Banner ---
def banner():
    os.system("clear")
    print(f"""{H}
   ___ _  _   _   ___  ___ ___ 
  / __| || | /_\ | _ \/ __|_ _|
 | (__| __ |/ _ \|   /\__ \| | 
  \___|_||_/_/ \_\_|_\|___/___|
  {P}-----------------------------------
  {K}Owner   : CHARSI MASTER PRO
  {K}Workers : 30 METHODS (UNLIMITED)
  {K}Agents  : 30 (SAMSUNG/FB/COUNTRY)
  {P}-----------------------------------{N}""")

# --- Countries SIM Codes ---
countries = {
    "1": {"name": "Pakistan", "code": "+92", "sim": ["300","301","302","304","315","333","345"]},
    "2": {"name": "India", "code": "+91", "sim": ["91","98","70","81"]},
    "3": {"name": "Bangladesh", "code": "+880", "sim": ["17","18","19"]},
    "4": {"name": "Nigeria", "code": "+234", "sim": ["703","803","906"]},
}

class CharsiUltimate:
    def __init__(self):
        self.ids = []

    def main_menu(self):
        banner()
        print(" [01] Random Cloning (Global)")
        print(" [02] File Cloning (Txt File)")
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
        print(f" {H}Total IDs: {len(self.ids)} | Methods: 30{N}")
        print("-" * 35)
        with tred(max_workers=30) as engine:
            for user_data in self.ids:
                uid, name = user_data.split("<=>") if "<=>" in user_data else (user_data, "User")
                pwx = [uid, name, name+'123', name+'1234', '786786', 'pakistan']
                engine.submit(self.master_work, uid, pwx)
        print(f"\n {H}Cloning Done.")

    def master_work(self, uid, pwx):
        global loop, ok, cp
        sys.stdout.write(f'\r [CHARSI] {loop}/{len(self.ids)} OK:{len(ok)} '); sys.stdout.flush()
        
        session = requests.Session()
        # Mix of Samsung, FB App and Country agents
        ua = random.choice([samsung_ua(), fb_app_ua(), country_ua()])
        
        for pw in pwx:
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'referer': 'https://m.facebook.com/',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="114"',
                'user-agent': ua,
            }
            # API logic and Request yahan aayegi
            pass
        loop += 1

if __name__ == '__main__':
    CharsiUltimate().main_menu()
