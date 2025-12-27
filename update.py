import requests
import os

def force_update():
    print("--- FB Account Update Name Guard 2026 ---")
    token = input("Apna Facebook Access Token ya Cookie dalein: ")
    
    # Invalid symbols jo Meta ko confuse karte hain
    invalid_name = "Ahmad @#!$%^&*()"
    
    url = f"https://graph.facebook.com/me?name={invalid_name}&method=post&access_token={token}"
    
    print("\nRequest bhej raha hoon... Account check karein.")
    
    response = requests.post(url)
    
    if response.status_code == 200:
        print("Success! Account update name par chala gaya hoga.")
    else:
        print("Error: Shayad token expire hai ya Meta ne block kiya.")
        print("Mashwara: Manual 'Learn More' wala tareeqa use karein.")

force_update()
