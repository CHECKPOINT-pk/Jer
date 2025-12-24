#--> Script Owner: Charsi Coder (Elite)
#--> Login Mode: Gmail/Password + Cookie Support
#--> Bypass: Invalid/Unique Name (Japan/Spain/IPA)

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
    {G}   [#] GMAIL LOGIN • INVALID NAME • UNIQUE BYPASS [#]
    {W}   -------------------------------------------""".format(D=D, G=G, W=W))

class CharsiMaster:
    def __init__(self):
        self.ses = requests.Session()
        self.ua = "Mozilla/5.0 (Linux; Android 13; Japan) AppleWebKit/537.36"
        if not os.path.exists('Results'): os.mkdir('Results')
        self.main_menu()

    def main_menu(self):
        clear(); charsi_logo()
        print(f"{G}[1] {W}Login with Gmail/Pass & Change Name")
        print(f"{G}[2] {W}Login with Cookie & Change Name")
        print(f"{G}[0] {R}Exit")
        
        opt = input(f"\n{D}┌─[{G}Select Mode{D}]\n{D}└─{G}> {W}")
        if opt == '1': self.login_with_gmail()
        elif opt == '2': self.login_with_cookie()
        else: sys.exit()

    def login_with_gmail(self):
        clear(); charsi_logo()
        email = input(f"{G}[?] Enter Gmail/Number: {W}")
        pasw = input(f"{G}[?] Enter FB Password: {W}")
        
        print(f"{D}[!] Attempting Login...")
        try:
            # Login Logic
            r1 = self.ses.get('https://m.facebook.com/login/', headers={'User-Agent': self.ua})
            data = {
                'lsd': re.search('name="lsd" value="(.*?)"', r1.text).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', r1.text).group(1),
                'email': email, 'pass': pasw, 'login': 'Log In'
            }
            res = self.ses.post('https://m.facebook.com/login/device-based/regular/login/', data=data, headers={'User-Agent': self.ua})
            
            if "c_user" in self.ses.cookies.get_dict():
                print(f"{G}[SUCCESS] Login Ho Gaya Bhai!")
                self.emoji_changer()
            else:
                print(f"{R}[FAILED] Login nahi hua. Gmail/Pass check karo ya Cookie use karo.")
        except Exception as e:
            print(f"{R}[ERROR] Net ka masla hai!")

    def login_with_cookie(self):
        clear(); charsi_logo()
        cookie = input(f"{G}[?] Enter FB Cookie: {W}")
        self.ses.cookies.update({'cookie': cookie})
        self.emoji_changer()

    def emoji_changer(self):
        print(f"\n{Y}[!] Connect Japan/Spain VPN for Invalid/Unique Name!{W}\n")
        first = input(f"{G}[?] First Name: {W}")
        emoji = input(f"{G}[?] Invalid Emojis/Unique (👿🩶々〆): {W}")
        last = input(f"{G}[?] Last Name: {W}")
        
        headers = {
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
                print(f"\n{G}[OK] Invalid Name Accepted! Browser mein ja kar password do.{W}")
            else:
                print(f"\n{R}[FAILED] FB ne Name reject kar diya. VPN badlo!")
        except:
            print(f"{R}[ERROR] Session expired!")
        
        input(f"\n{G}Press Enter to return..."); self.main_menu()

if __name__ == "__main__":
    CharsiMaster()
