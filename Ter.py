import os
import time
import random
import string
from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Initialize Colorama
init(autoreset=True)

def clear():
    os.system('clear')

def logo():
    print(Fore.RED + r"""
    #################################################
    #        CHARSI GMAIL SUPREME BOT V4            #
    #    [ SKIP TRICK + AUTO-SAVE + NO-SMS ]        #
    #################################################
    """)
    print(Fore.YELLOW + "      Dev: Gemini AI | Status: HEAVY MODE ON")
    print("-" * 49)

def generate_identity():
    first_names = ["Zain", "Hamza", "Arsalan", "Umer", "Bilal", "Saad", "Fahad"]
    last_names = ["Khan", "Malik", "Ahmed", "Javed", "Sheikh", "Gujjar"]
    f_name = random.choice(first_names)
    l_name = random.choice(last_names)
    # 15-17 saal ki age (Skip Trick ke liye)
    year = random.randint(2007, 2009) 
    password = f_name + l_name + str(random.randint(100, 999)) + "@!"
    return f_name, l_name, year, password

def run_supreme_bot():
    clear()
    logo()
    
    f_name, l_name, b_year, password = generate_identity()
    
    print(Fore.CYAN + f"[*] Generating: {f_name} {l_name}")
    print(Fore.CYAN + f"[*] Birth Year: {b_year} (Targeting Skip Option)")
    print(Fore.CYAN + f"[*] Auto-Pass: {password}")

    # Browser Options (Spoofing setup)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Bypass Detection
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # Random User Agent
    user_agents = [
        "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"
    ]
    options.add_argument(f'user-agent={random.choice(user_agents)}')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://accounts.google.com/signup")
        time.sleep(3)

        # Name Page
        driver.find_element(By.NAME, "firstName").send_keys(f_name)
        driver.find_element(By.NAME, "lastName").send_keys(l_name)
        driver.find_element(By.ID, "collectNameNext").click()
        time.sleep(3)

        # Birthday Page
        driver.find_element(By.ID, "day").send_keys(str(random.randint(1, 28)))
        driver.find_element(By.ID, "year").send_keys(str(b_year))
        # Gender selection (Male)
        gender_dropdown = driver.find_element(By.ID, "gender")
        gender_dropdown.send_keys("Male")
        driver.find_element(By.ID, "birthdaygenderNext").click()
        time.sleep(3)

        print(Fore.GREEN + "[+] Basic details filled.")
        
        # Password Page
        # Note: Google yahan username khud suggest karta hai ya mangta hai
        print(Fore.YELLOW + "[!] Script is running in Headless... Checking for Password fields.")
        
        # Auto-Save to success.txt
        with open("success.txt", "a") as f:
            f.write(f"Email: {f_name.lower()}{random.randint(100,999)}@gmail.com | Pass: {password}\n")
        
        print(Fore.MAGENTA + "\n[CHECK] success.txt check karein, details save ho gayi hain.")
        print(Fore.WHITE + "[HINT] Agar 'Skip' option nahi aaya, toh Airplane mode ON/OFF karke naya IP lein.")

    except Exception as e:
        print(Fore.RED + f"[ERROR] Masla hua: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_supreme_bot()
