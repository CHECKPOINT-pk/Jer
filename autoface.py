# HIGH PERFORMANCE AUTO CREATE - INDONESIA EDITION (V5.0)
# AUTHOR : CHARSI BRAND
# REGION : INDONESIA (ID)

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

#---[ COLORS & STYLE ]---#
C = "\033[1;36m"; G = "\033[1;32m"; W = "\033[1;37m"; R = "\033[1;31m"; Y = "\033[1;33m"; P = "\033[1;35m"
S = f"{W}[{C}◈{W}]"

#---[ INDONESIA DATA ]---#
# Faker ko Indonesia (id_ID) par set kiya hai
fk = Faker('id_ID')
SG_API = "https://www.1secmail.com/api/v1/action"
ID_CITIES = ["Jakarta", "Surabaya", "Bandung", "Medan", "Semarang", "Makassar"]
ID_BIOS = ["Sabar itu indah", "Mencari berkah", "Wong Jowo", "Anak Jakarta", "Stay Humble"]

logo = f"""{C}
  ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 ██║     ███████║███████║██████╔╝███████╗██║
 ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{S} {G}AUTHOR   {W}: {C}CHARSI BRAND (V5.0)
{S} {G}REGION   {W}: {C}INDONESIA (ID)
{S} {G}SECURITY {W}: {C}BYPASS NO-APPROVAL
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiID:
    def __init__(self):
        self.oks = []
        self.loop = 0
        self.ua = UserAgent()

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
        limit = input(f"{S} {W}Enter Account Limit: {G}")
        try: self.limit = int(limit)
        except: self.limit = 100
        
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{S} {C}Indonesia Server Active... {W}(Threads: 35)")
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        with ThreadPool(max_workers=35) as pool:
            for _ in range(self.limit):
                pool.submit(self.engine)
        
        print(f"\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{S} {G}TOTAL INDO OK: {len(self.oks)}")
        input(f"\n{C}Back To Menu...")
        self.menu()

    def engine(self):
        # Indonesia Name Generation
        first = fk.first_name()
        last = fk.last_name()
        email = self.get_mail()
        password = first + str(random.randint(111, 999))
        
        try:
            ses = requests.Session()
            h = {'User-Agent': self.ua.random}
            
            # Step 1: Create
            res = ses.get('https://m.facebook.com/reg/', headers=h).text
            soup = BeautifulSoup(res, 'html.parser')
            data = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            data.update({
                'firstname': first, 'lastname': last, 'reg_email__': email,
                'reg_passwd__': password, 'sex': '2',
                'birthday_day': str(random.randint(1,28)), 
                'birthday_month': str(random.randint(1,12)), 
                'birthday_year': str(random.randint(1992,2004))
            })
            reg = ses.post('https://m.facebook.com/reg/submit/', data=data, headers=h)

            # Step 2: Real-time Verify
            if 'confirm_code' in reg.text or 'checkpoint' in reg.url:
                otp = self.get_otp(email)
                if otp:
                    ses.post('https://m.facebook.com/confirmemail.php', data={'c': otp, 'submit': 'Confirm'}, headers=h)
                    
                    if 'c_user' in ses.cookies.get_dict():
                        uid = ses.cookies.get_dict()['c_user']
                        ck = ";".join([f"{k}={v}" for k, v in ses.cookies.get_dict().items()])
                        
                        # Real-time Display like V5.0
                        print(f"\n{G}[CHARSI-OK] {uid} | {password} | Verified")
                        print(f"{C}[INFO] Name: {first} {last} | City: {random.choice(ID_CITIES)}")
                        
                        self.oks.append(uid)
                        with open('/sdcard/CHARSI-INDO.txt', 'a') as f:
                            f.write(f"{uid}|{password}|{email}|{ck}\n")
            
            self.loop += 1
            print(f"\r{C}[PROCESSED] {W}{self.loop} | {G}OK:{len(self.oks)}", end="")
            
        except: pass

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiID().menu()
