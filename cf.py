#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Warna
P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
A = '\x1b[38;5;248m' # Abu-Abu

#--> Import Module & Run
try :
    import os, sys, time, re, datetime, random
    from datetime import datetime
except Exception as e :
    print(e)
    exit('\nTerjadi Kesalahan!')
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
reco = 'Gausa Direcode Bos, Tinggal Pake Aja'
rede = 'Dibilangin Gausa Direcode'
key = len(auth1)*len(auth2)-len(auth1)
bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
ok = 0
cp = 0
boys_name = ['Axel Lateef Noah','Anzel Qasim Wisthara','Basheer Malik Yazdan','Bernardus Clementine Christian','Carel Vasco Zachariah','Cyrus Osmanth Elkanah','Damian Vasyl Isaac','Dominic Valdi Xander','Ephraim Benedict Gevariel','El Fatih Ghazwan','Fawwaz Rafisqy Ezaz','Faheem Fakhri Isyraq','Gianluca Nathanael Nadav','Haddad Ammar Ar-Rayyan','Istafa Tabriz Qiwam','Kenneth Krisantus Lazarus','Nathanael Alfred William','Vaskylo Yeremia Clearesta','Xaferius Eliel Antonios','Yesaya Nathanael Liam']
girls_name = ['Atika Fithriya Tsabita','Alya Kinana Juwairiyah','Adzkiya Naila Taleetha','Adiva Arsyila Savina','Aqeela Nabiha Sakhi','Bilqis Adzkiya Rana','Chayra Ainin Qulaibah','Caliana Fiona Syafazea','Chaerunnisa Denia Athalla','Dhawiyah Nisrin Naziha','Dilara Adina Yuani','Farah Sachnaz Ashanty','Ghariyah Zharufa Abidah','Hamna Nafisa Raihana','Hanin Raihana Syahira','Izza Hilyah Nafisah','Kayla Zhara Qamela','Mahreen Shafana Almahyra','Rasahana Shafwa Ruqayah','Shakayla Aretha Shaima']

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

#--> Waktu
def waktu():
    _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
    hari_ini = ("%s%s%s"%(datetime.now().day,_bulan_,datetime.now().year))
    return(str(hari_ini.lower()))

#--> Penjeda Waktu
def jeda(t):
    for x in range(t+1):
        print('\r%sTunggu %s Detik                     '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)
def tunggu_kode(t):
    for x in range(t+1):
        print('\r%sTunggu Kode %s Detik                     '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)

#--> User Agent Vivo (Updated 2025)
def random_ua_vivo():
    os_ver = random.randrange(12, 15)
    dv_typ = random.choice(['V2303','V2310','V2250','V2231','V2219'])
    ch_ver = f'{random.randrange(125, 131)}.0.{random.randrange(6000, 6700)}.{random.randrange(100, 200)}'
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Samsung (Updated 2025)
def random_ua_samsung():
    os_ver = random.randrange(12, 15)
    dv_typ = random.choice(['SM-S928B','SM-S918B','SM-A556B','SM-G990B','SM-M546B'])
    ch_ver = f'{random.randrange(125, 131)}.0.{random.randrange(6000, 6700)}.{random.randrange(100, 200)}'
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Realme (Updated 2025)
def random_ua_realme():
    os_ver = random.randrange(12, 15)
    dv_typ = random.choice(['RMX3840','RMX3710','RMX3741','RMX3771','RMX3890'])
    ch_ver = f'{random.randrange(125, 131)}.0.{random.randrange(6000, 6700)}.{random.randrange(100, 200)}'
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Custom
def random_ua_custom():
    try:
        _file_ = uman
        if 'Android' in str(_file_):
            ad_ver = 'Android ' + str(re.search(r'Android\s+(\d+)', _file_).group(1))
            os_ver = 'Android ' + str(random.randrange(12,15))
            ua1 = _file_.replace(ad_ver,os_ver)
        else: ua1 = _file_
        if 'Build' in str(_file_):
            od_ver = 'Build/' + str(re.search(r'Build/([^;]+)', _file_).group(1))
            bl_typ = random.choice(['UP1A','TP1A','UKQ1','RKQ1','SP1A'])
            dv_ver = random.randrange(100000,250000)
            sd_ver = random.randrange(1,10)
            nw_str = 'Build/' + str('%s.%s.00%s'%(bl_typ,dv_ver,sd_ver))
            ua2 = ua1.replace(od_ver,nw_str)
        else: ua2 = ua1
        if 'Chrome' in str(_file_):
            ch_old = 'Chrome/' + str(re.search(r'Chrome/([^ ]+)', _file_).group(1))
            a = random.randrange(125,131)
            b = random.randrange(6000,6700)
            c = random.randrange(100,200)
            ch_ver = f'{a}.0.{b}.{c}'
            ch_new = 'Chrome/' + str(ch_ver)
            ua3 = ua2.replace(ch_old,ch_new)
        else: ua3 = ua2
        return(ua3)
    except Exception as e:
        return('Mozilla/5.0 (Linux; Android 14; V2303 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.103 Mobile Safari/537.36')

