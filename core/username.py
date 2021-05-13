#!/usr/bin/env python2 
# -*- coding:utf-8 -*- 
import httplib
import socket
import os,sys
import time
import requests
os.system('clear')
def logop(z):
    for word in z + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.0001)
def logop2(z):
    for word in z + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.001)        
banner1= '''\033[91m██     ██ ███████ ██████                                
\033[91m██     ██ ██      ██   ██                               
\033[91m██  █  ██ █████   ██████                                
\033[91m██ ███ ██ ██      ██   ██                               
\033[91m ███ ███  ███████ ██████                                
                                                        
                                                        
    ██   ██ ██    ██ ███    ██ ████████ ███████ ██████  
    ██   ██ ██    ██ ████   ██    ██    ██      ██   ██ 
    ███████ ██    ██ ██ ██  ██    ██    █████   ██████  
    ██   ██ ██    ██ ██  ██ ██    ██    ██      ██   ██ 
    ██   ██  ██████  ██   ████    ██    ███████ ██   ██ 


                                                        
                              '''
                                                        
banner2 ='''\033[93m
     Author    : Dark Hunter 141
     Tool      : Web Hunter
     Version   : 1.0
     Github    : https://github.com/darkhunter141
     Facebook  : https://www.facebook.com/darkhunter141
     Devolopers: Ashrafi Abir (DarkXploit)
                 Tanvir Mahamud Shariful (DarkWolf)
             


                   \033[0m \033[0;37;41mCreated By Team Dark Hunter 141\033[0m 

            \033[0m          \033[0;37;41m Wordpress Username Finder\033[0m 


 '''  
os.system('clear')
try: 
	import requests
	import json
	from colorama import Fore, Back, Style 
	import time
	import sys
	from urlparse import urlparse
except Exception as err:
	print "[!] "+str(err)
	sys.exit(0)


payload ="wp-json/wp/v2/users/"
G  = '\033[1;32m' 
O  = '\033[33m' 

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() 
        time.sleep(8./90)



def start(argv):
	if len(sys.argv) < 2:
		print Fore.WHITE+"Usage: python wpUsersScan.py URL \n"
		sys.exit(1)
	url = argv[0]	
	o = urlparse(url)
	if o[0] not in ['http','https']:
		print Fore.RED+"[!] Please checkout your URL http:// or https:// "+Fore.RESET
		sys.exit(0)		
	url = sys.argv[1]
	if url[-1] != "/":
		url+="/"
	logop (banner1)
	logop2 (banner2)
	print Fore.GREEN+"[✓] Scaning Start,Please wait...\n\n[+] Target : "+url+"\n"	
	print Fore.GREEN+"[+] USERS \n"	
	GetUsersList(url)	



def GetUsersList(url):

	try:
		r = requests.get(url+payload)
		if r.status_code == 200 :
			Pjson = requests.get(url+payload).json()
			u =0
			for user in Pjson:
				u+=1
				print Fore.CYAN+"ID : "+str(user["id"])+Fore.RED+" | Name : "+Fore.WHITE+user["name"]+Fore.YELLOW+" | Username: "+user["slug"]+"\n"
				
		else:
			print Fore.RED+"[!] No User found !!"		
	except requests.exceptions.RequestException as e:  
	    print e
	    sys.exit(1)



if __name__ == "__main__":
	try:
		start(sys.argv[1:])
	except KeyboardInterrupt as err:
		print "\n[!] By... :)"
		sys.exit(0)
