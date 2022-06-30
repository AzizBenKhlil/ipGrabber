import sys,os,re,socket,time,random,colorama
from colorama import *
from random import choice
from colorama import Fore,Back,init
colorama.init()


# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
BLUE  = "\033[34m"
CYAN  = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD    = "\033[m"
REVERSE = "\033[m"
#coded by mister spy
#contact me 712083179
def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """ 

  ___                       _     _               
 |_ _|_ __   __ _ _ __ __ _| |__ | |__   ___ _ __ 
  | || '_ \ / _` | '__/ _` | '_ \| '_ \ / _ \ '__|
  | || |_) | (_| | | | (_| | |_) | |_) |  __/ |   
 |___| .__/ \__, |_|  \__,_|_.__/|_.__/ \___|_|   
     |_|    |___/                                 
				  Telegram: @ZoxTn
			                  """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)
logo()


def getIP(site):
	
		site = i.strip()
		try:
			if 'http://' not in site:
				IP1 = socket.gethostbyname(site)
				print "IP: "+IP1
				open('ips.txt', 'a').write(IP1+'\n')
			elif 'http://' in site:
				url = site.replace('http://', '').replace('https://', '').replace('/', '')
				IP2 = socket.gethostbyname(url)
				print "IP: "+IP2
				open('ips.txt', 'a').write(IP2+'\n')
	
		except:
			pass
			
nam=raw_input('Domain List name :')
with open(nam) as f:
    for i in f:
        getIP(i)

		
