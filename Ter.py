import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def solve_issue():
    options = Options()
    # Google ko dhoka dene ke liye headless mode ke sath window size zaroori hai
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    
    # Ye line automation detection ko khatam karti hai
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # Path check: Termux default path use karein
    try:
        service = Service('/usr/bin/chromedriver')
        driver = webdriver.Chrome(service=service, options=options)
        
        print("Testing Connection...")
        driver.get("https://accounts.google.com/signup")
        time.sleep(5)
        
        if "Create" in driver.title or "Sign" in driver.title:
            print("✅ SCRIPT WORKING! Google page load ho gaya hai.")
            # Yahan screenshot lein taake aap dekh saken kya ho raha hai
            driver.save_screenshot("check_page.png")
            print("Screenshot saved as 'check_page.png'. Isay check karein.")
        else:
            print("❌ Google ne block kiya ya page load nahi hua.")
            
    except Exception as e:
        print(f"❌ Driver Error: {str(e)}")
    finally:
        if 'driver' in locals():
            driver.quit()

solve_issue()
