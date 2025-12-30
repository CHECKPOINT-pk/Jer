# -*- coding: utf-8 -*-
import os, sys, re, time, random, string, json
import requests
from concurrent.futures import ThreadPoolExecutor as tred

# --- COLORS (CHARSI THEME) ---
G = '\033[1;32m' # Green
W = '\033[1;37m' # White
R = '\033[1;31m' # Red
Y = '\033[1;33m' # Yellow

def clear():
    os.system('clear')

def linex():
    print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}')

def banner():
    clear()
    print(f"""{G}
     ___ _   _  ____ _____  _      ____ ____  
    |_ _| \ | |/ ___|_   _|/ \    |  _ \  _ \ 
     | ||  \| | \___ \ | | / _ \   | |_) | |_) |
     | || |\  |  ___) || |/ ___ \  |  __/|  _ < 
    |___|_| \_| |____/ |_/_/   \_\ |_|   |_| \_\\
    {Y}========================================
    {R}[+]{W} TOOL    : {G}INSTA VERIFIED CREATOR
    {R}[+]{W} ACCESS  : {G}FULL ACCESS (NO KEY)
    {R}[+]{W} STATUS  : {G}VERIFIED ACCOUNTS
    {Y}========================================{W}""")

# --- PRO USER AGENTS ---
def get_ua():
    ver = random.randint(400, 450)
    android_v = random.choice(['12','13','14'])
    model = random.choice(['SM-S928B','SM-G998B','Pixel 8 Pro'])
    return f"Instagram {ver}.0.0.{random.randint(10,99)} Android ({android_v}; 480dpi; 1080x2214; samsung; {model}; e3q; qcom; en_US; {random.randint(500000000,600000000)})"

class InstaPro:
    def __init__(self):
        self.session = requests.Session()
        self.oks = []

    def register(self):
        try:
            # 1. Random Data
            user = "pro_" + ''.join(random.choices(string.ascii_lowercase, k=5)) + str(random.randint(10,99))
            pw = "Verify@" + ''.join(random.choices(string.digits, k=5))
            
            # Note: For real verification, use a Temp-Mail API here
            email = user + "@1secmail.com" 
            
            headers = {
                'User-Agent': get_ua(),
                'X-IG-App-ID': '1217981644879628',
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            # 2. Check Username
            check = self.session.post("https://i.instagram.com/api/v1/users/check_username/", 
                                    data={'username': user}, headers=headers).json()

            if check.get('available'):
                print(f" {G}[+] Creating: {user} | {pw}")
                
                # 3. Request OTP (Verification)
                # Yahan Instagram verification code bhejega
                print(f" {Y}[!] Verification Code Sent to: {email}")
                
                # Manual OTP entry for Full Control
                otp = input(f" {W}Enter 6-digit OTP from {email}: ")

                if otp:
                    reg_data = {
                        'email': email,
                        'username': user,
                        'password': pw,
                        'verification_code': otp,
                        'first_name': 'Verified User',
                        'force_sign_up_code': '',
                    }
                    
                    # 4. Final Signup
                    resp = self.session.post("https://i.instagram.com/api/v1/accounts/process_contact_point_signup_code/", 
                                           data=reg_data, headers=headers).json()

                    if 'account_created' in str(resp):
                        print(f" {G}[SUCCESS] Verified Account Created!")
                        print(f" {G}[>] {user}:{pw}")
                        with open('verified_insta.txt', 'a') as f:
                            f.write(f"{user}|{pw}|{email}\n")
                        self.oks.append(user)
                    else:
                        print(f" {R}[-] Registration Failed: {resp.get('message', 'Unknown Error')}")
            else:
                print(f" {R}[-] Username taken, skipping...")

        except Exception as e:
            print(f" {R}[!] Connection Error: {e}")

# --- MAIN ---
if __name__ == "__main__":
    banner()
    print(f" {G}(1) Start Unlimited Verified Cloning")
    print(f" {G}(0) Exit")
    linex()
    ch = input(f" {G}Choice: {W}")
    
    if ch == '1':
        num = int(input(f" {G}How many accounts: {W}"))
        bot = InstaPro()
        # Multi-threading for speed
        with tred(max_workers=5) as pool:
            for _ in range(num):
                pool.submit(bot.register)
        
        linex()
        print(f" {G}Process Finished. Accounts saved in verified_insta.txt")
    else:
        sys.exit()
