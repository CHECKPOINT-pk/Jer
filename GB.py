#--> Script Info
Author    = 'Dapunta Khurayra X'
Updated   = 'Gemini AI - Anti-Ban v2.0'

import os, sys, time, re, datetime, random, requests
from bs4 import BeautifulSoup as bs

#--> Colors
P = "\x1b[38;5;231m" # White
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green

#--> High-End User Agents (Android 15)
def latest_ua():
    model = random.choice(['SM-S928B', 'Pixel-9-Pro', 'V2303', 'RMX3840'])
    ver = random.choice(['14', '15'])
    chrome = f'131.0.{random.randint(6000,6900)}.{random.randint(10,150)}'
    return f'Mozilla/5.0 (Linux; Android {ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36'

class AdvancedCreator:
    def __init__(self):
        self.ok = 0
        self.cp = 0
        self.results = "Results_OK.txt"
        self.clear_screen()
        self.show_logo()
        self.start()

    def clear_screen(self):
        os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

    def show_logo(self):
        print(f"{M}   ______      __  __                      ")
        print(f"{P}  / ____/___ _/ /_/ /_  ___  ________      ")
        print(f"{M} / /_  / __ `/ __/ __ \/ _ \/ ___/ _ \     ")
        print(f"{P}/ __/ / /_/ / /_/ / / /  __/ /  /  __/     ")
        print(f"{M}/_/    \__,_/\__/_/ /_/\___/_/   \___/  v2.0")
        print(f"{P}-------------------------------------------")
        print(f"{H}  STABLE ACCOUNT CREATOR - ENGLISH VERSION {P}")
        print(f"-------------------------------------------")

    def start(self):
        print(f"{M}[{P}1{M}] {P}Start Creating 100% OK IDs")
        print(f"{M}[{P}0{M}] {P}Exit")
        choice = input(f" {M}└─ {P}Select: ")
        if choice == '1':
            self.loop()
        else:
            exit()

    def loop(self):
        delay = input(f"{M}[{P}•{M}] {P}Set Delay (Seconds) [Rec: 60]: ")
        delay = int(delay) if delay else 60
        print(f"\n{H}Running Deep-Bypass Logic...{P}\n")
        
        while True:
            self.create_id()
            for x in range(delay, 0, -1):
                print(f"\r{P}[OK:{H}{self.ok}{P}] [CP:{M}{self.cp}{P}] Next ID in {x}s...", end="")
                time.sleep(1)

    def create_id(self):
        ses = requests.Session()
        ua = latest_ua()
        
        # Random Data Generation
        first_names = ['Aryan', 'Zain', 'Arsalan', 'Sana', 'Ayesha', 'Mehak', 'Rohan', 'Kabir']
        last_names = ['Khan', 'Ahmed', 'Malik', 'Sheikh', 'Jatt', 'Ali']
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        email = name.lower().replace(" ","") + str(random.randint(100,999)) + "@telegmail.com"
        password = "Pass" + str(random.randint(1111,9999)) + "!!"
        
        try:
            # Step 1: Get Cookies & Tokens
            reg_url = 'https://m.facebook.com/reg/?cid=103'
            res = ses.get(reg_url, headers={'User-Agent': ua})
            soup = bs(res.text, 'html.parser')
            
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
            
            # Step 2: Post Data with Bypass Headers
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'user-agent': ua,
                'referer': reg_url
            }
            
            post = ses.post('https://m.facebook.com/reg/submit/', data=payload, headers=headers)
            
            if "checkpoint" not in post.url:
                print(f"\n{H}[SUCCESS] ID Created!")
                print(f"{H}INFO: {email} | {password}{P}")
                with open(self.results, "a") as f:
                    f.write(f"{email}|{password}\n")
                self.ok += 1
            else:
                self.cp += 1
        except:
            self.cp += 1

if __name__ == "__main__":
    AdvancedCreator()
