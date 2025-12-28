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
{yellow}  OWNER    :  CHARSI BABA (UPDATED)
{yellow}  VERSION  :  2025.V1 (BETA)
{yellow}  TOOL     :  SAFEUM UNLIMITED CREATOR
{white} -------------------------------------------
    """)

# 2025 Updated User-Agent
def get_ua():
    win = random.choice(['10.0', '11.0'])
    ver = random.randint(131, 135)
    build = random.randint(6700, 6900)
    # Aapka manga hua format
    letter1 = random.choice(string.ascii_uppercase)
    num = random.randint(10, 99)
    letter2 = random.choice(string.ascii_uppercase)
    return f"Mozilla/5.0 (Windows NT {win}; Win64; x64){letter1}{num}{letter2} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.{build}.150 Safari/537.36"

def create_acc():
    user = 'charsi' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    pasw = 'charsi' + ''.join(random.choices(string.digits, k=7))
    dev_id = str(uuid.uuid4())
    
    url = "https://core.safeum.com/api/v1/auth/register"
    headers = {'User-Agent': get_ua(), 'Content-Type': 'application/json'}
    data = {
        "username": user, "password": pasw, 
        "device_id": dev_id, "app_version": "1.1.0.1332", "os": "Android"
    }

    try:
        res = requests.post(url, json=data, headers=headers, timeout=15)
        if res.status_code == 200 and "Success" in res.text:
            print(f"{green}[SUCCESS] {white}USER: {yellow}{user} {white}| PASS: {yellow}{pasw}")
            with open("charsi_hits.txt", "a") as f:
                f.write(f"{user}:{pasw}\n")
        else:
            print(f"{red}[FAILED] {white}SERVER BUSY OR LIMIT FOR: {user}")
    except:
        print(f"{red}[!] CONNECTION ERROR - CHECK VPN")

if __name__ == "__main__":
    logo()
    try:
        limit = int(input(f"{green}[?] {white}KITNE ACCOUNTS BANANE HAIN? : {yellow}"))
        print(f"{white}-------------------------------------------")
        for _ in range(limit):
            create_acc()
            time.sleep(1.5) # Anti-ban delay
        print(f"{white}-------------------------------------------")
        print(f"{green}[+] DONE! ACCOUNTS SAVED IN charsi_hits.txt")
    except ValueError:
        print(f"{red}[!] INVALID INPUT")
