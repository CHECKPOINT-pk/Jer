#--> Script: VORTEX-MAX (Ultimate Edition)
#--> Owner: Charsi Coder (Elite)
#--> Logic: Cookie Refresh + Direct Login + Auto Name Change

import os, sys, time, re, random, requests, json

#--> Charsi Colors
G = "\x1b[38;5;46m"  # Green
C = "\x1b[38;5;51m"  # Cyan
W = "\x1b[38;5;231m" # White
R = "\x1b[38;5;196m" # Red
Y = "\x1b[38;5;226m" # Yellow

def clear():
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

def charsi_logo():
    print(rf"""{G}
      _______  _    _  _______  ______   _______  _________
     (_______)(_)  (_)(_______)(_____ \ (_______)(_________)
      _        _    _  _______  _____) ) _           _    
     | |      | |__| ||  ___  ||  __  / | |         | |   
     | |_____ |  __  || |   | || |  \ \ | |_____   _| |_  
      \______)(_)  (_)(_)   (_)(_)   (_)(_______) (_____)
    {C}   [#] FULL SYSTEM • COOKIE/TOKEN • NAME CHANGE [#]
    {W}   -------------------------------------------""")

class VortexMax:
    def __init__(self):
        self.ses = requests.Session()
        self.ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1"
        self.cookie = None
        self.token = None
        self.main_menu()

    def main_menu(self):
        clear(); charsi_logo()
        print(f"{C}[1] {W}Login via Browser Cookies {G}(Recommended)")
        print(f"{C}[2] {W}Login via Gmail/Pass {Y}(Security Handshake)")
        print(f"{C}[0] {R}Exit")
        
        opt = input(f"\n{G}┌─[Choice]\n└─> {W}")
        if opt == '1': self.cookie_login()
        elif opt == '2': self.direct_login()
        else: sys.exit()

    def cookie_login(self):
        clear(); charsi_logo()
        cookie = input(f"{C}[?] Paste Via Browser Cookies: {W}")
        print(f"\n{G}[*] Validating Session...")
        try:
            head = {'cookie': cookie, 'user-agent': self.ua}
            res = self.ses.get('https://business.facebook.com/business_locations', headers=head).text
            token = re.search('(EAAG\w+)', res)
            
            if token:
                self.cookie = cookie
                self.token = token.group(1)
                print(f"{G}[SUCCESS] Session Active! Token Extracted.")
                self.name_change_menu()
            else:
                print(f"{R}[!] Cookie Expired ya Business Manager block hai.")
        except: print(f"{R}[!] Connection Error.")
        input(f"\n{W}Press Enter..."); self.main_menu()

    def direct_login(self):
        clear(); charsi_logo()
        user = input(f"{G}[?] Gmail/Number: {W}")
        pasw = input(f"{G}[?] Password: {W}")
        print(f"\n{C}[*] Bypassing CP Security...")
        try:
            self.ses.headers.update({'User-Agent': self.ua})
            r1 = self.ses.get('https://m.facebook.com/login/').text
            data = {
                'lsd': re.search('name="lsd" value="(.*?)"', r1).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', r1).group(1),
                'email': user, 'pass': pasw, 'login': 'Log In'
            }
            time.sleep(2)
            res = self.ses.post('https://m.facebook.com/login/device-based/regular/login/', data=data)
            
            if "c_user" in self.ses.cookies.get_dict():
                self.cookie = "; ".join([f"{k}={v}" for k, v in self.ses.cookies.get_dict().items()])
                t_res = self.ses.get('https://business.facebook.com/business_locations').text
                self.token = re.search('(EAAG\w+)', t_res).group(1)
                print(f"{G}[SUCCESS] ID Login! Cookies & Token Generated.")
                self.name_change_menu()
            else: print(f"{R}[!] Login Failed (CP or Wrong Pass).")
        except: print(f"{R}[!] Error.")
        input(f"\n{W}Press Enter..."); self.main_menu()

    def name_change_menu(self):
        clear(); charsi_logo()
        print(f"{G}[!] Logged In Successfully!{W}")
        first = input(f"{C}[?] First Name: {W}")
        emoji = input(f"{C}[?] Invalid Emoji/Symbol: {W}")
        last = input(f"{C}[?] Last Name: {W}")
        
        print(f"\n{Y}[*] Sending Name Change Request...")
        head = {'cookie': self.cookie, 'user-agent': self.ua}
        try:
            r = self.ses.get('https://m.facebook.com/settings/edit_name/', headers=head).text
            fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', r).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', r).group(1)
            
            payload = {
                'fb_dtsg': fb_dtsg, 'jazoest': jazoest,
                'firstname': first, 'middlename': emoji, 'lastname': last,
                'save': 'Review Change'
            }
            post = self.ses.post('https://m.facebook.com/settings/edit_name/', data=payload, headers=head).text
            if "password" in post.lower() or "review" in post.lower():
                print(f"\n{G}[OK] Name Accepted! Browser mein password daal dein.{W}")
            else: print(f"{R}[FAILED] FB rejected the request.")
        except: print(f"{R}[!] Session Error.")
        input(f"\n{W}Press Enter to return..."); self.main_menu()

if __name__ == "__main__":
    VortexMax()
