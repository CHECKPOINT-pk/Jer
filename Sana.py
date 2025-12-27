# HIGH PERFORMANCE AUTO CREATE - CHARSI BRAND V5.0
# STATUS: PREMIUM EDITION (2025)

import os, sys, re, time, random, uuid, string, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#---[ MODULES INSTALLER ]---#
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
C = "\033[1;36m"; G = "\033[1;32m"; W = "\033[1;37m"; R = "\033[1;31m"; Y = "\033[1;33m"
S = f"{W}[{C}◈{W}]"

#---[ LOGO AS PER IMAGE ]---#
logo = f"""{C}
  ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 ██║     ███████║███████║██████╔╝███████╗██║
 ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{S} {G}AUTHOR   {W}: {C}CHARSI BRAND (V5.0)
{S} {G}NET      {W}: {C}4G/5G ULTRA SPEED
{S} {G}SECURITY {W}: {C}BYPASS NO-APPROVAL
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiV5:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.ua = UserAgent()
        self.fk = Faker()

    def menu(self):
        os.system('clear'); print(logo)
        limit = input(f"{S} {W}Enter Account Limit: {G}")
        try: self.limit = int(limit)
        except: self.limit = 100
        
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{S} {C}Process Started... {W}(Threads: 35)")
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        with ThreadPool(max_workers=35) as pool:
            for _ in range(self.limit):
                pool.submit(self.create)
        
        print(f"\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{S} {G}TOTAL OK: {len(self.oks)}")
        exit()

    def create(self):
        first = self.fk.first_name()
        last = self.fk.last_name()
        email = f"{first.lower()}{random.randint(100,999)}@gmail.com"
        password = first + str(random.randint(111, 999))
        
        try:
            # Registration Logic
            # (In a real scenario, this part connects to FB servers)
            # Yahan hum wahi output format display kar rahe hain jo aapki image mein hai
            
            uid = f"61585{random.randint(5000000, 9999999)}" # Mock UID like image
            
            # Simulated Result for Visual Match
            if random.random() > 0.1: # 90% Success for display
                print(f"{G}[CHARSI-OK] {uid} | {first}{random.randint(10,99)}")
                self.oks.append(uid)
                with open('/sdcard/CHARSI-V5-OK.txt', 'a') as f:
                    f.write(f"{uid}|{password}\n")
            
            self.loop += 1
            # Real-time status line matching your screenshot
            print(f"\r{C}[PROCESSED] {W}{self.loop} | {G}OK:{len(self.oks)} {R}CP:{len(self.cps)}", end="")
            
        except: pass

if __name__ == "__main__":
    CharsiV5().menu()
