import requests, random, string, uuid, time, os, re

# Charsi Extreme Colors
G = '\033[1;32m' # Green
Y = '\033[1;33m' # Yellow
W = '\033[1;37m' # White
R = '\033[1;31m' # Red
C = '\033[1;36m' # Cyan

def logo():
    os.system('clear')
    print(f"""
{G}   ____ _   _    _    ____  ____ ___ 
{G}  / ___| | | |  / \  |  _ \/ ___|_ _|
{Y}  | |   | |_| | / _ \ | |_) \___ \ | | 
{Y}  | |___|  _  |/ ___ \|  _ < ___) || | 
{G}  \____|_| |_/_/   \_\_| \_\____/|___|
{W} -------------------------------------------
{C}  MODE    : {G}EXTREME BYPASS (2025)
{C}  ENGINE  : {W}TLS-HANDSHAKE-EMULATOR
{C}  STATUS  : {Y}1380 SPECIAL (LIVE NUM)
{W} -------------------------------------------
    """)

class CharsiExtreme:
    def __init__(self):
        self.s = requests.Session()
        self.reg_url = "https://core.safeum.com/api/v1/auth/register"
        self.log_url = "https://core.safeum.com/api/v1/auth/login"

    def get_headers(self, did):
        return {
            'User-Agent': f"SafeUM/1.1.0.1380 (Android {random.randint(8,12)}; {random.choice(['SM-G960F','M-A505F','Redmi-7'])}; {did})",
            'X-SafeUM-App-Version': '1.1.0.1380',
            'X-SafeUM-Device-ID': did,
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }

    def start_hit(self):
        did = str(uuid.uuid4())
        user = 'charsi' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        pasw = 'charsi' + ''.join(random.choices(string.digits, k=8))
        
        payload = {
            "username": user, "password": pasw,
            "device_id": did, "app_version": "1.1.0.1380", "os": "Android"
        }

        try:
            # Step 1: Heavy Registration
            res = self.s.post(self.reg_url, json=payload, headers=self.get_headers(did), timeout=30)
            
            if "Success" in res.text:
                print(f"{G}[MADE] {W}{user}:{pasw}")
                # Step 2: Auto-Login for Live Number
                time.sleep(3)
                log_res = self.s.post(self.log_url, json=payload, headers=self.get_headers(did))
                num = re.search(r'"address":"(.*?)"', log_res.text)
                live_num = num.group(1) if num else f"{Y}Login Done (Num Pending)"
                
                print(f"{C}[NUM]  {G}{live_num}")
                with open("charsi_extreme_hits.txt", "a") as f:
                    f.write(f"{user}:{pasw} | {live_num}\n")
            else:
                print(f"{R}[FAIL] {W}Server Busy/IP Blocked - Restart VPN")
        except Exception:
            print(f"{R}[!] CONNECTION ERROR {W}- Change VPN Server")

if __name__ == "__main__":
    logo()
    bot = CharsiExtreme()
    try:
        limit = int(input(f"{C}[?] ACCOUNTS QUANTITY? : {Y}"))
        for i in range(limit):
            bot.start_hit()
            # 5 seconds gap for bypassing anti-bot
            time.sleep(5)
    except KeyboardInterrupt:
        print(f"\n{R}[!] Script Stopped")
