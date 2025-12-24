# HIGH PERFORMANCE AUTO CREATE FB - 2025 PREMIUM VERSION
# AUTHOR : CHARSI BRAND
# GITHUB  : CHARSI-BRAND-708
# STYLE   : NEON PREMIUM EDITION

import os, sys, re, time, random, uuid, string, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#---[ DEPENDENCIES ]---#
def install_modules():
    modules = ['requests', 'bs4', 'faker', 'fake-useragent']
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            print(f"\033[1;37m[\033[1;32m!\033[1;37m] Installing {module}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

install_modules()

import requests
from bs4 import BeautifulSoup
from faker import Faker
from fake_useragent import UserAgent

#---[ COLOR SCHEME ]---#
# Neon & Premium Palette
P = "\033[1;35m" # Purple
G = "\033[1;32m" # Green
C = "\033[1;36m" # Cyan
W = "\033[1;37m" # White
R = "\033[1;31m" # Red
Y = "\033[1;33m" # Yellow
S = f"{W}[{C}◈{W}]" # Bullet Style

#---[ PREMIUM BANNER ]---#
logo = f"""{C}
  ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 ██║     ███████║███████║██████╔╝███████╗██║
 ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{S} {G}AUTHOR   {W}: {C}CHARSI BRAND (V5.0)
{S} {G}NET      {W}: {C}4G/5G ULTRA SPEED
{S} {G}SECURITY {W}: {C}BYPASS NO-APPROVAL
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiBrand:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.ua = UserAgent()
        self.fk = Faker()

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{S} {W}[{G}01{W}] Start Auto Creation {C}(Ultra Speed)")
        print(f"{S} {W}[{G}02{W}] Contact Author")
        print(f"{S} {W}[{R}00{W}] Exit")
        opt = input(f"\n{C}⚡ {W}Select Choice: {G}")
        if opt in ['1', '01']: self.start()
        elif opt in ['2', '02']: os.system('xdg-open https://github.com/CHARSI-BRAND-708')
        else: exit()

    def start(self):
        os.system('clear'); print(logo)
        try:
            limit = int(input(f"{S} {W}Enter Account Limit: {G}"))
        except: limit = 10
        
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{S} {C}Process Started... {W}(Threads: 35)")
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        with ThreadPool(max_workers=35) as pool:
            for _ in range(limit):
                pool.submit(self.create)
        
        print(f"\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{S} {G}COMPLETED SUCCESS: {len(self.oks)}")
        print(f"{S} {R}COMPLETED CHECKPOINT: {len(self.cps)}")
        print(f"{S} {W}Path: /sdcard/CHARSI-OK.txt")
        input(f"\n{C}Press Enter To Back...")
        self.menu()

    def create(self):
        first = self.fk.first_name()
        last = self.fk.last_name()
        password = first + str(random.randint(111, 999))
        birthday = f"{random.randint(1992, 2005)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
        email = f"{first.lower()}{last.lower()}{random.randint(10,999)}@gmail.com"
        
        try:
            ses = requests.Session()
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'referer': 'https://m.facebook.com/reg/',
                'user-agent': self.ua.random,
            }
            
            reg_page = ses.get('https://m.facebook.com/reg/', headers=headers).text
            soup = BeautifulSoup(reg_page, 'html.parser')
            form_data = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            
            payload = {
                **form_data,
                'firstname': first,
                'lastname': last,
                'reg_email__': email,
                'reg_passwd__': password,
                'birthday_day': birthday.split('-')[2],
                'birthday_month': birthday.split('-')[1],
                'birthday_year': birthday.split('-')[0],
                'sex': '2'
            }
            
            response = ses.post('https://m.facebook.com/reg/submit/', data=payload, headers=headers)
            
            if 'c_user' in ses.cookies.get_dict():
                uid = ses.cookies.get_dict()['c_user']
                print(f"\r{G}[CHARSI-OK] {uid} | {password}      ")
                self.oks.append(uid)
                with open("/sdcard/CHARSI-OK.txt", "a") as f:
                    f.write(f"{uid}|{password}\n")
            elif 'checkpoint' in response.url:
                # CP print nahi karwa raha takay screen saaf rahay
                self.cps.append(email)
                with open("/sdcard/CHARSI-CP.txt", "a") as f:
                    f.write(f"{email}|{password}\n")
            
            self.loop += 1
            print(f"\r{W}[{C}PROCESSED{W}] {self.loop} | {G}OK:{len(self.oks)} {R}CP:{len(self.cps)}", end="")
            
        except Exception:
            pass

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): 
        print(f"{S} {Y}Please allow storage permission...")
        os.system('termux-setup-storage')
    CharsiBrand().menu()
