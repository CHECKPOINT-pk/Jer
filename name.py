#--> Script Owner: Charsi Coder (Elite)
#--> Nasha: Facebook Bashing
#--> Update: 2025 Deep Bypass

import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs

#--> Charsi Colors (Nasheeli Green)
G = "\x1b[38;5;46m"  # Green
D = "\x1b[38;5;28m"  # Dark Green
W = "\x1b[38;5;231m" # White
R = "\x1b[38;5;196m" # Red
Y = "\x1b[38;5;226m" # Yellow

#--> Data Stats
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
    {G}   [#] STAY HIGH • CLONE FAST • EMOJI BYPASS [#]
    {W}   -------------------------------------------""")

class CharsiMaster:
    def __init__(self):
        self.ses = requests.Session()
        if not os.path.exists('Results'): os.mkdir('Results')
        self.main_menu()

    def main_menu(self):
        clear(); charsi_logo()
        print(f"{G}[1] {W}Invalid Emoji Name Changer {D}(Japan/Spain Proxy)")
        print(f"{G}[2] {W}Random Number Cloning     {D}(ID, BD, NG Codes)")
        print(f"{G}[0] {R}Exit Charsi World")
        
        opt = input(f"\n{D}┌─[{G}Charsi-Menu{D}]\n{D}└─{G}> {W}")
        
        if opt == '1': self.emoji_changer()
        elif opt == '2': self.cloning_menu()
        else: sys.exit()

    #--- Section 1: Emoji Name Changer ---
    def emoji_changer(self):
        clear(); charsi_logo()
        print(f"{Y}[!] Connect Japan or Spain VPN First!{W}\n")
