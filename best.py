import os, sys, re, time, random, uuid, string, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#▬▭▬▭▬▭▬▭[AUTO INSTALLER]▬▭▬▭▬▭▬▭#
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

#▬▭▬▭▬▭▬▭[NEON COLORS]▬▭▬▭▬▭▬▭#
cyan = "\033[1;36m"; magenta = "\033[1;35m"; white = "\033[1;37m"
green = "\x1b[38;5;49m"; red = "\x1b[38;5;160m"; reset = "\033[0m"
style = f"{white}[{cyan}★{white}]"

#▬▭▬▭▬▭▬▭[BANNER]▬▭▬▭▬▭▬▭#
logo = f"""{cyan}
  ██████  ██░ ██  ▄▄▄       ██▀███    ██████  ██▓
▒██    ▒  ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▒██    ▒ ▓██▒
░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒░ ▓██▄   ▒██░
  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄    ▒   ██▒▒██░
▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒▒██████▒▒░██████▒
{magenta}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{style} AUTHOR  : {white}CHARSI BRAND
{style} PROXY   : {green}AUTO-ROTATION ON
{style} STATUS  : {cyan}ULTIMATE VERSION (2025)
{magenta}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiBrand:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.ua = UserAgent()
        self.fk = Faker()
        self.proxies = []

    def get_proxies(self):
        """Public sources se fresh proxies fetch karne ke liye"""
        try:
            res = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text
            self.proxies = res.splitlines()
        except:
            self.proxies = []

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{white}[1] Start Bulk Creation {green}(Proxy Mode)")
        print(f"{white}[2] Update Proxy List")
        print(f"{white}[0] Exit")
        opt = input(f"\n{cyan}Select Option: {reset}")
        if opt == '1': 
            self.get_proxies()
            self.start()
        elif opt == '2':
            print(f"{style} Fetching new proxies..."); self.get_proxies()
            print(f"{style} {green}Done!"); time.sleep(1); self.menu()
        else: exit()

    def start(self):
        os.system('clear'); print(logo)
        try:
            limit = int(input(f"{style} {green}ACCOUNT LIMIT: {white}"))
        except: limit = 10
        print(f"{style} {cyan}THREADS ACTIVE | PROXY ROTATING...")
        print(f"{magenta}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        with ThreadPool(max_workers=35) as pool:
            for _ in range(limit):
                pool.submit(self.create)
        
        print(f"\n{magenta}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{style} {green}SUCCESS: {len(self.oks)} | {red}CP: {len(self.cps)}")

    def create(self):
        first = self.fk.first_name()
        last = self.fk.last_name()
        password = first + str(random.randint(111, 999))
        email = f"{first.lower()}{last.lower()}{random.randint(10,999)}@gmail.com"
        
        # Proxy selection
        proxy = {"http": random.choice(self.proxies)} if self.proxies else None
        
        try:
            ses = requests.Session()
            # Request with proxy
            # res = ses.get('https://m.facebook.com/reg/', proxies=proxy, timeout=10)
            
            # Simulated Success (Logic replace karein real API ke liye)
            time.sleep(0.5)
            self.loop += 1
            print(f"\r{white}[RUNNING] {self.loop} {cyan}OK:{len(self.oks)} {magenta}PROXY:{'ACTIVE' if proxy else 'OFF'}", end="")
            
        except:
            pass

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiBrand().menu()
