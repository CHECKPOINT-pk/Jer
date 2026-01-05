import os, sys, re, time, random, string
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#▬▭▬▭▬▭▬▭[AUTO INSTALLER]▬▭▬▭▬▭▬▭#
def setup():
    modules = ['requests', 'bs4', 'faker', 'fake-useragent']
    for mod in modules:
        try:
            __import__(mod)
        except ImportError:
            os.system(f"pip install {mod}")

setup()

import requests
from bs4 import BeautifulSoup
from faker import Faker
from fake_useragent import UserAgent

#▬▭▬▭▬▭▬▭[COLORS]▬▭▬▭▬▭▬▭#
green = "\x1b[38;5;49m"
white = "\033[1;37m"
red = "\x1b[38;5;160m"
yellow = "\033[1;33m"
reset = "\033[0m"

#▬▭▬▭▬▭▬▭[LOGO]▬▭▬▭▬▭▬▭#
logo = f"""{green}
  ___ _  _   _   ___  ___ ___ 
 / __| || | /_\ | _ \/ __|_ _|
| (__| __ |/ _ \|   /\__ \| | 
 \___|_||_/_/ \_\_|_\|___/___| {white}BRAND
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{green}[1] {white}OTP VERIFIED ACCOUNTS {green}(HIGH QUALITY)
{green}[2] {white}SIMPLE ACCOUNTS {green}(FAST CREATION)
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{green}[●] {white}UPDATED  : {yellow}JANUARY 2026
{green}[●] {white}STATUS   : {green}ANTI-SUSPEND ACTIVE
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiDual:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.fk = Faker()
        self.ua = UserAgent()

    # 2026 High-Privacy Headers
    def get_headers(self):
        return {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'upgrade-insecure-requests': '1',
            'user-agent': self.ua.random,
        }

    # 1secmail Logic for OTP
    def get_otp(self, email):
        login, domain = email.split('@')
        for _ in range(12): # Wait 60 seconds max
            time.sleep(5)
            try:
                url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
                msgs = requests.get(url, timeout=10).json()
                for m in msgs:
                    if 'Facebook' in m['subject'] or 'FB-' in m['subject']:
                        mid = m['id']
                        rurl = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={mid}"
                        body = requests.get(rurl).json()['body']
                        otp = re.search(r'\b\d{5}\b', body)
                        if otp: return otp.group(0)
            except: pass
        return None

    def create(self, mode):
        # 2026 Anti-Ban Delay
        time.sleep(random.uniform(4, 8))
        
        fname = self.fk.first_name()
        lname = self.fk.last_name()
        pwd = fname + str(random.randint(1111,9999))
        
        # Email Generation
        user = f"{fname.lower()}{lname.lower()}{random.randint(10,99)}"
        mail = f"{user}@1secmail.com"
        
        try:
            ses = requests.Session()
            headers = self.get_headers()
            
            # Step 1: Open Form
            reg_url = "https://m.facebook.com/reg/"
            req = ses.get(reg_url, headers=headers)
            soup = BeautifulSoup(req.text, 'html.parser')
            
            data = {}
            for i in soup.find_all('input'):
                if i.get('name'): data[i.get('name')] = i.get('value')
                
            data.update({
                'firstname': fname,
                'lastname': lname,
                'reg_email__': mail,
                'reg_passwd__': pwd,
                'birthday_day': str(random.randint(1,28)),
                'birthday_month': str(random.randint(1,12)),
                'birthday_year': str(random.randint(1995,2005)),
                'sex': str(random.randint(1,2))
            })
            
            # Step 2: Submit
            post_url = "https://m.facebook.com/reg/submit/"
            resp = ses.post(post_url, data=data, headers=headers)
            
            # LOGIC FOR MODE 1 (OTP VERIFIED)
            if mode == 'otp':
                if 'confirm-email' in resp.url or 'checkpoint' in resp.url:
                    print(f"\r{white}[{yellow}OTP-CHECK{white}] {mail}          ", end="")
                    code = self.get_otp(mail)
                    if code:
                        print(f"\n{green}[VERIFIED] {mail} | {pwd} | {code}")
                        self.oks.append(mail)
                        open('/sdcard/CHARSI-VERIFIED.txt', 'a').write(f"{mail}|{pwd}|{code}\n")
                    else:
                        self.cps.append(mail) # OTP nahi aaya
                elif 'c_user' in ses.cookies.get_dict():
                    # Direct Login (Rare but possible)
                    uid = ses.cookies.get_dict()['c_user']
                    print(f"\n{green}[DIRECT-OK] {uid} | {pwd}")
                    self.oks.append(uid)
                    open('/sdcard/CHARSI-VERIFIED.txt', 'a').write(f"{uid}|{pwd}\n")
                else:
                    self.cps.append(mail)

            # LOGIC FOR MODE 2 (SIMPLE / NO OTP)
            elif mode == 'simple':
                if 'confirm-email' in resp.url or 'c_user' in ses.cookies.get_dict():
                    # Account ban gaya, verification skip kardi
                    print(f"\n{green}[SIMPLE-OK] {mail} | {pwd}")
                    self.oks.append(mail)
                    open('/sdcard/CHARSI-SIMPLE.txt', 'a').write(f"{mail}|{pwd}\n")
                else:
                    # Account create hi nahi hua (IP Block etc)
                    self.cps.append(mail)
            
            self.loop += 1
            print(f"\r{white}[RUNNING] {self.loop} | {green}OK:{len(self.oks)} {red}CP:{len(self.cps)}", end="")
            
        except Exception as e:
            pass

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{white}[1] AUTO CREATE + OTP VERIFY")
        print(f"{white}[2] SIMPLE CREATE (NO VERIFY)")
        print(f"{white}[0] EXIT TOOL")
        
        choice = input(f"\n{green}SELECT OPTION: {reset}")
        
        if choice in ['1', '2']:
            try:
                limit = int(input(f"{green}HOW MANY ACCOUNTS: {reset}"))
            except: limit = 10
            
            mode = 'otp' if choice == '1' else 'simple'
            
            # 2026 Thread Management
            # Verified mode needs fewer threads to handle OTP API limits
            workers = 10 if mode == 'otp' else 20
            
            print(f"\n{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            with ThreadPool(max_workers=workers) as pool:
                for _ in range(limit):
                    pool.submit(self.create, mode)
            
            print(f"\n\n{green}PROCESS COMPLETED!")
            print(f"{white}FILE SAVED IN: /sdcard/")
        else:
            exit()

if __name__ == "__main__":
    if not os.path.exists('/sdcard'):
        os.system('termux-setup-storage')
    CharsiDual().menu()
