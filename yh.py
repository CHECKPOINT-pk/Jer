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

#--> Import Modules
try :
    import os, sys, time, re, datetime, random
    from datetime import datetime
except Exception as e :
    print(e)
    exit('\nAn error occurred during import!')
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

#--> Global Variables
auth1 = 'Dapunta Khurayra X'
auth2 = 'Suci Maharani Putri'
reco = 'Don\'t Recode, Just Use It'
key = len(auth1)*len(auth2)-len(auth1)
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
ok = 0
cp = 0
boys_name = ['Alex Graham','David Miller','John Wick','Robert Downey','Chris Evans','Tony Stark','Steve Rogers','Bruce Banner','Peter Parker','Clark Kent','Basheer Malik','Bernardus Clementine','Cyrus Osmanth','Damian Vasyl','Dominic Valdi','Faheem Fakhri','Gianluca Nathanael','Haddad Ammar','Kenneth Krisantus','Vaskylo Yeremia']
girls_name = ['Sarah Jenkins','Emily Watson','Jessica Alba','Scarlett Rose','Emma Stone','Sophia Loren','Bella Hadid','Kendall Jenner','Gigi Hadid','Gal Gadot','Atika Fithriya','Adzkiya Naila','Adiva Arsyila','Aqeela Nabiha','Bilqis Adzkiya','Chayra Ainin','Caliana Fiona','Dhawiyah Nisrin','Dilara Adina','Farah Sachnaz']

#--> Utilities
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

def waktu():
    _bulan_  = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][datetime.now().month - 1]
    hari_ini = ("%s%s%s"%(datetime.now().day,_bulan_,datetime.now().year))
    return(str(hari_ini.lower()))

def jeda(t):
    for x in range(t+1):
        print('\r%sPlease Wait %s Seconds                     '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)

#--> 2025 Modern User Agents
def random_ua_vivo():
    os_ver = random.randrange(12, 15)
    dv_typ = random.choice(['V2303','V2310','V2250','V2231','V2219'])
    ch_ver = f'{random.randrange(128, 133)}.0.{random.randrange(6000, 6900)}.{random.randrange(100, 250)}'
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

def random_ua_samsung():
    os_ver = random.randrange(12, 15)
    dv_typ = random.choice(['SM-S928B','SM-S918B','SM-A556B','SM-G990B','SM-M546B'])
    ch_ver = f'{random.randrange(128, 133)}.0.{random.randrange(6000, 6900)}.{random.randrange(100, 250)}'
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

def random_ua_realme():
    os_ver = random.randrange(12, 15)
    dv_typ = random.choice(['RMX3840','RMX3710','RMX3741','RMX3771','RMX3890'])
    ch_ver = f'{random.randrange(128, 133)}.0.{random.randrange(6000, 6900)}.{random.randrange(100, 250)}'
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

def random_ua_custom():
    return random_ua_vivo()

#--> Logo
def logo():
    print('%s_________                      __        %s________________ %s'%(P,M,P))
    print('%s\_   ___ \_______ ____ _____ _/  |_  ____%s\_   ____|___   \\%s'%(P,M,P))
    print('%s/    \  \/\_  __ \ __ \\\\__  \\\\   __\/ __ \%s|    __)   |  _/%s'%(P,M,P))
    print('%s\ %s0.1 %s\____|  | \/ ___/ / __ \|  | \  ___/%s|   \  |   |   \\%s'%(P,M,P,M,P))
    print('%s \________/|__|  \_____>______/__|  \____>%s|___/  |_______/%s'%(P,M,P))
    print('%s\n      ─────────────── %s• %sFull Update 2025 %s• %s───────────────\n%s'%(A,M,P,M,A,P))

#--> Main Menu
class menu:
    def __init__(self):
        clear()
        logo()
        self.main_menu()
    def main_menu(self):
        print('%s[%s1%s] %sAuto Create Account'%(M,P,M,P))
        print('%s[%s2%s] %sCheck Results'%(M,P,M,P))
        print('%s[%s3%s] %sSettings'%(M,P,M,P))
        print('%s[%s0%s] %sExit Script'%(M,P,M,P))
        x = input(' %s└─ %sOption %s: %s'%(M,P,M,P)).lower()
        print('')
        if   x in ['1','01']: menu_create()
        elif x in ['2','02']: exit('Results saved in Akun_New folder.')
        else: exit('%sGoodbye!%s'%(M,P))

