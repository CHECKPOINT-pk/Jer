#--> Script: VORTEX-PRO (Final Working)
#--> Function: Cookie Refresher + EAAG Token
#--> Fix: 2025 Handshake Bypass

import requests, re, os, time, random

#--> Charsi Colors
G = "\x1b[38;5;46m" 
C = "\x1b[38;5;51m"
W = "\x1b[38;5;231m"
R = "\x1b[38;5;196m"

def clear():
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

class VortexPro:
    def __init__(self):
        self.ses = requests.Session()
        # High-Trust User Agent
        self.ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Mobile/15E148 Safari/604.1"
        self.main()

    def main(self):
        clear()
        print(f"{C}--- VORTEX PRO: COOKIE & TOKEN SYSTEM ---{W}")
        print(f"{G}[!] Step: Paste full cookies from Via Browser{W}")
        cookie = input(f"{G}[?] Cookie: {W}")
        
        if "c_user=" not in cookie or "xs=" not in cookie:
            print(f"{R}[!] Error: Incomplete Cookie. XS and C_USER are required.{W}")
            return

        print(f"\n{C}[*] Extracting EAAG Token & Refreshing Session...{W}")
        
        # Headers specifically for Business Manager Bypass
        headers = {
            'authority': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'user-agent': self.ua,
        }

        try:
            # Most stable endpoint for EAAG Token in 2025
            response = self.ses.get('https://business.facebook.com/business_locations', headers=headers, timeout=20).text
            token = re.search('(EAAG\w+)', response)
            
            if token:
                print(f"\n{G}[SUCCESS] ID Refresh Ho Gayi!{W}")
                print(f"{C}-------------------------------------------{W}")
                print(f"{G}NEW TOKEN: {W}{token.group(1)}")
                print(f"{C}-------------------------------------------{W}")
                print(f"{G}STABLE COOKIE: {W}{cookie}")
                
                # Saving to file
                uid = re.search('c_user=(\d+)', cookie).group(1)
                with open(f'Active_{uid}.txt', 'w') as f:
                    f.write(f"TOKEN: {token.group(1)}\nCOOKIE: {cookie}")
                print(f"\n{G}[!] Saved as Active_{uid}.txt{W}")
            else:
                print(f"{R}[!] Token Extraction Failed!{W}")
                print(f"{Y}[Note] ID par 2FA off karein aur Japan VPN use karein.{W}")

        except Exception as e:
            print(f"{R}[ERROR] Request Blocked: {e}{W}")

if __name__ == "__main__":
    VortexPro()
