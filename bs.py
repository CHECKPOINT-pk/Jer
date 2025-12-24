#--> Author: Dapunta Khurayra X | Final Elite Update 2025
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

#--> High Success Location Generator
def get_high_success_data():
    # Priority: Indonesia (ID) and Bangladesh (BD)
    locations = [
        {'cc': 'ID', 'lang': 'id-ID,id;q=0.9', 'model': 'Vivo-V2025'},
        {'cc': 'BD', 'lang': 'bn-BD,bn;q=0.9', 'model': 'Infinix-X688B'},
        {'cc': 'ID', 'lang': 'id-ID,id;q=0.8', 'model': 'SM-A525F'},
        {'cc': 'PK', 'lang': 'en-PK,en;q=0.9', 'model': 'RMX3191'}
    ]
    loc = random.choice(locations)
    ver = random.choice(['11', '12', '13']) # Stable versions for cloning
    chrome = f'122.0.{random.randint(5000,6000)}.{random.randint(100,200)}'
    ua = f'Mozilla/5.0 (Linux; Android {ver}; {loc["model"]}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36'
    return ua, loc['lang'], loc['cc']

def logo():
    print(f"{C}_________                      __        {M}________________ {C}")
    print(f"{C}\_   ___ \_______ ____ _____ _/  |_  ____{M}\_   ____|___   \\{C}")
    print(f"{C}/    \  \/\_  __ \ __ \\\\__  \\\\   __\/ __ \{M}|    __)   |  _/{C}")
    print(f"{C}\ 0.1 \____|  | \/ ___/ / __ \|  | \  ___/{M}|   \  |   |   \\{C}")
    print(f"{C} \________/|__|  \_____>______/__|  \____>{M}|___/  |_______/{C}")
    print(f"{Y}      ──────────── {M}• {P}ELITE ID/BD BYPASS {M}• {Y}────────────\n{P}")

class FinalCreator:
    def __init__(self):
        clear()
        logo()
        print(f"{M}[{P}1{M}] {P}Start Creating High-Success IDs")
        print(f"{M}[{P}0{M}] {P}Exit")
        if input(f"\n {M}└─ {P}Select: ") == '1': self.boot()
        else: sys.exit()

    def boot(self):
        delay = int(input(f"{M}[{P}•{M}] {P}Set Delay (Seconds) [Rec 60]: ") or 60)
        print(f"\n{H}[!] System Active: Target Countries [ID, BD, PK]{P}")
        
        while True:
            self.create_account()
            print(f"{Y}" + "-"*45 + f"{P}")
            for x in range(delay, 0, -1):
                print(f"\r{P}[OK:{H}{ok}{P}] [CP:{M}{cp}{P}] Cooling Down: {x}s...      ", end="")
                time.sleep(1)

    def create_account(self):
        global ok, cp
        ses = requests.Session()
        ua, lang, country = get_high_success_data()
        
        # Identity Logic
        f_names = ['Dwi','Eka','Budi','Santi','Arif','Zul','Nur','Hassan','Ali','Sajid']
        l_names = ['Saputra','Pratama','Sari','Rahma','Khan','Ahmed','Hossain']
        name = f"{random.choice(f_names)} {random.choice(l_names)}"
        email = f"{name.lower().replace(' ','')}{random.randint(1111,9999)}@vjuum.com"
        password = f"{name.split()[0]}{random.randint(11,99)}@#"

        print(f"{C}[STEP-1]{P} Location: {Y}{country}{P} | Device: {Y}{ua.split(';')[2].split(')')[0]}{P}")
        print(f"{C}[STEP-2]{P} ID Data : {H}{email}{P} | {H}{password}{P}")
        
        try:
            headers = {'User-Agent': ua, 'Accept-Language': lang, 'referer': 'https://m.facebook.com/'}
            print(f"{C}[STEP-3]{P} Bypassing FB Security...", end="\r")
            
            # Pre-logging
            res = ses.get('https://m.facebook.com/reg/?cid=103', headers=headers)
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
                'birthday_year': str(random.randint(1995,2004)),
                'submit': 'Sign Up'
            }
            
            post = ses.post('https://m.facebook.com/reg/submit/', data=payload, headers=headers)

            if "c_user" in ses.cookies.get_dict() or "checkpoint" not in post.url:
                print(f"{H}[RESULT]{P} Status: {H}OK-ID CREATED!{P}                    ")
                open("Results_OK.txt", "a").write(f"{email}|{password}|{country}\n")
                ok += 1
            else:
                print(f"{M}[RESULT]{P} Status: {M}Checkpoint (CP){P}                    ")
                cp += 1
        except:
            print(f"{M}[RESULT]{P} Status: {M}Network Error/Blocked{P}                ")
            cp += 1

if __name__ == "__main__":
    FinalCreator()