#--> Creation Menu
class menu_create:
    def __init__(self):
        global kelamin, namstat, nameme, web_email, tampil, useragent, uman, passtat, password
        try:os.mkdir('Akun_New')
        except:pass
        print('      %s◉ %sStable   %s◉ %sRisky   ◉ Neutral'%(H,P,M,P))
        print('')
        kelamin   = input('%s[%s•%s] %sGender [Male/Female/Random] [%sm/f/r%s] : '%(M,P,M,P,H,P)).lower()
        namanama  = input('%s[%s•%s] %sName Mode [Random/Manual] [%sr/m%s] : '%(M,P,M,P,M,P)).lower()
        if namanama == 'm':
            namstat = 'Manual'
            nameme = input(' %s└─ %sEnter Name: %s'%(M,P,M)).split(',')
        else:
            namstat = 'Random'
        print('%s[%s•%s] %sEmail Service [c: Crypto, s: SecMail, m: Minute]'%(M,P,M,P))
        web_email = input(' %s└─ %sSelect: '%(M,P)).lower()
        tampil    = input('%s[%s•%s] %sShow CP Accounts? [y/n]: '%(M,P,M,P)).lower()
        useragent = input('%s[%s•%s] %sUA Device [v/s/r]: '%(M,P,M,P)).lower()
        passtat   = input('%s[%s•%s] %sPassword Mode [Random/Manual]: '%(M,P,M,P)).lower()
        if passtat == 'manual':
            password = input(' %s└─ %sPassword: %s'%(M,P,M))
        else:
            password = 'FB_User_2025'
        d = input('%s[%s•%s] %sDelay (Minutes): '%(M,P,M,P))
        if d == '': d = 1
        l = int(d)*60
        for y in range(10000):
            create_fb()
            self.hitung(l)
    def hitung(self,a):
        for x in range(a+1):
            print('\r[%sOK:%s%s] [%sCP:%s%s] Delaying %s Seconds...         '%(H,str(ok),P,M,str(cp),P,str(a)),end='');sys.stdout.flush()
            a -= 1
            time.sleep(1)

#--> Core Facebook Account Creator
class create_fb:
    def __init__(self):
        self.file = 'Akun_New/Results.txt'
        self.xyz = requests.Session()
        if   useragent == 'v': self.ua = random_ua_vivo()
        elif useragent == 's': self.ua = random_ua_samsung()
        else: self.ua = random_ua_realme()
        self.headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','user-agent':self.ua}
        self.generate_data()
        self.scrap1()

    def generate_data(self):
        gder = random.choice(['male','female']) if kelamin == 'r' else ('male' if kelamin == 'm' else 'female')
        self.name = random.choice(boys_name if gder == 'male' else girls_name) if namstat == 'Random' else random.choice(nameme)
        self.nope = '08' + str(random.randrange(111111111,999999999))
        self.pw = password if passtat == 'manual' else ''.join(random.choice('abcdefgh123456') for _ in range(12))
        self.sex = '2' if gder == 'male' else '1'
        self.ttl = {'d':str(random.randrange(1,28)),'m':str(random.randrange(1,12)),'y':str(random.randrange(1990,2005))}

    def scrap1(self):
        try:
            res = self.xyz.get('https://m.facebook.com/reg/?cid=103', headers=self.headers)
            soup = bs(res.content, 'html.parser')
            form = soup.find('form', {'method': 'post'})
            data = {
                'lsd': soup.find('input', {'name': 'lsd'})['value'],
                'jazoest': soup.find('input', {'name': 'jazoest'})['value'],
                'ccp': soup.find('input', {'name': 'ccp'})['value'] if soup.find('input', {'name': 'ccp'}) else '',
                'reg_instance': soup.find('input', {'name': 'reg_instance'})['value'],
                'firstname': self.name,
                'reg_email__': self.nope,
                'sex': self.sex,
                'reg_passwd__': self.pw,
                'birthday_day': self.ttl['d'],
                'birthday_month': self.ttl['m'],
                'birthday_year': self.ttl['y'],
                'submission_request': True
            }
            pos = self.xyz.post('https://m.facebook.com' + form['action'], data=data, headers=self.headers)
            if 'confirm' in pos.url or 'checkpoint' not in pos.url:
                self.printing('OK')
            else:
                self.printing('CP')
        except:
            self.printing('CP')

    def printing(self, stat):
        global ok, cp
        if stat == 'OK':
            print(f'\r{H}Status : OK | {self.nope} | {self.pw}{P}                 ')
            open(self.file,'a').write(f'{self.nope}|{self.pw}\n')
            ok += 1
        else:
            if tampil == 'y': print(f'\r{M}Status : CP | {self.nope} | {self.pw}{P}                 ')
            cp += 1

if __name__ == '__main__':
    menu()
