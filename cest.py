# HIGH PERFORMANCE AUTO CREATE & VERIFY - 2025 ULTRA
# AUTHOR : CHARSI BRAND
# FEATURES: AUTO EMAIL GENERATE | AUTO OTP FETCH | AUTO VERIFY

import os, sys, re, time, random, uuid, string, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#---[ DEPENDENCIES ]---#
def install_modules():
    modules = ['requests', 'bs4', 'faker', 'fake-useragent']
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

install_modules()

import requests
from bs4 import BeautifulSoup
from faker import Faker
from fake_useragent import UserAgent

#---[ COLORS ]---#
G = "\033[1;32m"; C = "\033[1;36m"; W = "\033[1;37m"; R = "\033[1;31m"; Y = "\033[1;33m"
S = f"{W}[{C}◈{W}]"

#---[ API CONFIG ]---#
API_MAIL = "https://www.1secmail.com/api/v1/action"

logo = f"""{C}
  ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 ██║     ███████║███████║██████╔╝███████╗██║
 ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{S} {G}SYSTEM   {W}: {C}AUTO-VERIFICATION ENABLED (2025)
{S} {G}METHOD   {W}: {C}OTP BYPASS & EMAIL CONFIRM
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiVerify:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.ua = UserAgent()
        self.fk = Faker()

    def get_mail(self):
        """Temporary Email Generate Karna"""
        user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        domain = random.choice(['kz6.me', 'ovz.me', '1secmail.com'])
        return f"{user}@{domain}"

    def get_otp(self, email):
        """Email se OTP nikalna"""
        user, domain = email.split('@')
        for _ in range(20): # 20 baar check karega 
            time.sleep(2)
            res = requests.get(f"{API_MAIL}?action=getMessages&login={user}&domain={domain}").json()
            if res:
                msg_id = res[0]['id']
                msg_content = requests.get(f"{API_MAIL}?action=readMessage&login={user}&domain={domain}&id={msg_id}").json()
                otp = re.search(r'\b\d{5}\b', msg_content['body'])
                if otp: return otp.group(0)
        return None

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{S} {W}[01] Start Creation + Auto Verify")
        print(f"{S} {W}[00] Exit")
        opt = input(f"\n{C}⚡ {W}Select: {G}")
        if opt in ['1', '01']: self.start()
        else: exit()

    def start(self):
        os.system('clear'); print(logo)
        limit = int(input(f"{S} {W}Limit: {G}"))
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        with ThreadPool(max_workers=30) as pool:
            for _ in range(limit):
                pool.submit(self.create_and_verify)
        print(f"\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{S} {G}VERIFIED OK: {len(self.oks)}")
        input(f"\n{C}Press Enter...")

    def create_and_verify(self):
        first = self.fk.first_name()
        last = self.fk.last_name()
        email = self.get_mail()
        password = first + str(random.randint(111, 999))
        birthday = f"{random.randint(1992, 2005)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
        
        try:
            ses = requests.Session()
            # Step 1: Registration Request
            res = ses.get('https://m.facebook.com/reg/', headers={'User-Agent': self.ua.random})
            soup = BeautifulSoup(res.text, 'html.parser')
            data = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            
            data.update({
                'firstname': first, 'lastname': last, 'reg_email__': email,
                'reg_passwd__': password, 'sex': '2',
                'birthday_day': birthday.split('-')[2],
                'birthday_month': birthday.split('-')[1],
                'birthday_year': birthday.split('-')[0],
            })
            
            reg = ses.post('https://m.facebook.com/reg/submit/', data=data)
            
            # Step 2: Verification System
            if 'confirm_code' in reg.text or 'checkpoint' in reg.url:
                print(f"\r{Y}[FETCHING-OTP] {email}...          ", end="")
                otp = self.get_otp(email)
                
                if otp:
                    v_data = {'c': otp, 'submit': 'Confirm'}
                    confirm = ses.post('https://m.facebook.com/confirmemail.php', data=v_data)
                    
                    if 'c_user' in ses.cookies.get_dict():
                        uid = ses.cookies.get_dict()['c_user']
                        print(f"\r{G}[CHARSI-VERIFIED] {uid} | {password} | {email} ")
                        self.oks.append(uid)
                        open('/sdcard/CHARSI-VERIFIED.txt', 'a').write(f"{uid}|{password}|{email}\n")
                    else:
                        self.cps.append(email)
                else:
                    self.cps.append(email)
            
            self.loop += 1
            print(f"\r{W}[RUNNING] {self.loop} | {G}OK:{len(self.oks)}", end="")
        except: pass

if __name__ == "__main__":
    CharsiVerify().menu()
