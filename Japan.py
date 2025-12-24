#--> Script Owner: Charsi Coder (Elite)
#--> Logic: Auto Login -> Extract Cookie/Token -> Auto Name Change
#--> Bypass: Invalid/Unique Emojis (Japan Headers)

import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs

#--> Charsi Colors
G = "\x1b[38;5;46m"  # Green
D = "\x1b[38;5;28m"  # Dark Green
W = "\x1b[38;5;231m" # White
R = "\x1b[38;5;196m" # Red
Y = "\x1b[38;5;226m" # Yellow

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
    {G}   [#] AUTO COOKIE + TOKEN + INVALID NAME BYPASS [#]
    {W}   -------------------------------------------""".format(D=D, G=G, W=W))

class CharsiAutomation:
    def __init__(self):
        self.ses = requests.Session()
        self.ua = "Mozilla/5.0 (Linux; Android 13; Japan) AppleWebKit/537.36"
        self.cookie = None
        self.token = None
        self.main_menu()

    def main_menu(self):
        clear(); charsi_logo()
        print(f"{G}[1] {W}Login with Gmail/Pass (Auto Extract Cookie/Token)")
        print(f"{G}[0] {R}Exit")
        
        opt = input(f"\n{D}┌─[{G}Select{D}]\n{D}└─{G}> {W}")
        if opt == '1': self.auto_login()
        else: sys.exit()

    def auto_login(self):
        clear(); charsi_logo()
        email = input(f"{G}[?] Gmail/Number: {W}")
        pasw = input(f"{G}[?] FB Password: {W}")
        
        print(f"\n{D}[!] Logging in & Extracting Data...")
        try:
            # Step 1: Login to get Cookies
            head = {'User-Agent': self.ua}
            link = self.ses.get('https://m.facebook.com/login/', headers=head).text
            data = {
                'lsd': re.search('name="lsd" value="(.*?)"', link).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', link).group(1),
                'email': email, 'pass': pasw, 'login': 'Log In'
            }
            res = self.ses.post('https://m.facebook.com/login/device-based/regular/login/', data=data, headers=head)
            
            if "c_user" in self.ses.cookies.get_dict():
                # Extracting Real Cookies
                cookie_dict = self.ses.cookies.get_dict()
                self.cookie = "; ".join([f"{k}={v}" for k, v in cookie_dict.items()])
                
                print(f"{G}[SUCCESS] ID Logged In!")
                print(f"{G}[COOKIE] {W}{self.cookie[:50]}...")
                
                # Step 2: Extracting Access Token (EAAG)
                print(f"{D}[!] Extracting Token...")
                token_page = self.ses.get('https://business.facebook.com/business_locations', headers=head).text
                token_find = re.search('(EAAG\w+)', token_page)
                if token_find:
                    self.token = token_find.group(1)
                    print(f"{G}[TOKEN ] {W}{self.token[:20]}...")
                else:
                    print(f"{Y}[!] Token manually nikalna parega, par ID login hai.")
                
                time.sleep(2)
                self.emoji_changer()
            else:
                print(f"{R}[FAILED] Password galat hai ya Checkpoint (CP) aa gaya.")
        except Exception as e:
            print(f"{R}[ERROR] Connection Error!")

    def emoji_changer(self):
        clear(); charsi_logo()
        print(f"{H}ID LOGGED IN: {W}Proceeding to Name Change...")
        print(f"{Y}[!] Use Japan VPN for Emojis: 👿🩶💔々〆{W}\n")
        
        first = input(f"{G}[?] First Name: {W}")
        emoji = input(f"{G}[?] Invalid Emoji/Japan Symbols: {W}")
        last = input(f"{G}[?] Last Name: {W}")
        
        headers = {
            'cookie': self.cookie,
            'user-agent': self.ua,
            'referer': 'https://m.facebook.com/settings/edit_name/'
        }
        
        try:
            res = self.ses.get('https://m.facebook.com/settings/edit_name/', headers=headers).text
            fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', res).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', res).group(1)
            
            payload = {'fb_dtsg': fb_dtsg, 'jazoest': jazoest, 'firstname': first, 'middlename': emoji, 'lastname': last, 'save': 'Review Change'}
            post = self.ses.post('https://m.facebook.com/settings/edit_name/', data=payload, headers=headers).text
            
            if "password" in post.lower() or "review" in post.lower():
                print(f"\n{G}[OK] Name Accepted! Browser mein ja kar password dein.{W}")
            else:
                print(f"\n{R}[FAILED] FB ne emojis reject kar diye.")
        except:
            print(f"{R}[ERROR] Session expired ho gaya!")
        
        input(f"\n{G}Press Enter to return..."); self.main_menu()

if __name__ == "__main__":
    CharsiAutomation()
