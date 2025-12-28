import cloudscraper, random, string, uuid, time, os, re

# Charsi Pro Colors
G, Y, W, R, B = '\033[1;32m', '\033[1;33m', '\033[1;37m', '\033[1;31m', '\033[1;34m'

def pro_logo():
    os.system('clear')
    print(f"{B}PRO-MODE {G}LIVE {W}- {Y}KAZAKHSTAN SPECIAL")
    print(f"{W}-------------------------------------------")

class KazakhstanBypass:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper(browser={'browser': 'chrome','platform': 'android','desktop': False})
        self.h = {
            'X-SafeUM-App-Version': '1.1.0.1380',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive'
        }

    def make(self):
        u = 'charsi' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        p = 'charsi' + ''.join(random.choices(string.digits, k=8))
        did = str(uuid.uuid4())
        
        data = {"username": u, "password": p, "device_id": did, "app_version": "1.1.0.1380", "os": "Android"}

        try:
            # Registration
            res = self.scraper.post("https://core.safeum.com/api/v1/auth/register", json=data, headers=self.h, timeout=30)
            if "Success" in res.text:
                print(f"{G}[KAZAKH-HIT] {W}{u}:{p}")
                time.sleep(4)
                # Login Check
                log = self.scraper.post("https://core.safeum.com/api/v1/auth/login", json=data, headers=self.h)
                num = re.search(r'"address":"(.*?)"', log.text)
                print(f"{B}[NUMBER] {G}{num.group(1) if num else 'Wait 5 Min'}")
                with open("kazakh_hits.txt", "a") as f: f.write(f"{u}:{p}\n")
            else:
                print(f"{R}[BLOCKED] {W}Server busy - Change Kazakhstan City")
        except:
            print(f"{R}[!] Connection Error - Restart VPN")

if __name__ == "__main__":
    pro_logo()
    bot = KazakhstanBypass()
    limit = int(input(f"{B}[?] Accounts? : {Y}"))
    for _ in range(limit):
        bot.make()
        time.sleep(7) # Safe delay for Kazakhstan IP
