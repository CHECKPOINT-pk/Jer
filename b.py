#--> Script: VORTEX-EXTRACTOR (2025)
#--> Function: Cookie Refresher + EAAG Token Grabber
#--> Safety: Anti-CP Human Handshake

import requests, re, os, time, json

#--> Charsi Colors
G = "\x1b[38;5;46m"  # Green
C = "\x1b[38;5;51m"  # Cyan
W = "\x1b[38;5;231m" # White
R = "\x1b[38;5;196m" # Red
Y = "\x1b[38;5;226m" # Yellow

def clear():
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

def charsi_logo():
    print(rf"""{C}
      _______  _    _  _______  ______   _______  _________
     (_______)(_)  (_)(_______)(_____ \ (_______)(_________)
      _        _    _  _______  _____) ) _           _    
     | |      | |__| ||  ___  ||  __  / | |         | |   
     | |_____ |  __  || |   | || |  \ \ | |_____   _| |_  
      \______)(_)  (_)(_)   (_)(_)   (_)(_______) (_____)
    {G}   [#] HEAVY COOKIE REFRESHER • TOKEN GENERATOR [#]
    {W}   -------------------------------------------""")

class VortexExtractor:
    def __init__(self):
        self.ses = requests.Session()
        # High-Trust UA (iPhone 16 Pro)
        self.ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1"
        if not os.path.exists('Extracted_Data'): os.mkdir('Extracted_Data')
        self.main()

    def main(self):
        clear(); charsi_logo()
        print(f"{C}[!] Enter Via Browser Cookies To Generate New Ones{W}")
        old_cookie = input(f"{G}[?] Paste Cookie: {W}")
        
        print(f"\n{C}[*] Handshaking with FB Business Servers...")
        head = {'cookie': old_cookie, 'user-agent': self.ua}
        
        try:
            # Step 1: Validating Session & Extracting EAAG Token
            # Business Manager se request karne par cookies refresh ho jati hain
            res = self.ses.get('https://business.facebook.com/business_locations', headers=head).text
            token = re.search('(EAAG\w+)', res)
            
            if token:
                # Step 2: Extracting the New Fresh Cookie Set
                new_cookie_dict = self.ses.cookies.get_dict()
                # Adding essential IDs from old cookie if missing
                new_cookie = "; ".join([f"{k}={v}" for k, v in new_cookie_dict.items()])
                if "c_user" not in new_cookie:
                    new_cookie = old_cookie # Fallback if session didn't update
                
                uid = re.search('c_user=(\d+)', new_cookie).group(1)
                final_token = token.group(1)

                print(f"\n{G}[SUCCESS] Data Extracted Successfully!{W}")
                print(f"{G}[UID]   : {W}{uid}")
                print(f"{G}[TOKEN] : {W}{final_token[:40]}...")
                print(f"{G}[COOKIE]: {W}{new_cookie[:60]}...")

                # Saving for universal use
                save_path = f"Extracted_Data/{uid}.txt"
                with open(save_path, 'w') as f:
                    f.write(f"--- VORTEX EXTRACTED DATA ---\n")
                    f.write(f"UID: {uid}\n")
                    f.write(f"TOKEN: {final_token}\n")
                    f.write(f"COOKIE: {new_cookie}\n")
                
                print(f"\n{C}[!] Full Data Saved in {save_path}{W}")
            else:
                print(f"{R}[!] Error: Cookie Expire hai ya Token nahi mil raha.{W}")
                print(f"{Y}[Tip] Browser mein login karke nayi cookie uthayein.{W}")

        except Exception as e:
            print(f"{R}[ERROR] System Failure: {e}{W}")
        
        input(f"\n{G}Press Enter to Exit..."); exit()

if __name__ == "__main__":
    VortexExtractor()
