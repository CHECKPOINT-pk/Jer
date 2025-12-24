#--> Script: VORTEX-7 (The Cookie King)
#--> Owner: Charsi Coder (Elite)
#--> Power: Real-Time Handshake • No CP • EAAG Heavy Token

import os, sys, time, re, random, requests, json
from bs4 import BeautifulSoup as bs

#--> Charsi Color Palette
G = "\x1b[38;5;46m"  # Neon Green
D = "\x1b[38;5;28m"  # Deep Forest
W = "\x1b[38;5;231m" # Snow White
R = "\x1b[38;5;196m" # Blood Red
Y = "\x1b[38;5;226m" # Gold Yellow
C = "\x1b[38;5;51m"  # Cyan

def clear():
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

def charsi_logo():
    print(r"""{D}
      _______  _    _  _______  ______   _______  _________
     (_______)(_)  (_)(_______)(_____ \ (_______)(_________)
      _        _    _  _______  _____) ) _           _    
     | |      | |__| ||  ___  ||  __  / | |         | |   
     | |_____ |  __  || |   | || |  \ \ | |_____   _| |_  
      \______)(_)  (_)(_)   (_)(_)   (_)(_______) (_____)
    {G}   [#] VORTEX-7 • HEAVY SECURITY BYPASS • NO CP [#]
    {W}   -------------------------------------------""".format(D=D, G=G, W=W))

class Vortex7:
    def __init__(self):
        self.ses = requests.Session()
        # Using 2025 High-Tier Device UA
        self.ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1"
        if not os.path.exists('Active_Sessions'): os.mkdir('Active_Sessions')
        self.main_menu()

    def main_menu(self):
        clear(); charsi_logo()
        print(f"{C}[1] {W}Extract Heavy Cookies & Token {G}(Safe Mode)")
        print(f"{C}[2] {W}Auto-Protect Account {G}(Guard + Bio + Follow)")
        print(f"{C}[0] {R}Shutdown System")
        
        opt = input(f"\n{D}┌─[{G}Vortex-Choice{D}]\n{D}└─{G}> {W}")
        if opt == '1': self.secure_login()
        elif opt == '2': self.protect_id()
        else: sys.exit()

    def secure_login(self):
        clear(); charsi_logo()
        user = input(f"{G}[?] Gmail/Number: {W}")
        pasw = input(f"{G}[?] Password: {W}")
        
        print(f"\n{C}[!] Injecting Anti-Checkpoint Sensors...")
        try:
            # Step 1: Secure Handshake
            self.ses.headers.update({'User-Agent': self.ua})
            login_page = self.ses.get('https://m.facebook.com/login/').text
            
            payload = {
                'lsd': re.search('name="lsd" value="(.*?)"', login_page).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', login_page).group(1),
                'email': user, 'pass': pasw, 'login': 'Log In'
            }
            
            # Step 2: Post with Randomized Delay to mimic human behavior
            time.sleep(random.randint(2, 5))
            res = self.ses.post('https://m.facebook.com/login/device-based/regular/login/', data=payload)
            
            if "c_user" in self.ses.cookies.get_dict():
                # Extract Cookies
                cookies = "; ".join([f"{k}={v}" for k, v in self.ses.cookies.get_dict().items()])
                uid = self.ses.cookies.get_dict()['c_user']
                
                print(f"{G}[SUCCESS] ID Logged In! UID: {uid}")
                
                # Step 3: Extracting Permanent Business Token (EAAG)
                print(f"{C}[!] Extracting Heavy EAAG Token...")
                token_res = self.ses.get('https://business.facebook.com/business_locations').text
                token = re.search('(EAAG\w+)', token_res)
                final_token = token.group(1) if token else "Token Not Found"
                
                # Saving to Active_Sessions
                data = {"UID": uid, "COOKIE": cookies, "TOKEN": final_token}
                with open(f'Active_Sessions/{uid}.json', 'w') as f:
                    json.dump(data, f, indent=4)
                
                print(f"\n{G}[+] DATA SAVED! Check 'Active_Sessions' folder.{W}")
                print(f"{G}[+] TOKEN: {W}{final_token[:30]}...")
            
            elif "checkpoint" in res.url:
                print(f"{R}[!] SECURITY BLOCK! Use Japan VPN & try again.{W}")
            else:
                print(f"{R}[!] Login Failed! Check Credentials.{W}")
                
        except Exception as e:
            print(f"{R}[ERROR] System Failure: {e}{W}")
        
        input(f"\n{C}Press Enter to go back..."); self.main_menu()

    def protect_id(self):
        # Auto Guard & Bio Logic
        print(f"{Y}[!] Account protection system coming in next patch!{W}")
        time.sleep(2); self.main_menu()

if __name__ == "__main__":
    Vortex7()
