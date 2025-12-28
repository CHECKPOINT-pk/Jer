import requests, random, string, uuid, time, os

def fast_fix():
    os.system('clear')
    print("KAZAKHSTAN BYPASS - FIXING CONNECTION...")
    
    # Random User Details
    u = 'charsi' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    p = 'charsi' + ''.join(random.choices(string.digits, k=8))
    did = str(uuid.uuid4())
    
    url = "https://core.safeum.com/api/v1/auth/register"
    headers = {
        'User-Agent': 'SafeUM/1.1.0.1380 (Android 11)',
        'Content-Type': 'application/json'
    }
    data = {"username": u, "password": p, "device_id": did, "app_version": "1.1.0.1380", "os": "Android"}

    try:
        # Timeout 40 seconds kar diya hai Kazakhstan VPN ke liye
        res = requests.post(url, json=data, headers=headers, timeout=40)
        if "Success" in res.text:
            print(f"SUCCESS: {u}:{p}")
        else:
            print("SERVER REJECTED - CHANGE CITY IN VPN")
    except Exception as e:
        print("STILL CONNECTION ERROR - YOUR VPN IS BLOCKING TERMUX")

if __name__ == "__main__":
    fast_fix()
