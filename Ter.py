import os
import time
import random
import string
import requests
from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

init(autoreset=True)

def logo():
    os.system('clear')
    print(Fore.RED + r"""
    #################################################
    #        CHARSI PRO MAX - PROXY EDITION         #
    #    [ AUTO-PROXY + LOOP + SKIP ACTIVE ]        #
    #################################################
    """)

# Internet se free proxies uthane wala function
def get_proxies():
    print(Fore.YELLOW + "[*] Fetching fresh proxies...")
    try:
        res = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymosity=all")
        proxies = res.text.splitlines()
        return proxies
    except:
        return []

def run_supreme_bot(proxy=None):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    if proxy:
        print(Fore.CYAN + f"[*] Using Proxy: {proxy}")
        options.add_argument(f'--proxy-server={proxy}')

    service = Service('/usr/bin/chromedriver')
    
    # Details generation
    f_name = "Charsi" + "".join(random.choices(string.ascii_lowercase, k=3))
    l_name = "Don" + str(random.randint(10, 99))
    b_year = random.randint(2007, 2009)
    password = f_name + "@" + str(random.randint(1000, 9999))

    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.set_page_load_timeout(30)
        driver.get("https://accounts.google.com/signup")
        time.sleep(3)

        # Name & DOB Fill
        driver.find_element(By.NAME, "firstName").send_keys(f_name)
        driver.find_element(By.NAME, "lastName").send_keys(l_name)
        driver.find_element(By.ID, "collectNameNext").click()
        time.sleep(3)
        
        driver.find_element(By.ID, "day").send_keys(str(random.randint(1, 25)))
        driver.find_element(By.ID, "year").send_keys(str(b_year))
        driver.find_element(By.ID, "gender").send_keys("Male")
        driver.find_element(By.ID, "birthdaygenderNext").click()
        
        print(Fore.GREEN + f"[+] Success: Details submitted for {f_name}")
        
        with open("success_log.txt", "a") as f:
            f.write(f"Email: {f_name.lower()}@gmail.com | Pass: {password} | Proxy: {proxy}\n")

    except Exception as e:
        print(Fore.RED + f"[!] Proxy Slow ya Error: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()

def main():
    logo()
    proxy_list = get_proxies()
    count = 1
    
    while True:
        print(Fore.WHITE + f"\n>>> Loop #{count}")
        current_proxy = random.choice(proxy_list) if proxy_list else None
        run_supreme_bot(current_proxy)
        
        # Thoda gap taake Google server ko shak na ho
        print(Fore.BLUE + "[*] Sleeping for 15 seconds... Best time for Airplane Mode toggle!")
        time.sleep(15)
        count += 1

if __name__ == "__main__":
    main()
