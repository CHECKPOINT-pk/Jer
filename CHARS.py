import requests, random, string, uuid, time, os

# Charsi 1380 Theme Colors
G = '\033[1;32m' # Green
Y = '\033[1;33m' # Yellow
W = '\033[1;37m' # White
R = '\033[1;31m' # Red
C = '\033[1;36m' # Cyan

def logo_1380():
    os.system('clear')
    print(f"""
{G}   ____ _   _    _    ____  ____ ___ 
{G}  / ___| | | |  / \  |  _ \/ ___|_ _|
{Y}  | |   | |_| | / _ \ | |_) \___ \ | | 
{Y}  | |___|  _  |/ ___ \|  _ < ___) || | 
{G}  \____|_| |_/_/   \_\_| \_\____/|___|
{W} -------------------------------------------
{C}  TARGET  : {G}SAFEUM v1.1.0.1380
{C}  METHOD  : {W}API-V1-INJECTION
{C}  STATUS  : {Y}STABLE & RUNNING
{W} -------------------------------------------
    """)

class Charsi1380:
    def __init__(self):
        self.url = "https://core.safeum.com/api/v1/auth/register"
        # 1380 specific session handling
        self.session = requests.Session()

    def get_1380_headers(self, dev_id):
        return {
            'User-Agent': f"SafeUM/1.1.0.1380 (Android 11; SM-A515F; {dev_id})",
            'X-SafeUM-App-Version': '1.1.0.1380',
            'X-SafeUM-Device-ID': dev_id,
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }

    def start_making(self):
        # Unique ID per registration
        dev_id = str(uuid.uuid4())
        user = 'charsi' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        pasw = 'charsi' + ''.join(random.choices(string.digits, k=8))
        
        payload = {
            "username": user,
            "password": pasw,
            "device_id": dev_id,
            "app_version": "1.1.0.1380",
            "os": "Android",
            "language": "en_US"
        }

        try:
            # 1380 API response is faster, so timeout is 15s
            res = self.session.post(self.url, json=payload, headers=self.get_1380_headers(dev_id), timeout=15)
            
            if res.status_code == 200:
                if "Success" in res.text:
                    print(f"{G}[SUCCESS-1380] {W}{user}:{pasw}")
                    with open("charsi_1380_hits.txt", "a") as f:
                        f.write(f"{user}:{pasw}\n")
                elif "AlreadyExists" in res.text:
                    print(f"{R}[!] {W}User Taken, changing name...")
                    self.start_making()
                else:
                    print(f"{R}[FAILED] {W}IP Blocked or Proxy Dead!")
            else:
                print(f"{R}[ERROR] {W}Server Busy (Code: {res.status_code})")
                
        except Exception:
            print(f"{R}[!] CONNECTION ERROR {W}- VPN Check Karein!")

if __name__ == "__main__":
    logo_1380()
    bot = Charsi1380()
    try:
        limit = int(input(f"{C}[?] {W}KITNE ACCOUNTS? : {Y}"))
        print(f"{W}-------------------------------------------")
        for i in range(limit):
            bot.start_making()
            # 1380 server needs 3-4 sec gap to avoid 'Too many attempts'
            time.sleep(3.5)
        print(f"{W}-------------------------------------------")
        print(f"{G}[+] HITS SAVED: charsi_1380_hits.txt")
    except KeyboardInterrupt:
        print(f"\n{R}[!] Stopped!")