#--> Convert Cookies
def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s;'%(ran['sb'],ran['datr'],ran['c_user'],ran['xs'],ran['fr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s;'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
    return(str(cookie))

#--> Logo
def logo():
    print('%s_________                      __        %s________________ %s'%(P,M,P))
    print('%s\_   ___ \_______ ____ _____ _/  |_  ____%s\_   ____|___   \\%s'%(P,M,P))
    print('%s/    \  \/\_  __ \ __ \\\\__  \\\\   __\/ __ \%s|    __)   |  _/%s'%(P,M,P))
    print('%s\ %s0.1 %s\____|  | \/ ___/ / __ \|  | \  ___/%s|   \  |   |   \\%s'%(P,M,P,M,P))
    print('%s \________/|__|  \_____>______/__|  \____>%s|___/  |_______/%s'%(P,M,P))
    print('%s\n      ─────────────── %s• %sRan_Arraya %s• %s───────────────\n%s'%(A,M,P,M,A,P))

#--> Main Menu
class menu:
    def __init__(self):
        logo()
        self.main_menu()
    def main_menu(self):
        print('%s[%s1%s] %sCreate Account'%(M,P,M,P))
        print('%s[%s2%s] %sCheck Result'%(M,P,M,P))
        print('%s[%s3%s] %sSettings'%(M,P,M,P))
        print('%s[%s4%s] %sBot'%(M,P,M,P))
        x = input(' %s└─ %sPilih %s: %s'%(M,P,M,P)).lower()
        print('')
        if   x in ['1','01','001','a']: menu_create()
        elif x in ['2','02','002','b']: menu_check()
        elif x in ['3','03','003','c']: belum_tersedia()
        elif x in ['4','04','004','d']: belum_tersedia()
        else: exit('%sIsi Yang Benar!%s'%(M,P))

#--> Menu Create
class menu_create:
    def __init__(self):
        global kelamin, namstat, nameme, web_email, tampil, useragent, uman, passtat, password
        try:os.mkdir('Akun_New')
        except Exception as e :pass
        print('      %s◉ %sRekomendasi   %s◉ %sTidak Rekomendasi   ◉ Netral'%(H,P,M,P))
        print('')
        kelamin   = input('%s[%s•%s] %sAkun Laki/Perempuan/Random [%sl%s/%sp%s/%sr%s] : '%(M,P,M,P,H,P,H,P,M,P)).lower()
        namanama  = input('%s[%s•%s] %sGunakan Nama Random/Manual [%sr%s/%sm%s] : '%(M,P,M,P,M,P,H,P)).lower()
        if namanama in ['m','manual','0','00']:
            namstat = 'Manual'
            nameme = input(' %s└─ %sNama : %s'%(M,P,M)).split(',')
        else:
            namstat = 'Random'
        print('%s[%s•%s] %sEmail CryptoGmail/SecMail/MinuteMail'%(M,P,M,P))
        web_email = input(' %s└─ %s[c/s/m] [skip=MinuteMail] : '%(M,P)).lower()
        tampil    = input('%s[%s•%s] %sTampilkan Akun CP [%sy%s/%st%s] : '%(M,P,M,P,M,P,H,P)).lower()
        print('%s[%s•%s] %sUser Agent Vivo/Samsung/Realme/Manual'%(M,P,M,P))
        useragent = input(' %s└─ %s[v/s/r/m] [skip=statis] : '%(M,P)).lower()
        if useragent in ['m','manual','0','00']:
            uman = input(' %s└─ %sUser Agent : %s'%(M,P,M))
            if uman == '' or uman == ' ':
                exit('%sIsi Yang Benar!%s'%(M,P))
        else:
            uman = 'Mozilla/5.0 (Linux; Android 14; RMX3840) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36'
        passtat   = input('%s[%s•%s] %sGunakan Password Random/Manual [%sr%s/%sm%s] : '%(M,P,M,P,H,P,M,P)).lower()
        if passtat in ['m','manual','b','2','02']:
            password = input(' %s└─ %sPassword : %s'%(M,P,M))
            if len(password) < 6:
                exit('%sPassword Minimal 6 Digit!%s'%(M,P))
            if password in ['akusayangkamu','123456','iloveyou','password','qwerty','sayang','anjing','bismillah']:
                exit('%sGunakan Password Yang Kuat!%s'%(M,P))
        else:
            password = 'dapuntaloverani'
        d = input('%s[%s•%s] %sBeri Delay (%sDalam Menit%s) : '%(M,P,M,P,M,P))
        if d == '' or d == ' ':
            d = 1
        print('')
        l = int(d)*60
        for y in range(10000):
            if key/len(auth1) == len(reco)/2: create_fb(); self.hitung(l)
            else: print(reco)
    def hitung(self,a):
        for x in range(a+1):
            print('\r[%sOK:%s%s] [%sCP:%s%s] Tunggu %s Detik         '%(H,str(ok),P,M,str(cp),P,str(a)),end='');sys.stdout.flush()
            a -= 1
            time.sleep(1)

