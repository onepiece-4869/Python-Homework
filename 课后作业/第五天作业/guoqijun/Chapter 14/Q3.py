
from scapy.all import *


def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=1, verbose=False)
    if ping_result:
        return ip,1
    else:
        return ip,0


if __name__ == '__main__':
    import sys
    result = qytang_ping(sys.argv[1])

    if result[1]:
        print(result[0], '通!')
    else:
        print(result[0], '不通!')
