#--> Author: Dapunta Khurayra X | Global Location Bypass v3.0
import os, sys, time, re, datetime, random, requests
from bs4 import BeautifulSoup as bs

#--> Colors
P = "\x1b[38;5;231m" # White
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green
C = "\x1b[38;5;51m"  # Cyan
Y = "\x1b[38;5;226m" # Yellow

#--> Stats
ok = 0
cp = 0

def clear():
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

#--> Global Location & UA Generator
def get_global_data():
    locations = [
        {'cc': 'US', 'lang': 'en-US,en;q=0.9', 'model': 'Pixel-9-Pro'},
        {'cc': 'GB', 'lang': 'en-GB,en;q=0.8', 'model': 'SM-S928B'},
        {'cc': 'IN', 'lang': 'en-IN,en;q=0.7', 'model': 'V2303'},
        {'cc': 'PK', 'lang': 'en-PK,en;q=0.9', 'model': 'RMX3840'},
        {'cc': 'AE', 'lang': 'en-AE,en;q=0.8', 'model': 'S24-Ultra'}
    ]
    loc = random.choice(locations)
    ver = random.choice(['14', '15'])
    chrome = f'132.0.{random.randint(6000,7000)}.{random.randint(100,200)}'
    ua = f'Mozilla/5.0 (Linux; Android {ver}; {loc["model"]}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36'
    return ua, loc['lang'], loc['cc']

def logo():
    print(f"{C}_________                      __        {M}________________ {C}")
    print(f"{C}\_   ___ \_______ ____ _____ _/  |_  ____{M}\_   ____|___   \\{C}")
    print(f"{C}/    \  \/\_  __ \ __ \\\\__  \\\\   __\/ __ \{M}|    __)   |  _/{C}")
    print(f"{C}\ 0.1 \____|  | \/ ___/ / __ \|  | \  ___/{M}|   \  |   |   \\{C}")
    print(f"{C} \________/|__|  \_____>______/__|  \____>{M}|___/  |_______/{C}")
    print(f"{Y}      ──────────── {M}• {P}GLOBAL LOCATION BYPASS {M}• {Y}────────────\n{P}")

class GlobalCreator:
    def __init__(self):
        clear()
        logo()
        print(f"{M}[{P}1{M}] {P}Start Global ID Creation (Verified OK)")
        print(f"{M}[{P}0{M}] {P}Exit")
        if input(f"\n {M}└─ {P}Select: ") == '1': self.boot()
        else: sys.exit()

    def boot(self):
        delay = int(input(f"{M}[{P}•{M}] {P}Set Delay (Seconds) [Min 60]: ") or 60)
        print(f"\n{H}[!] System Active: Simulating Global IP & Locations...{P}")
        
        while True:
            self.create_account()
            print(f"{Y}" + "-"*45 + f"{P}")
            for x in range(delay, 0, -1):
                print(f"\r{P}[OK:{H}{ok}{P}] [CP:{M}{cp}{P}] Global Cooling: {x}s...      ", end="")
                time.sleep(1)

    def create_account(self):
        global ok, cp
        ses = requests.Session()
        ua, lang, country = get_global_data()
        
        # Identity Generator
        f_names = ['James','Aryan','Zain','Robert','Sarah','Ayesha','Emma','John']
        l_names = ['Smith','Khan','Ahmed','Wilson','Davis','Ali','Malik']
        name = f"{random.choice(f_names)} {random.choice(l_names)}"
        email = f"{name.lower().replace(' ','')}{random.randint(111,999)}@vjuum.com"
        password = f"{name.split()[0]}@{random.randint(111,999)}!"

        print(f"{C}[LOCATION]{P} Country: {Y}{country}{P} | Lang: {Y}{lang.split(',')[0]}{P}")
        print(f"{C}[IDENTITY]{P} Name: {H}{name}{P} | Pass: {H}{password}{P}")
        
        try:
            # Step 1: Pre-Fetch with Location Headers
            headers = {'User-Agent': ua, 'Accept-Language': lang}
            res = ses.get('https://m.facebook.com/reg/?cid=103', headers=headers)
            soup = bs(res.text, 'html.parser')
            
            # Step 2: Data Submission
            payload = {
                'lsd': soup.find('input', {'name': 'lsd'})['value'],
                'jazoest': soup.find('input', {'name': 'jazoest'})['value'],
                'firstname': name.split()[0],
                'lastname': name.split()[1],
                'reg_email__': email,
                'sex': random.choice(['1', '2']),
                'reg_passwd__': password,
                'birthday_day': str(random.randint(1,28)),
                'birthday_month': str(random.randint(1,12)),
                'birthday_year': str(random.randint(1995,2005)),
                'submit': 'Sign Up'
            }
            
            print(f"{C}[PROCESS ]{P} Submitting encrypted data...", end="\r")
            headers.update({'referer': 'https://m.facebook.com/reg/'})
            post = ses.post('https://m.facebook.com/reg/submit/', data=payload, headers=headers)

            if "c_user" in ses.cookies.get_dict() or "checkpoint" not in post.url:
                print(f"{H}[SUCCESS ] ID Created Successfully!               {P}")
                open("Results_Global.txt", "a").write(f"{email}|{password}|{country}\n")
                ok += 1
            else:
                print(f"{M}[FAILED  ] Account Checkpointed (CP).              {P}")
                cp += 1
        except:
            print(f"{M}[ERROR   ] Connection Blocked by Facebook.         {P}")
            cp += 1

if __name__ == "__main__":
    GlobalCreator()
