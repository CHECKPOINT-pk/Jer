import os
import time
import random
import string
from colorama import Fore, Style, init
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# Colors aur Style Initialize
init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    print(Fore.GREEN + r"""
      ______ _    _          _____   _____ _____ 
     / ____| |  | |   /\   |  __ \ / ____|_   _|
    | |    | |__| |  /  \  | |__) | (___   | |  
    | |    |  __  | / /\ \ |  _  / \___ \  | |  
    | |____| |  | |/ ____ \| | \ \ ____) |_| |_ 
     \_____|_|  |_/_/    \_\_|  \_\_____/|_____|
    """)
    print(Fore.YELLOW + "      [+] Unlimited Gmail Creator - Charsi Edition [+]")
    print(Fore.CYAN + "      [+] Status: Active | Dev: Gemini AI Partner [+]")
    print("-" * 55)

def random_string(length=5):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def create_gmail():
    print(Fore.BLUE + "\n[*] Browser khul raha hai... Intezar karein.")
    
    options = uc.ChromeOptions()
    # Mobile emulation taake 'Skip' option milne ke chance hon
    options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36')
    
    driver = uc.Chrome(options=options)
    
    try:
        driver.get('https://accounts.google.com/signup')
        time.sleep(3)

        # Details Filling
        f_name = "Charsi"
        l_name = "Don"
        user_name = f_name.lower() + l_name.lower() + random_string(4)
        password = "CharsiPass@" + random_string(3)

        print(Fore.MAGENTA + f"[!] Filling Name: {f_name} {l_name}")
        driver.find_element(By.NAME, "firstName").send_keys(f_name)
        driver.find_element(By.NAME, "lastName").send_keys(l_name)
        driver.find_element(By.ID, "collectNameNext").click()
        time.sleep(3)

        print(Fore.MAGENTA + "[!] Selecting DOB & Gender...")
        driver.find_element(By.ID, "day").send_keys("20")
        driver.find_element(By.ID, "year").send_keys("1995")
        # Gender selection manual ya focus se karni hogi
        print(Fore.YELLOW + "[?] Screen par Gender select karke Next dabayen.")
        
        print(Fore.CYAN + f"[!] Suggested Username: {user_name}")
        print(Fore.CYAN + f"[!] Password: {password}")
        
        print(Fore.GREEN + "\n[SUCCESS] Details fill ho gayi hain!")
        print(Fore.RED + "[!] Ab Verification page par khud control sambhalen.")
        
        input("\nBrowser band karne ke liye Enter dabayen...")
    except Exception as e:
        print(Fore.RED + f"\n[ERROR] Kuch masla hua: {e}")
    finally:
        driver.quit()

def main_menu():
    while True:
        clear()
        logo()
        print(Fore.WHITE + "1. Create New Gmail (Auto-Fill)")
        print(Fore.WHITE + "2. Settings (Proxy/API)")
        print(Fore.WHITE + "3. About Charsi Bot")
        print(Fore.RED + "4. Exit")
        
        choice = input(Fore.YELLOW + "\n[?] Option Select Karein: ")
        
        if choice == '1':
            create_gmail()
        elif choice == '2':
            print(Fore.RED + "\n[!] Proxy Settings coming soon...")
            time.sleep(2)
        elif choice == '3':
            print(Fore.GREEN + "\n[+] Yeh bot Gmail automation ke liye banaya gaya hai.")
            time.sleep(3)
        elif choice == '4':
            print(Fore.YELLOW + "\nAllah Hafiz!")
            break
        else:
            print(Fore.RED + "\nInvalid Choice!")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
