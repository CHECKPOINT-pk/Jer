import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def run_final_bot():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    # --- TERMUX ARCHITECTURE FIX ---
    # Hum selenium ko khud dhundne nahi denge, hum rasta khud batayenge
    try:
        service = Service('/usr/bin/chromedriver') 
        driver = webdriver.Chrome(service=service, options=options)
        
        print("✅ Driver Connected! Starting Gmail Creation...")
        driver.get("https://accounts.google.com/signup")
        
        # Details (2005-2009 Age Trick)
        f_name = "Charsi" + str(random.randint(10,99))
        print(f"[*] Filling details for: {f_name}")
        
        # Baki aapki typing logic yahan aayegi...
        time.sleep(5)
        
        # Proof ke liye screenshot
        driver.save_screenshot("work_proof.png")
        print("✅ Screenshot saved as 'work_proof.png'. Check it with 'ls'")

    except Exception as e:
        print(f"❌ Abhi bhi error hai: {e}")
        print("\nHINT: Agar '/usr/bin/chromedriver' nahi mila, toh 'pkg install chromedriver' dobara karein.")
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    run_final_bot()
