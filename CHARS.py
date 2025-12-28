import requests, random, string, uuid, time, os

# Colors for Charsi Theme
green = '\033[1;32m'
yellow = '\033[1;33m'
white = '\033[1;37m'
red = '\033[1;31m'
reset = '\033[0m'

def logo():
    os.system('clear')
    print(f"""
{green}  ____ _   _    _    ____  ____ ___ 
{green} / ___| | | |  / \  |  _ \/ ___|_ _|
{yellow} | |   | |_| | / _ \ | |_) \___ \ | | 
{yellow} | |___|  _  |/ ___ \|  _ < ___) || | 
{green}  \____|_| |_/_/   \_\_| \_\____/|___|
{white} -------------------------------------------
{yellow}  OWNER    :  CHARSI BABA (PROXY UPDATED)
{yellow}  LOCATION :  LATVIA / AZERBAIJAN / POLAND
{yellow}  VERSION  :  2025.V2 (BETA)
{white} -------------------------------------------
    """)

# Updated 2025 User-Agent
def get_ua():
    win = random.choice(['10.0', '11.0'])
    ver = random.randint(131, 135)
    build = random.randint(6700, 6900)
    letter1 = random.choice(string.ascii_uppercase)
    num = random.randint(10, 99)
    letter2 = random.choice(string.ascii_uppercase)
    return f"Mozilla/5.0 (Windows NT {win}; Win64; x64){letter1}{num}{letter2} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.{build}.150 Safari/537.36"

def create_acc(proxy_url):
    user = 'charsi' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    pasw = 'charsi' + ''.join(random.choices(string.digits, k=8))
    dev_id = str(uuid.uuid4())
    
    url = "https://core.safeum.com/api/v1/auth/register"
    headers = {'User-Agent': get_ua(), 'Content-Type': 'application/json'}
    data = {
        "username": user, "password": pasw, 
        "device_id": dev_id, "app_version": "1.1.0.1332", "os": "Android"
    }

    # Proxy Configuration
    proxies = {
        'http': proxy_url,
        'https': proxy_url
    }

    try:
        # Request with Proxy
        res = requests.post(url, json=data, headers=headers, proxies=proxies, timeout=15)
        if res.status_code == 200 and "Success" in res.text:
            print(f"{green}[SUCCESS] {white}USER: {yellow}{user} {white}| {green}PROXY: {proxy_url[:20]}...")
            with open("charsi_hits.txt", "a") as f:
                f.write(f"{user}:{pasw}\n")
        else:
            print(f"{red}[FAILED] {white}SERVER BLOCKED PROXY: {red}{proxy_url[:15]}...")
    except:
        print(f"{red}[!] PROXY ERROR - DEAD OR SLOW")

if __name__ == "__main__":
    logo()
    print(f"{yellow}[!] Make sure your proxy list has Poland/Latvia/Azerbaijan IPs")
    
    # Proxy list load karein
    # File format: ip:port OR user:pass@ip:port
    if not os.path.exists("proxies.txt"):
        with open("proxies.txt", "w") as f: f.write("ip:port")
        print(f"{red}[!] proxies.txt file bana di gayi hai. Isme proxies dalein.")
    else:
        proxy_list = open("proxies.txt", "r").read().splitlines()
        limit = int(input(f"{green}[?] {white}KITNE ACCOUNTS? : {yellow}"))
        
        for _ in range(limit):
            current_proxy = random.choice(proxy_list)
            create_acc(f"http://{current_proxy}")
            time.sleep(1)
