import requests, random, string, uuid, time, os, re

# Charsi Colors
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
{C}  VERSION : {Y}1.1.0.1380 (LIVE NUMBER)
{C}  STATUS  : {G}FULL WORKING (AZ/POLAND VPN)
{W} -------------------------------------------
    """)

class SafeUM_Pro:
    def __init__(self):
        self.reg_url = "https://core.safeum.com/api/v1/auth/register"
        self.login_url = "https://core.safeum.com/api/v1/auth/login"
        self.session = requests.Session()

    def get_headers(self, dev_id):
        return {
            'User-Agent': f"SafeUM/1.1.0.1380 (Android 11; SM-A51; {dev_id})",
            'X-SafeUM-App-Version': '1.1.0.1380',
            'X-SafeUM-Device-ID': dev_id,
            'Content-Type': 'application/json',
            'Host': 'core.safeum.com',
            'Connection': 'Keep-Alive'
        }

    def check_number(self, user, pasw, dev_id):
        # Account banlyavar login karun number check karnya sathi
        payload = {
            "username": user, "password": pasw,
            "device_id": dev_id, "app_version": "1.1.0.1380", "os": "Android"
        }
        try:
            res = self.session.post(self.login_url, json=payload, headers=self.get_headers(dev_id))
            if "status" in res.text and "Success" in res.text:
                # Response madhun number extract karne
                num_match = re.search(r'"address":"(.*?)"', res.text)
                if num_match:
                    return num_match.group(1)
            return "Login Success (Number Pending)"
        except:
            return "Check Manually"

    def register(self):
        dev_id = str(uuid.uuid4())
        user = 'charsi' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        pasw = 'charsi' + ''.join(random.choices(string.digits, k=8))
        
        data = {
            "username": user, "password": pasw,
            "device_id": dev_id, "app_version": "1.1.0.1380", "os": "Android"
        }

        try:
            res = self.session.post(self.reg_url, json=data, headers=self.get_headers(dev_id), timeout=25)
            if "Success" in res.text:
                print(f"{G}[SUCCESS] {W}USER: {Y}{user} {W}| PASS: {Y}{pasw}")
                # Live number check suru
                time.sleep(2)
                number = self.check_number(user, pasw, dev_id)
                print(f"{C}[NUMBER]  {G}{number}")
                with open("charsi_live.txt", "a") as f:
                    f.write(f"User: {user} | Pass: {pasw} | Num: {number}\n")
            else:
                print(f"{R}[FAILED] {W}Server Rejected - Change VPN IP")
        except:
            print(f"{R}[!] CONNECTION ERROR - VPN Check Kara!")

if __name__ == "__main__":
    logo()
    bot = SafeUM_Pro()
    limit = int(input(f"{C}[?] KITNE ACCOUNTS? : {Y}"))
    for i in range(limit):
        bot.register()
        time.sleep(4)
    print(f"\n{G}[+] Sagla data 'charsi_live.txt' madhe save aahe!")
