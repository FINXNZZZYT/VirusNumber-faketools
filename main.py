import time
import socket

import os, sys, time, requests, json, re, random, itertools, random, threading
from colorama import Fore, Back, init

try:
    import os, sys, time, requests, json, re, random, itertools, threading
    from colorama import Fore, Back, init
except ModuleNotFoundError:
    print("Install Module Dahulu")

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

id = []
P = "\x1b[1;97m"  # PUTIH
M = "\x1b[1;91m"  # MERAH
H = "\x1b[1;92m"  # HIJAU
K = "\x1b[1;93m"
B = "\x1b[1;94m"  # BIRU
U = "\x1b[1;95m"  # UNGU
O = "\x1b[1;96m"  # BIRU MUDA
N = "\x1b[0m"  # WARNA MATI
warna = random.choice(
    ["\x1b[1;91m", "\x1b[1;92m", "\x1b[1;93m", "\x1b[1;94m", "\x1b[1;95m", "\x1b[1;96m"]
)

# warna ngab
Hijau = "\033[1;92m"
putih = "\033[1;97m"
abu = "\033[1;90m"
kuning = "\033[1;93m"
ungu = "\033[1;95m"
merah = "\33[37;1m"
biru = "\033[1;96m"
# Tulisan Background Merah
bg = "\033[1;0m\033[1;41mText\033[1;0m"

hah = f"{W}Menyepam Dalam "
xit = "Exited In "

try:
    ip = requests.get("https://api.ipify.org").text
    localtime = time.asctime(time.localtime(time.time()))
except requests.exceptions.ConnectionError:
    sys.exit(f"{W}Koneksi Tidak Stabil [{R}!{W}]")


def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def prjn():
    lgn = input(f"""{W}[{R}?{W}]  {G}y/n :  """)
    if lgn == "Y" or lgn == "y":
        time.sleep(0.2)
        load()
    put()
    if lgn == "N" or lgn == "n":
        time.sleep(0.2)
        sys.exit(f"{W}[{R}!{W}] Keluar Tools{biru}....{W}")
    else:
        sys.exit(f"{W}[{R}!{W}] Password Salah{biru}....{W}")


def load():
    load = "█"
    count = 0
    for t in range(11):
        time.sleep(0.7)
        print(f"\r{W} Loading.... {R}{t}", end="", flush=True)
        count += 1
        if count == 1:
            count = 0
            load += "&"


def mulai():
    try:
        time.sleep(0.2)
        os.system("clear")
        print(f"""\n""")
        time.sleep(0.1)
        main()
    except requests.exceptions.ConnectionError:
        sys.exit(f"{W}[{R}!{W}] Error Cek Jaringan{abu}....{abu}")
    except KeyboardInterrupt:
        sys.exit(f"{W}[{R}!{W}] Keluar{abu}...{W}")


def main():
    try:
        time.sleep(0.2)
        os.system("clear")
        print(
            f"""
▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
             ░ ░      ░ ░      ░  ░
\033[1;0m\033[1;41mFakeTools\033[1;0m\n{W}[{R}!{W}] Peringatan !\n{W}[{R}!{W}] Fake Tools Fake all!!\n{W}[{R}!{W}] Just for fun """
        )
        time.sleep(4)
        prjn()
    except requests.exceptions.ConnectionError:
        sys.exit(f"{W}[{R}!{W}] Error Cek Jaringan{abu}....{abu}")
    except KeyboardInterrupt:
        sys.exit(f"{W}[{R}!{W}] Keluar{abu}...{W}")


