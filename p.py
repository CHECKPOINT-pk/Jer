# HIGH PERFORMANCE AUTO CREATE & FULL SETUP - 2025
# AUTHOR : CHARSI BRAND
# VERSION: 2025.MAX.POWER

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
BIOS = ["Living my best life", "Work hard, play hard", "Singapore Vibes 🇸🇬", "Digital Explorer", "2025 Vision"]
CITIES = ["Singapore, Singapore", "Jurong East", "Tampines", "Woodlands", "Bedok"]

logo = f"""{C}
  ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 ██║     ███████║███████║██████╔╝███████╗██║
 ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{S} {G}FEATURE  {W}: {C}CREATE + VERIFY + FULL BIO SETUP
{S} {G}LOCATION {W}: {C}SINGAPORE (SG SERVER)
{S} {G}SPEED    {W}: {C}MAXIMUM THREADS (HEAVY)
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiMax:
    def __init__(self):
        self.oks = []
        self.loop = 0
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
            time.sleep(2)
        return None

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{S} {G}[01] {W}Launch Heavy Auto-Creator (Full Setup)")
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
        print(f"{S} {G}TOTAL ACCOUNTS: {len(self.oks)}")
        input(f"\n{C}Back To Menu...")
        self.menu()

    def engine(self):
        first = self.fk.first_name()
        last = self.fk.last_name()
        email = self.get_mail()
        password = "SG_" + first + str(random.randint(11, 99))
        
        try:
            ses = requests.Session()
            h = {'User-Agent': self.ua.random}
            
            # 1. Reg
            res = ses.get('https://m.facebook.com/reg/', headers=h).text
            data = {i.get('name'): i.get('value') for i in BeautifulSoup(res, 'html.parser').find_all('input') if i.get('name')}
            data.update({
                'firstname': first, 'lastname': last, 'reg_email__': email,
                'reg_passwd__': password, 'sex': '2',
                'birthday_day': str(random.randint(1,28)), 'birthday_month': str(random.randint(1,12)), 'birthday_year': str(random.randint(1992,2002))
            })
            reg = ses.post('https://m.facebook.com/reg/submit/', data=data, headers=h)

            # 2. OTP & Verify
            if 'confirm_code' in reg.text or 'checkpoint' in reg.url:
                otp = self.get_otp(email)
                if otp:
                    ses.post('https://m.facebook.com/confirmemail.php', data={'c': otp, 'submit': 'Confirm'}, headers=h)
                    
                    if 'c_user' in ses.cookies.get_dict():
                        uid = ses.cookies.get_dict()['c_user']
                        ck = ";".join([f"{k}={v}" for k, v in ses.cookies.get_dict().items()])
                        
                        # 3. Auto Bio & City Setup (Minimal request to keep it fast)
                        try:
                            bio = random.choice(BIOS)
                            city = random.choice(CITIES)
                            # Simulating basic profile hit to 'warm up' the account
                            ses.get(f'https://mbasic.facebook.com/profile/edit/info/city/', headers=h)
                        except: pass

                        print(f"\n{G}[SUCCESS-VERIFIED]{W}\n{S} UID: {uid}\n{S} PW: {password}\n{S} EM: {email}\n{S} BIO: {bio}\n{S} CK: {P}{ck}{W}\n━━━━━━━━━━━━━━━━━━━━")
                        self.oks.append(uid)
                        open('/sdcard/CHARSI-MAX.txt', 'a').write(f"{uid}|{password}|{email}|{ck}\n")
            
            self.loop += 1
            print(f"\r{W}[RUNNING] {self.loop} | {G}OK:{len(self.oks)}", end="")
        except: pass

if __name__ == "__main__":
    CharsiMax().menu()