#--> Create Facebook Account
class create_fb:
    def __init__(self):
        self.file  = 'Akun_New/%s.txt'%(waktu())
        self.abc = requests.Session()
        self.xyz = requests.Session()
        self.abc.cookies.clear()
        self.xyz.cookies.clear()
        if   useragent in ['v','vivo','1','01','a']:    self.ua = random_ua_vivo()
        elif useragent in ['s','samsung','2','02','b']: self.ua = random_ua_samsung()
        elif useragent in ['r','realme','3','03','c']:  self.ua = random_ua_realme()
        elif useragent in ['m','manual','0','00','z']:  self.ua = random_ua_custom()
        else : self.ua = 'Mozilla/5.0 (Linux; Android 14; RMX3840) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36'
        self.head_email = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Sec-Ch-Ua-Mobile':'?1','User-Agent':self.ua}
        self.headers_get = {'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-encoding' : 'gzip, deflate','accept-language' : 'id-ID, id;q=0.9, en-US;q=0.8,en;q=0.7','cache-control' : 'max-age=0','sec-fetch-dest' : 'document','sec-fetch-mode' : 'navigate','sec-fetch-site' : 'none','sec-fetch-user' : '1','upgrade-insecure-requests':'1','user-agent' : self.ua}
        self.generate_data()
        self.scrap1()
    
    def generate_data(self):
        self.name, soex = self.get_name().split('|')
        self.nope  = self.get_nope()
        if   web_email in ['c','cryptogmail','1','01','a']: self.email = self.get_email_cryptogmail()
        elif web_email in ['s','secmail','2','02','b']:     self.email = self.get_email_onesecmail()
        elif web_email in ['m','minutemail','4','04','d']:  self.email = self.get_email_10minutemail()
        else : self.email = self.get_email_10minutemail()
        if soex == 'male' : self.sex = '2'
        else : self.sex = '1'
        if passtat in ['m','manual','b','2','02']: self.pw = password
        else: self.pw = self.get_pass()
        self.ttl = {'tgl':str(random.randrange(1,29)),'bln':str(random.randrange(1,13)),'thn':str(random.randrange(1985,2005))}
        self.perangkat = '; m_pixel_ratio=1.25; dpr=1.125; wd=360x780; locale=id_ID;'
    
    def get_name(self):
        if kelamin in ['l','laki','1','01','a']: gder = 'male'
        elif kelamin in ['p','perempuan','2','02','b']: gder = 'female'
        else: gder = random.choice(['male','female'])
        try:
            if gder == 'male':
                if namstat == 'Manual': name = random.choice(nameme)
                else: name = random.choice(boys_name)
            else:
                if namstat == 'Manual': name = random.choice(nameme)
                else: name = random.choice(girls_name)
        except Exception as e:
            name = f'User{random.randrange(100,999)} {random.randrange(100,999)}'
        return(f'{name}|{gder}')

    def get_nope(self):
        na   = random.choice(['77','78','59','12','13'])
        ni   = str(random.randrange(1000,10000))
        nu   = str(random.randrange(10000,100000))
        return('08%s%s%s'%(na,ni,nu))

    def get_pass(self):
        ch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        return(''.join(random.choice(ch) for _ in range(12)).lower())

    def get_email_cryptogmail(self):
        nam = self.name.lower().replace(' ','')
        email = f'{nam}{random.randrange(100,999)}@fexbox.org'
        return(email)
    def get_code_cryptogmail(self):
        try:
            url = f'https://tempmail.plus/api/mails?email={self.email}'
            req = self.abc.get(url,headers=self.head_email).json()
            return(re.search(r'FB-([^ ]+)',str(req)).group(1))
        except: return('00000')

    def get_email_onesecmail(self):
        nam = self.name.lower().replace(' ','')
        dom = random.choice(['1secmail.com','1secmail.org','1secmail.net'])
        return(f'{nam}{random.randrange(100,999)}@{dom}')
    def get_code_onesecmail(self):
        try:
            name, domain = self.email.split('@')
            req = self.abc.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={name}&domain={domain}').json()
            return(re.search(r'FB-([^ ]+)',str(req)).group(1))
        except: return('00000')

    def get_email_10minutemail(self):
        try:
            req = bs(self.abc.get('https://10minutemail.net/m/?lang=id',headers=self.head_email).content,'html.parser')
            self.ses_email = re.search('sessionid="(.*?)"',str(req)).group(1)
            self.tim_email = str(time.time()).replace('.','')[:13]
            pos = self.abc.post('https://10minutemail.net/address.api.php',data={'new':'1','sessionid':self.ses_email,'_':self.tim_email},headers=self.head_email).json()
            self.cookie_email = '; '.join([str(x)+"="+str(y) for x,y in self.abc.cookies.get_dict().items()])
            return(pos['mail_get_mail'])
        except: return('email@error.com')
    def get_code_10minutemail(self):
        try:
            pos = self.abc.post('https://10minutemail.net/address.api.php',data={'new':'0','sessionid':self.ses_email,'_':self.tim_email},headers=self.head_email,cookies={'cookie':self.cookie_email}).json()
            return(re.search(r'FB-([^ ]+)',str(pos)).group(1))
        except: return('00000')

    def scrap1(self): 
        try:
            req = bs(self.xyz.get('https://m.facebook.com/reg/?is_two_steps_login=0&cid=103',headers=self.headers_get).content,'html.parser')
            fom = req.find('form',{'method':'post'})
            data = {
                'lsd':re.search('name="lsd" value="(.*?)"',str(fom)).group(1),
                'jazoest':re.search('name="jazoest" value="(.*?)"',str(fom)).group(1),
                'ccp':re.search('name="ccp" value="(.*?)"',str(fom)).group(1),
                'reg_instance':re.search('name="reg_instance" value="(.*?)"',str(fom)).group(1),
                'reg_impression_id':re.search('name="reg_impression_id" value="(.*?)"',str(fom)).group(1),
                'ns':re.search('name="ns" value="(.*?)"',str(fom)).group(1),
                'app_id':re.search('name="app_id" value="(.*?)"',str(fom)).group(1),
                'logger_id':re.search('name="logger_id" value="(.*?)"',str(fom)).group(1),
                'firstname':self.name,'reg_email__':self.nope,'sex':self.sex,'reg_passwd__':self.pw,
                'birthday_day':self.ttl['tgl'],'birthday_month':self.ttl['bln'],'birthday_year':self.ttl['thn'],
                'multi_step_form':'1','submission_request':True}
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            pos = bs(self.xyz.post('https://m.facebook.com' + fom['action'],data=data,headers=self.headers_get,cookies={'cookie':cok}).content,'html.parser')
            if pos.find('title').text == 'Konfirmasikan Akun Anda': self.scrap4()
            else:
                rog = pos.find('form',{'method':'post'})
                if rog and 'update-nonce' in str(rog['action']): self.scrap2(rog)
                elif rog and 'send_code' in str(rog['action']): self.scrap3(rog)
                else: self.printing('CP')
        except: self.printing('CP')

    def scrap2(self,fom):
        data = {'fb_dtsg':re.search('name="fb_dtsg" value="(.*?)"',str(fom)).group(1),
                'jazoest':re.search('name="jazoest" value="(.*?)"',str(fom)).group(1),
                'submit':'OK'}
        cok = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
        pos = bs(self.xyz.post('https://m.facebook.com' + fom['action'],data=data,headers=self.headers_get,cookies={'cookie':cok}).content,'html.parser')
        self.scrap3(pos.find('form',{'method':'post'}))

    def scrap3(self,fom):
        try:
            data = {'fb_dtsg':re.search('name="fb_dtsg" value="(.*?)"',str(fom)).group(1),
                    'jazoest':re.search('name="jazoest" value="(.*?)"',str(fom)).group(1),
                    'submit':'Kirim kode'}
            cok = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            self.xyz.post('https://m.facebook.com' + fom['action'],data=data,headers=self.headers_get,cookies={'cookie':cok})
            self.scrap4()
        except: self.printing('CP')

    def scrap4(self):
        try:
            cok = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            req = bs(self.xyz.get('https://m.facebook.com/changeemail/',headers=self.headers_get,cookies={'cookie':cok}).content,'html.parser')
            fom = req.find('form',{'method':'post'})
            data = {'fb_dtsg':re.search('name="fb_dtsg" value="(.*?)"',str(fom)).group(1),
                    'jazoest':re.search('name="jazoest" value="(.*?)"',str(fom)).group(1),
                    'new':self.email,'submit':'Tambahkan'}
            self.xyz.post('https://m.facebook.com' + fom['action'],data=data,headers=self.headers_get,cookies={'cookie':cok})
            tunggu_kode(30)
            self.scrap5()
        except: self.printing('CP')

    def scrap5(self):
        try:
            if web_email in ['c']: code = self.get_code_cryptogmail()
            elif web_email in ['s']: code = self.get_code_onesecmail()
            else: code = self.get_code_10minutemail()
            cok = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            id = self.xyz.cookies.get_dict()['c_user']
            data = {'code':code,'submit':'Konfirmasi'}
            self.xyz.post('https://m.facebook.com/confirmation_cliff/',data=data,headers=self.headers_get,cookies={'cookie':cok})
            self.semi_final()
        except: self.printing('CP')

    def semi_final(self):
        try:
            id = self.xyz.cookies.get_dict()['c_user']
            jeda(5)
            if check_account(id) == 'OK': self.printing('OK')
            else: self.printing('CP')
        except: self.printing('CP')

    def printing(self,stat):
        global ok, cp
        if stat == 'OK':
            cookie = cvt('ok',self.xyz.cookies.get_dict())
            id = self.xyz.cookies.get_dict()['c_user']
            print('\r%sStatus : %sSuccess%s                         '%(P,H,P))
            print('ID     : %s | Pass : %s'%(id,self.pw))
            open(self.file,'a+').write('%s|%s|%s|%s\n'%(self.name,id,self.email,self.pw))
            ok += 1
        else:
            if tampil != 't':
                print('\r%sStatus : %sCheckpoint%s                         '%(P,M,P))
            cp += 1

#--> Menu Checker Account
class menu_check:
    def __init__(self):
        self.file = {}
        f = 'Akun_New'
        if os.path.isdir(f):
            l = os.listdir(f)
            for i, y in enumerate(l):
                self.file[str(i+1)] = y
                print(f'{M}[{P}{i+1}{M}] {P}{y}')
            self.sortir()
        else: print('Belum ada hasil.')
    def sortir(self):
        d = input('Pilih file: ')
        if d in self.file:
            g = open(f'Akun_New/{self.file[d]}','r').read().splitlines()
            for a in g:
                n, id, e, p = a.split('|')
                print(f'{id} | {p} -> {check_account(id)}')

def check_account(id):
    try:
        r = requests.get(f'https://www.facebook.com/p/{id}',headers={'User-Agent':'Mozilla/5.0'}).text
        return 'OK' if 'Facebook' not in r else 'CP'
    except: return 'CP'

def belum_tersedia():
    print('Fitur belum tersedia.')

if __name__ == '__main__':
    clear()
    menu()
