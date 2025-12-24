#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Colors
P = "\x1b[38;5;231m" # White
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green
A = '\x1b[38;5;248m' # Grey

#--> Import Module & Run
try :
    import os, sys, time, re, datetime, random
    from datetime import datetime
except Exception as e :
    print(e)
    exit('\nAn error occurred while importing modules!')
try :
    import requests
except Exception as e :
    os.system('pip install requests')
    import requests
try :
    import bs4
    from bs4 import BeautifulSoup as bs
except Exception as e :
    os.system('pip install bs4')
    import bs4
    from bs4 import BeautifulSoup as bs

#--> Global Variable
auth1 = 'Dapunta Khurayra X'
auth2 = 'Suci Maharani Putri'
reco = 'Don\'t Recode, Just Use It'
key = len(auth1)*len(auth2)-len(auth1)
ok = 0
cp = 0
boys_name = ['Alex Graham','David Miller','John Wick','Robert Downey','Chris Evans','Tony Stark','Steve Rogers','Bruce Banner','Peter Parker','Clark Kent']
girls_name = ['Sarah Jenkins','Emily Watson','Jessica Alba','Scarlett Rose','Emma Stone','Sophia Loren','Bella Hadid','Kendall Jenner','Gigi Hadid','Gal Gadot']

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

#--> Modern User Agents (2025 Update)
def random_ua_modern():
    os_ver = random.randrange(12, 15)
    dv_typ = random.choice(['SM-S928B','RMX3840','V2303','SM-A556B','RMX3710'])
    ch_ver = f'{random.randrange(128, 133)}.0.{random.randrange(6000, 6900)}.{random.randrange(100, 250)}'
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ch_ver} Mobile Safari/537.36'
    return ua

#--> Logo
def logo():
    print('%s_________                      __        %s________________ %s'%(P,M,P))
    print('%s\_   ___ \_______ ____ _____ _/  |_  ____%s\_   ____|___   \\%s'%(P,M,P))
    print('%s/    \  \/\_  __ \ __ \\\\__  \\\\   __\/ __ \%s|    __)   |  _/%s'%(P,M,P))
    print('%s\ %s0.1 %s\____|  | \/ ___/ / __ \|  | \  ___/%s|   \  |   |   \\%s'%(P,M,P,M,P))
    print('%s \________/|__|  \_____>______/__|  \____>%s|___/  |_______/%s'%(P,M,P))
    print('%s\n      ─────────────── %s• %sUpdated By Gemini %s• %s───────────────\n%s'%(A,M,P,M,A,P))

#--> Main Menu
class menu:
    def __init__(self):
        clear()
        logo()
        self.main_menu()
    def main_menu(self):
        print('%s[%s1%s] %sStart Create Facebook Account'%(M,P,M,P))
        print('%s[%s2%s] %sCheck Saved Accounts'%(M,P,M,P))
        print('%s[%s0%s] %sExit'%(M,P,M,P))
        x = input(' %s└─ %sSelect Option %s: %s'%(M,P,M,P))
        if x in ['1','01']: menu_create()
        elif x in ['2','02']: exit('Results are in Results/ folder.')
        else: exit()

#--> Create Account Menu
class menu_create:
    def __init__(self):
        global kelamin, namstat, nameme, web_email, useragent, passtat, password
        try:os.mkdir('Results')
        except:pass
        
        kelamin   = input('%s[%s•%s] %sGender [m/f/r] : '%(M,P,M,P)).lower()
        namanama  = input('%s[%s•%s] %sName Type [random/manual] : '%(M,P,M,P)).lower()
        if namanama == 'manual':
            namstat = 'Manual'
            nameme = input(' %s└─ %sEnter Name (comma separated) : %s'%(M,P,M)).split(',')
        else:
            namstat = 'Random'
            
        print('%s[%s•%s] %sEmail: [c] CryptoGmail, [s] SecMail, [m] MinuteMail'%(M,P,M,P))
        web_email = input(' %s└─ %sSelect : '%(M,P)).lower()
        
        passtat   = input('%s[%s•%s] %sPassword [random/manual] : '%(M,P,M,P)).lower()
        if passtat == 'manual':
            password = input(' %s└─ %sEnter Password : %s'%(M,P,M))
        else:
            password = 'FB_User_2025!'
            
        d = input('%s[%s•%s] %sSet Delay (minutes) [Default 1]: '%(M,P,M,P))
        if d == '': d = 1
        l = int(d)*60
        
        print('\n%sStarting... Use Airplane Mode every 2 accounts!%s\n'%(H,P))
        for y in range(1000):
            create_fb()
            self.countdown(l)

    def countdown(self, a):
        for x in range(a+1):
            print('\r[%sOK:%s%s] [%sCP:%s%s] Next in %s seconds...      '%(H,str(ok),P,M,str(cp),P,str(a)),end='');sys.stdout.flush()
            a -= 1
            time.sleep(1)

#--> Core Creation Logic
class create_fb:
    def __init__(self):
        self.xyz = requests.Session()
        self.ua = random_ua_modern()
        self.headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': self.ua,
        }
        self.generate_data()
        self.start_reg()
    
    def generate_data(self):
        gder = random.choice(['male','female']) if kelamin == 'r' else ('male' if kelamin == 'm' else 'female')
        self.name = random.choice(boys_name if gder == 'male' else girls_name) if namstat == 'Random' else random.choice(nameme)
        self.nope = '08' + str(random.randrange(111111111,999999999))
        self.pw = password if passtat == 'manual' else ''.join(random.choice('abcdefg12345') for _ in range(10))
        self.sex = '2' if gder == 'male' else '1'
        self.day = str(random.randrange(1,28))
        self.month = str(random.randrange(1,12))
        self.year = str(random.randrange(1992,2004))

    def start_reg(self):
        global ok, cp
        try:
            res = self.xyz.get('https://m.facebook.com/reg/?cid=103', headers=self.headers)
            soup = bs(res.content, 'html.parser')
            form = soup.find('form', {'method': 'post'})
            
            data = {
                'lsd': soup.find('input', {'name': 'lsd'})['value'],
                'jazoest': soup.find('input', {'name': 'jazoest'})['value'],
                'firstname': self.name,
                'reg_email__': self.nope,
                'sex': self.sex,
                'reg_passwd__': self.pw,
                'birthday_day': self.day,
                'birthday_month': self.month,
                'birthday_year': self.year,
                'submit': 'Sign Up'
            }
            
            post_res = self.xyz.post('https://m.facebook.com' + form['action'], data=data, headers=self.headers)
            
            if 'confirm' in post_res.url or 'checkpoint' not in post_res.url:
                print(f'\r{H}Status: Success! | ID: {self.nope} | Pass: {self.pw}{P}')
                open('Results/OK.txt','a').write(f'{self.nope}|{self.pw}\n')
                ok += 1
            else:
                cp += 1
        except:
            cp += 1

if __name__ == '__main__':
    menu()
