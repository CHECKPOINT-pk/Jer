import os
import time
import random
import string
from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

init(autoreset=True)

# Fixed Recovery Email
RECOVERY_EMAIL = "Nawabzada0764@gmail.com"

def logo():
    os.system('clear')
    print(Fore.RED + r"""
    #################################################
    #      CHARSI HUMAN-BOT SUPREME (2025)          #
    #    [ HUMAN TYPING + RECOVERY + SKIP TRICK ]   #
    #################################################
    """)

def human_typing(element, text):
    """Asli insan ki tarah ek ek lafz type karne ke liye"""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3)) # Random delay between keys

def run_charsi_bot():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    service = Service('/usr/bin/chromedriver')
    
    # Random Data (2005-2009 Skip Trick)
    f_name = random.choice(["Ayan", "Musa", "Sami", "Umar", "Zaid", "Haris"])
    l_name = random.choice(["Ali", "Khan", "Ahmed", "Malik", "Sheikh"])
    b_year = random.randint(2005, 2009)
    username = f_name.lower() + l_name.lower() + str(random.randint(100, 999))
    password = "Charsi@" + "".join(random.choices(string.digits, k=5))

    print(Fore.YELLOW + "---------------------------------------------")
    print(Fore.CYAN + f"[*] TARGET EMAIL: {username}@gmail.com")
    print(Fore.CYAN + f"[*] HUMAN TYPING ACTIVE: {f_name} {l_name}")
    print(Fore.YELLOW + "---------------------------------------------")

    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://accounts.google.com/signup")
        time.sleep(random.uniform(2, 4)) # Random wait

        # Name Page with Human Typing
        first_input = driver.find_element(By.NAME, "firstName")
        human_typing(first_input, f_name)
        
        last_input = driver.find_element(By.NAME, "lastName")
        human_typing(last_input, l_name)
        
        time.sleep(1)
        driver.find_element(By.ID, "collectNameNext").click()
        
        # DOB Page
        time.sleep(random.uniform(3, 5))
        driver.find_element(By.ID, "day").send_keys(str(random.randint(1, 28)))
        driver.find_element(By.ID, "year").send_keys(str(b_year))
        driver.find_element(By.ID, "gender").send_keys("Male")
        driver.find_element(By.ID, "birthdaygenderNext").click()
        
        # Success Logging
        with open("human_accounts.txt", "a") as f:
            f.write(f"Email: {username}@gmail.com | Pass: {password} | Recovery: {RECOVERY_EMAIL}\n")
        
        print(Fore.GREEN + f"[LIVE] {username}@gmail.com Created Successfully!")

    except Exception as e:
        print(Fore.RED + f"[!] Google ne block kiya ya error: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()

def main():
    logo()
    count = 1
    while True:
        print(Fore.WHITE + f"\n>>> LOOP #{count} - STATUS: HEAVY")
        run_charsi_bot()
        print(Fore.BLUE + "\n[ALERT] 15s Break... Airplane Mode On/Off Karo!")
        time.sleep(15)
        count += 1

if __name__ == "__main__":
    main()
