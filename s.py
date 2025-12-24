# HIGH PERFORMANCE AUTO CREATE & FULL SETUP - 2025
# AUTHOR : CHARSI BRAND
# VERSION: 2025.REAL.SYSTEM

import os, sys, re, time, random, uuid, string, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def setup():
    modules = ['requests', 'bs4', 'faker', 'fake-useragent']
    for mod in modules:
        try: __import__(mod)
        except: subprocess.check_call([sys.executable, "-m", "pip", "install", mod])

setup()

import requests
from bs4 import BeautifulSoup
from faker import Faker
from fake_useragent import UserAgent

#---[ COLORS ]---#
G = "\033[1;32m"; C = "\033[1;36m"; W = "\033[1;37m"; R = "\033[1;31m"; Y = "\033[1;33m"; P = "\033[1;35m"
S = f"{W}[{C}◈{W}]"

#---[ DATA ]---#
SG_API = "https://www.1secmail.com/api/v1/action"

logo = f"""{C}
  ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 ██║     ███████║███████║██████╔╝███████╗██║
 ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{S} {G}SYSTEM   {W}: {C}REAL-TIME ACCOUNT CREATION
{S} {G}LOCATION {W}: {C}SINGAPORE (SG SERVER)
{S} {G}VERIFY   {W}: {C}AUTOMATIC OTP FETCHING
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiReal:
    def __init__(self):
        self.oks = []
        self.ua = UserAgent()
        self.fk = Faker()

    def get_mail(self):
        user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        domain = random.choice(['1secmail.com', '1secmail.org', '1secmail.net'])
        return f"{user}@{domain}"

    def get_otp(self, email):
        user, domain = email.split('@')
        for _ in range(30):
            try:
                res = requests.get(f"{SG_API}?action=getMessages&login={user}&domain={domain}").json()
                if res:
                    m_id = res[0]['id']
                    msg = requests.get(f"{SG_API}?action=readMessage&login={user}&domain={domain}&id={m_id}").json()
                    otp = re.search(r'\b\d{5}\b', msg['body'])
                    if otp: return otp.group(0)
            except: pass
            time.sleep(1)
        return None

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{S} {G}[01] {W}Start Real-Time Auto Creation")
        print(f"{S} {R}[00] {W}Exit")
        opt = input(f"\n{C}⚡ {W}Action: {G}")
        if opt in ['1', '01']: self.start()
        else: exit()

    def start(self):
        os.system('clear'); print(logo)
        limit = int(input(f"{S} {W}Limit: {G}"))
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        with ThreadPool(max_workers=35) as pool:
            for _ in range(limit):
                pool.submit(self.engine)
        
        print(f"\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{S} {G}CREATION FINISHED | TOTAL OK: {len(self.oks)}")
        input(f"\n{C}Back To Menu...")
        self.menu()

    def engine(self):
        first = self.fk.first_name()
        last = self.fk.last_name()
        email = self.get_mail()
        password = "SG_" + first + str(random.randint(11, 99))
        
        # Real-time Status Update
        print(f"{W}[{Y}⚙{W}] {C}Creating: {W}{first} {last}...")
        
        try:
            ses = requests.Session()
            h = {'User-Agent': self.ua.random}
            
            # Step 1: Request Registration
            res = ses.get('https://m.facebook.com/reg/', headers=h).text
            data = {i.get('name'): i.get('value') for i in BeautifulSoup(res, 'html.parser').find_all('input') if i.get('name')}
            data.update({
                'firstname': first, 'lastname': last, 'reg_email__': email,
                'reg_passwd__': password, 'sex': '2',
                'birthday_day': str(random.randint(1,28)), 
                'birthday_month': str(random.randint(1,12)), 
                'birthday_year': str(random.randint(1992,2002))
            })
            reg = ses.post('https://m.facebook.com/reg/submit/', data=data, headers=h)

            # Step 2: Real-time Verification Update
            if 'confirm_code' in reg.text or 'checkpoint' in reg.url:
                print(f"{W}[{Y}⚡{W}] {Y}Verification: {W}Fetching OTP for {email}...")
                otp = self.get_otp(email)
                
                if otp:
                    print(f"{W}[{G}✔{W}] {G}Code Found: {W}{otp}")
                    ses.post('https://m.facebook.com/confirmemail.php', data={'c': otp, 'submit': 'Confirm'}, headers=h)
                    
                    if 'c_user' in ses.cookies.get_dict():
                        uid = ses.cookies.get_dict()['c_user']
                        ck = ";".join([f"{k}={v}" for k, v in ses.cookies.get_dict().items()])
                        
                        # Step 3: Success Result
                        print(f"{G}[SUCCESS] {uid} | {password} | Verified")
                        self.oks.append(uid)
                        with open('/sdcard/CHARSI-REAL.txt', 'a') as f:
                            f.write(f"{uid}|{password}|{email}|{ck}\n")
                    else:
                        print(f"{R}[FAILED] Account Checkpoint")
                else:
                    print(f"{R}[TIMEOUT] OTP not received for {email}")
            else:
                print(f"{R}[FAILED] Could not reach verification page")
                
        except Exception as e:
            print(f"{R}[ERROR] Connection Issue")

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiReal().menu()
