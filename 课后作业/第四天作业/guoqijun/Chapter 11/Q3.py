
from scapy.all import *

def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        print(ip+' '+'通!')
    else:
        print(ip+' '+'不通!')

qytang_ping('192.168.2.254')