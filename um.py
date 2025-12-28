import requests
import random
import string
import uuid
import time

# 2025 Updated User-Agent
def get_ua():
    windows_versions = ['10.0', '11.0']
    chrome_major = random.randint(131, 135)
    chrome_build = random.randint(6700, 6900)
    chrome_patch = random.randint(1, 150)
    rand_letter = random.choice(string.ascii_uppercase)
    rand_num = random.randint(10, 99)
    return f"Mozilla/5.0 (Windows NT {random.choice(windows_versions)}; Win64; x64){rand_letter}{rand_num}{rand_letter} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{chrome_build}.{chrome_patch} Safari/537.36"

def generate_number():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    device_id = str(uuid.uuid4())
    
    reg_url = "https://core.safeum.com/api/v1/auth/register"
    headers = {'User-Agent': get_ua(), 'Content-Type': 'application/json'}
    
    data = {
        "username": username,
        "password": password,
        "device_id": device_id,
        "app_version": "1.1.0.1332",
        "os": "Android"
    }

    try:
        # Step 1: Account Create Karo
        reg_res = requests.post(reg_url, json=data, headers=headers, timeout=10)
        if reg_res.status_code == 200 and reg_res.json().get("status") == "Success":
            print(f"[+] Account Created: {username}")
            
            # Step 2: Login karke Number check karo
            login_url = "https://core.safeum.com/api/v1/auth/login"
            login_res = requests.post(login_url, json=data, headers=headers, timeout=10)
            
            if login_res.status_code == 200:
                user_info = login_res.json().get("data", {})
                phone = user_info.get("phone_number") # SafeUM API se number nikalna
                
                if phone and "+371" in phone:
                    print(f"[🔥] SUCCESS! Number Found: {phone}")
                    with open("hit_numbers.txt", "a") as f:
                        f.write(f"User: {username} | Pass: {password} | Number: {phone}\n")
                else:
                    print(f"[-] No Number (Empty Slot) for: {username}")
        else:
            print(f"[-] Registration Failed for {username}")
            
    except Exception as e:
        print(f"[!] Error: {e}")

# Script start
if __name__ == "__main__":
    print("--- SafeUM Number Hunter 2025 ---")
    while True:
        generate_number()
        time.sleep(1) # Block hone se bachne ke liye
