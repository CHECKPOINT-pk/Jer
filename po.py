import mechanize
import http.cookiejar
import os

def start_process():
    print("--- FB 2026 AUTO UPDATE SCRIPT ---")
    email = input("Email/Number: ")
    password = input("Password: ")

    # Browser simulation
    br = mechanize.Browser()
    cj = http.cookiejar.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; Android 13; Pixel 7)')]

    try:
        print("\n[+] Logging in to get fresh cookies...")
        br.open("https://m.facebook.com")
        br.select_form(nr=0)
        br['email'] = email
        br['pass'] = password
        br.submit()

        # Check if login success
        if "checkpoint" in br.geturl():
            print("[!] Security Checkpoint! Please login manually once.")
            return
        
        print("[+] Login Success! Extracting Cookies...")
        
        # Injects Invalid Name to force Update Name state
        print("[+] Forcing Update Name State...")
        br.open("https://m.facebook.com/settings/edit/?name")
        br.select_form(nr=0)
        br['firstname'] = "Ahmad @#!$"
        br['lastname'] = "Update-Name-Force"
        br.submit()
        
        print("\n[✔] Process Complete. Ab ID login karke check karen.")

    except Exception as e:
        print(f"[!] Error: {str(e)}")

start_process()
