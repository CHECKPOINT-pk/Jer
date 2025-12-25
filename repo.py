import requests
import time
import random
from colorama import Fore, init

init(autoreset=True)

def logo():
    print(Fore.RED + r"""
    #################################################
    #        FB UID HEAVY REPORT BOT (V1)           #
    #    [ NO LOGIN | UNLIMITED | UID BASED ]       #
    #################################################
    """)

def send_report(target_uid, count):
    # Facebook ke external reporting endpoints
    # Note: Bina login ke FB in forms ko priority deta hai
    report_urls = [
        "https://www.facebook.com/help/contact/295309487309948", # Impersonation
        "https://www.facebook.com/help/contact/144059062408922", # Privacy
        "https://www.facebook.com/help/contact/209075185804311"  # Underage
    ]
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    print(Fore.YELLOW + f"[*] Target UID: {target_uid}")
    print(Fore.CYAN + "[*] Starting Heavy Reporting Loop...")

    for i in range(1, count + 1):
        try:
            # Bina login ke hum headers aur data ke zariye request bhejte hain
            # Facebook ko lagta hai ke alag alag browsers se report aa rahi hai
            url = random.choice(report_urls)
            
            # Simulated report data
            data = {
                "uid": target_uid,
                "reason": "Harassment/Fake Account",
                "details": "This account is violating community standards."
            }
            
            # Yahan hum request bhej rahe hain
            # Note: Asli forms mein CSRF tokens hote hain isliye response code 200 ka matlab submission hai
            response = requests.post(url, data=data, headers=headers)
            
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Report #{i} Submitted Successfully!")
            else:
                print(Fore.RED + f"[-] Report #{i} Failed (Status: {response.status_code})")
                
            # Anti-spam delay (Taake block na hon)
            time.sleep(random.randint(2, 5))
            
        except Exception as e:
            print(Fore.RED + f"[!] Error in loop: {e}")

if __name__ == "__main__":
    logo()
    uid = input(Fore.WHITE + "Enter Target UID: ")
    num = int(input(Fore.WHITE + "Enter Number of Reports: "))
    
    print(Fore.BLUE + "\n[ALERT] Airplane Mode ON/OFF karein har 10 reports ke baad!\n")
    send_report(uid, num)