def put():
    try:
        os.system("clear")
        print(
            f"""{G}
        
  █████▒██▓ ███▄    █ ▒██   ██▒ ███▄    █ ▒███████▒▒███████▒▒███████▒▓██   ██▓▄▄▄█████▓
▓██   ▒▓██▒ ██ ▀█   █ ▒▒ █ █ ▒░ ██ ▀█   █ ▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░ ▒██  ██▒▓  ██▒ ▓▒
▒████ ░▒██▒▓██  ▀█ ██▒░░  █   ░▓██  ▀█ ██▒░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░   ▒██ ██░▒ ▓██░ ▒░
░▓█▒  ░░██░▓██▒  ▐▌██▒ ░ █ █ ▒ ▓██▒  ▐▌██▒  ▄▀▒   ░  ▄▀▒   ░  ▄▀▒   ░  ░ ▐██▓░░ ▓██▓ ░
░▒█░   ░██░▒██░   ▓██░▒██▒ ▒██▒▒██░   ▓██░▒███████▒▒███████▒▒███████▒  ░ ██▒▓░  ▒██▒ ░
 ▒ ░   ░▓  ░ ▒░   ▒ ▒ ▒▒ ░ ░▓ ░░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒   ██▒▒▒   ▒ ░░
 ░      ▒ ░░ ░░   ░ ▒░░░   ░▒ ░░ ░░   ░ ▒░░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒ ▓██ ░▒░     ░
 ░ ░    ▒ ░   ░   ░ ░  ░    ░     ░   ░ ░ ░ ░ ░ ░ ░░ ░ ░ ░ ░░ ░ ░ ░ ░ ▒ ▒ ░░    ░
        ░           ░  ░    ░           ░   ░ ░      ░ ░      ░ ░     ░ ░
                                          ░        ░        ░         ░ ░              
                                          
▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
             ░ ░      ░ ░      ░  ░
                                   
                   
{G}<================== Made By FINXNZZZYT ===================>
\033[33;1m
\033[1;0m\033[31;1m▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒ 
▒▒█▒▒▒▄██████████▄▒▒▒▒
▒█▐▒▒▒████████████▒▒▒▒
▒▌▐▒▒██▄▀██████▀▄██▒▒▒
▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒
▐┼▐▒▒██████████████▒▒▒                     
▐▄▐████─▀▐▐▀█─█─▌▐██▄▒                                                      
▒▒█████──────────▐███▌                             
▒▒█▀▀██▄█─▄───▐─▄███▀▒                            
▒▒█▒▒███████▄██████▒▒▒
▒▒▒▒▒██████████████▒▒▒   
▒▒▒▒▒█████████▐▌██▌▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒\033[1;0m

\033[4;37m<========================================================>
\033[1;97m[\033[1;93m•\033[1;97m] GitHub : http://github.com/FINXNZZZYT
\033[1;97m[\033[1;96m•\033[1;97m] {merah}You\033[1;97mTube \033[1;97m : FINXNZZZYT
\033[1;97m[\033[1;96m•\033[1;97m] {merah}Aut\033[1;97mhor \033[1;97m : FINXNZZZYT
\033[1;97m[\033[1;93m•\033[1;97m] Ip Kamu \033[1;97m  :\033[1;93m {ip}
\033[1;97m[\033[1;93m•\033[1;97m] Waktu/Jam \033[1;97m:\033[1;93m {localtime}
\033[1;97m[\033[1;93m•\033[1;97m] Virus Type [Random] : Malware,Trojan,Trojan-Sms,Phising
\033[1;30m<════════════[\033[1;33;41m • \033[1;37m Phone Number \033[1;33m•\033[0m\033[1;30m]══════════════>"""
        )
        mr_ua = random.choice(["Malware", "Trojan", "Trojan-Sms", "Phising", "Trojan"])
        os.system("xdg-open https://youtube.com/@FINXNZZZYT")
        mengetik(f"{W}[{G}•{W}]{G} Send...")
        mr_fnxzz = input(f"{W}[{G}•{W}]{G} Target Number : ")
        mengetik(
            f"{W}[{G}!{W}]{G} Pastikan Nomor Hp Benar Jika Tidak Maka Otomatis Tidak Terkirim Meskipun Ada Peringatan *Sending Virus*"
        )
        time.sleep(5)
        print("")
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
        mengetik(
            f"{W}[{G}✓{W}]{G} Sending Virus To : {Y}{mr_fnxzz}{G} Virus Type : {Y}{mr_ua}"
        )
        time.sleep(0.2)
    except requests.exceptions.ConnectionError:
        sys.exit(f"{W}[{R}!{W}] Error Cek Jaringan lu Ngab{abu}....{abu}")
    except KeyboardInterrupt:
        sys.exit(f"{W}[{R}!{W}] Keluar Tools!!!!{abu}....{abu}")
    except ValueError:
        sys.exit(f"{W}[{R}!{W}] Keluar Tools!!!!{abu}....{abu}")


def pro():
    mulai()


done = False


def loading():
    for c in itertools.cycle(
        [
            "\033[1;37m[\033[31m•\033[1;37m] Starting tools.     ",
            "\033[1;37m[\033[31m•\033[1;37m] sTarting tools..    ",
            "\033[1;37m[\033[31m•\033[1;37m] stArting tools...   ",
            "\033[1;37m[\033[31m•\033[1;37m] staRting tools....  ",
            "\033[1;37m[\033[31m•\033[1;37m] starTing tools..... ",
            "\033[1;37m[\033[31m•\033[1;37m] startIng tools......",
            "\033[1;37m[\033[31m•\033[1;37m] startiNg tools.      ",
            "\033[1;37m[\033[31m•\033[1;37m] startinG tools..     ",
            "\033[1;37m[\033[31m•\033[1;37m] starting Tools...   ",
            "\033[1;37m[\033[31m•\033[1;37m] starting tOols....   ",
            "\033[1;37m[\033[31m•\033[1;37m] starting toOls..... ",
            "\033[1;37m[\033[31m•\033[1;37m] starting tooLs.      ",
            "\033[1;37m[\033[31m•\033[1;37m] starting toolS..    ",
            "\033[1;37m[\033[31m•\033[1;37m] STARTING TOOLS...    ",
            "\033[1;37m[\033[31m•\033[1;37m] STARTING TOOLS....  ",
            "\033[1;37m[\033[31m•\033[1;37m] STARTING TOOLS..... ",
            "\033[1;37m[\033[31m•\033[1;37m] ",
        ]
    ):
        if done:
            break
        sys.stdout.write("\r" + c)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\r              ")
    print("                                                ")
    pro()


t = threading.Thread(target=loading)
t.start()

time.sleep(4.60)
done = True


if __name__ == "__main__":
    mulai()
