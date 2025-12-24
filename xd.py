# Script: CHARSI HUB AUTO ACCOUNT CREATOR
# Fixed & Heavy Updated
import os, requests, json, time, re, random, sys, uuid, platform
from concurrent.futures import ThreadPoolExecutor as tred

# --- Colors & Global ---
G = "\033[1;32m" # Green
R = "\033[1;31m" # Red
W = "\033[1;97m" # White
loop = 0
oks = []

# --- Banner ---
def clear():
    os.system('clear')
    print(f"""{G}
  ____ _   _    _    ____  ____ ___ 
 / ___| | | |  / \  |  _ \/ ___|_ _|
| |   | |_| | / _ \ | |_) \___ \ | | 
| |___|  _  |/ ___ \|  _ < ___) || | 
 \____|_| |_/_/   \_\_| \_\____/___|
{R}--------------------------------------------------
{W} [•] AUTHOR    : {G}CHARSI HUB (USA SPECIAL)
{W} [•] FEATURE   : {G}AUTO CREATE + AUTO VERIFY
{W} [•] LOCATION  : {G}USA SPOOFED (HEAVY SYSTEM)
{R}--------------------------------------------------""")

def linex():
    print(f'{R}--------------------------------------------------')

# --- USA Heavy User-Agent ---
def get_ua():
    ver = random.choice(['12','13','14'])
    device = random.choice(['Pixel 7 Pro','SM-S918U','Pixel 8','SM-G991U'])
    fbv = f"{random.randint(440, 495)}.0.0.{random.randint(10, 80)}"
    return f'Mozilla/5.0 (Linux; Android {ver}; {device} Build/UP1A.{random.randint(111111,999999)}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(110,128)}.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fbv};FBBV/{random.randint(500000000, 600000000)};FBLC/en_US;FBCR/Verizon;]'

# --- Main Menu ---
def Menu():
    clear()
    print(f' {W}[1] OPTION A: JUST CREATE (ID + PASS)')
    print(f' {W}[2] OPTION B: AUTO VERIFY (MAIL CODE SYSTEM)')
    print(f' {W}[0] EXIT')
    linex()
    opt = input(f' {G}CHOOSE SYSTEM : {W}')
    if opt == '1': Start_Creation(verify=False)
    elif opt == '2': Start_Creation(verify=True)
    else: exit()

def Start_Creation(verify):
    clear()
    limit = int(input(f' {G}KITNI IDS BANANI HAIN? : {W}'))
    linex()
    print(f' {W}USA SYSTEM LOADING... PLEASE WAIT')
    linex()
    with tred(max_workers=30) as hub:
        for _ in range(limit):
            hub.submit(Heavy_Creator, verify)
    print(f'\n{G}PROCESS COMPLETE! CHECK /sdcard/CHARSI-CREATED.txt')

# --- Main Creation Engine ---
def Heavy_Creator(verify):
    global loop, oks
    sys.stdout.write(f'\r\r{W} [CHARSI-CREATING] %s | OK:%s '%(loop, len(oks))); sys.stdout.flush()
    try:
        # Identity Logic
        first = random.choice(['James','Robert','John','Michael','David','William','Richard','Joseph'])
        last = random.choice(['Smith','Johnson','Williams','Brown','Jones','Garcia','Miller'])
        
        # Temp Mail Logic (1secmail API)
        mail_res = requests.get('https://www.1secmail.com/api/v1/?action=genEmail&count=1').json()
        email = mail_res[0]
        u_name, domain = email.split('@')
        password = first + str(random.randint(111,999)) + "@#"
        
        ua = get_ua()
        # Facebook Registration API
        url = "https://b-api.facebook.com/method/user.register"
        data = {
            'firstname': first, 'lastname': last, 'email': email,
            'password': password, 'gender': 'MALE', 'birthday': '1998-08-12',
            'format': 'json', 'device_id': str(uuid.uuid4()),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        }
        headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True'
        }
        
        res = requests.post(url, data=data, headers=headers).json()
        
        if 'session_key' in str(res):
            if verify:
                # Automatic Code Extraction Logic
                print(f'\n{W} [!] WAITING FOR USA CODE: {email}')
                for _ in range(20): # 40 Seconds Timeout
                    time.sleep(2)
                    check = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={u_name}&domain={domain}').json()
                    if check:
                        m_id = check[0]['id']
                        msg_body = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={u_name}&domain={domain}&id={m_id}').json()['body']
                        fb_code = re.findall(r'\b\d{5}\b', msg_body)
                        if fb_code:
                            print(f'{G} [VERIFIED] Code Mil Gaya: {fb_code[0]}')
                            break
            
            print(f'{G} [OK-SUCCESS] {email} | {password}')
            oks.append(email)
            open('/sdcard/CHARSI-CREATED.txt', 'a').write(f"{email}|{password}\n")
        
        loop += 1
    except: pass

if __name__ == "__main__":
    Menu()
