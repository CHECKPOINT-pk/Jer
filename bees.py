# HIGH PERFORMANCE AUTO CREATE & VERIFY - SINGAPORE + COOKIES
# AUTHOR : CHARSI BRAND
# VERSION: 2025.6.0 (ULTRA PREMIUM)

import os, sys, re, time, random, uuid, string, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#---[ DEPENDENCIES ]---#
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

#---[ API ]---#
SG_API = "https://www.1secmail.com/api/v1/action"

logo = f"""{G}
  ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 ██║     ███████║███████║██████╔╝███████╗██║
 ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{S} {G}SYSTEM   {W}: {C}VERIFIED + COOKIES GENERATOR
{S} {G}SERVER   {W}: {C}SINGAPORE (SG) 2025
{S} {G}AUTHOR   {W}: {C}CHARSI BRAND
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiUltra:
    def __init__(self):
        self.oks = []
        self.loop = 0
        self.ua = UserAgent()
        self.fk = Faker()

    def generate_sg_mail(self):
        user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        domain = random.choice(['1secmail.com', '1secmail.org', '1secmail.net'])
        return f"{user}@{domain}"

    def fetch_otp(self, email):
        user, domain = email.split('@')
        for _ in range(25):
            try:
                res = requests.get(f"{SG_API}?action=getMessages&login={user}&domain={domain}").json()
                if res:
                    msg_id = res[0]['id']
                    msg = requests.get(f"{SG_API}?action=readMessage&login={user}&domain={domain}&id={msg_id}").json()
                    otp = re.search(r'\b\d{5}\b', msg['body'])
                    if otp: return otp.group(0)
            except: pass
            time.sleep(2)
        return None

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{S} {G}[01] {W}Start Ultra Creation (Verify + Cookies)")
        print(f"{S} {R}[00] {W}Exit")
        opt = input(f"\n{C}⚡ {W}Choose: {G}")
        if opt in ['1', '01']: self.start()
        else: exit()

    def start(self):
        os.system('clear'); print(logo)
        try: limit = int(input(f"{S} {W}Limit: {G}"))
        except: limit = 5
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        with ThreadPool(max_workers=30) as pool:
            for _ in range(limit):
                pool.submit(self.create_ultra)
        print(f"\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{S} {G}SUCCESS: {len(self.oks)}")
        input(f"\n{C}Press Enter...")
        self.menu()

    def create_ultra(self):
        first = self.fk.first_name()
        last = self.fk.last_name()
        email = self.generate_sg_mail()
        password = first + str(random.randint(111, 999)) + "##"
        
        try:
            ses = requests.Session()
            header = {'User-Agent': self.ua.random}
            
            # Phase 1: Registration
            reg_page = ses.get('https://m.facebook.com/reg/', headers=header).text
            soup = BeautifulSoup(reg_page, 'html.parser')
            data = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            data.update({
                'firstname': first, 'lastname': last, 'reg_email__': email,
                'reg_passwd__': password, 'sex': '2',
                'birthday_day': str(random.randint(1,28)), 
                'birthday_month': str(random.randint(1,12)), 
                'birthday_year': str(random.randint(1992,2004)),
            })
            reg_res = ses.post('https://m.facebook.com/reg/submit/', data=data, headers=header)
            
            # Phase 2: Verification
            if 'confirm_code' in reg_res.text or 'checkpoint' in reg_res.url:
                otp = self.fetch_otp(email)
                if otp:
                    v_payload = {'c': otp, 'submit': 'Confirm'}
                    ses.post('https://m.facebook.com/confirmemail.php', data=v_payload, headers=header)
                    
                    if 'c_user' in ses.cookies.get_dict():
                        uid = ses.cookies.get_dict()['c_user']
                        # Cookie Extraction
                        cookie = ";".join([f"{k}={v}" for k, v in ses.cookies.get_dict().items()])
                        
                        print(f"\n{G}[CHARSI-VERIFIED-OK]{W}\n{S} ID: {uid}\n{S} PW: {password}\n{S} EM: {email}\n{S} CK: {P}{cookie}{W}\n━━━━━━━━━━━━━━━━━━━━")
                        
                        self.oks.append(uid)
                        with open('/sdcard/CHARSI-ULTRA.txt', 'a') as f:
                            f.write(f"{uid}|{password}|{email}|{cookie}\n")
            
            self.loop += 1
            print(f"\r{W}[RUNNING] {self.loop} | {G}OK:{len(self.oks)}", end="")
        except: pass

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiUltra().menu()
