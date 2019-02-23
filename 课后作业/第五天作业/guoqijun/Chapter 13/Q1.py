from scapy.all import *

class qyt_ping:
    def __init__(self,ip):
        self.ip = ip
        self.srcip = None
        self.length = 100
        self.pkt = IP(dst=self.ip,src=self.srcip)/ICMP()

    def src(self,srcip):
        self.srcip = srcip
        self.pkt = IP(dst=self.ip,src=self.srcip)/ICMP()

    def size(self,length):
        self.length = length
        self.pkt = IP(dst=self.ip,src=self.srcip)/ICMP()

    def one(self):
        result = sr1(self.pkt,timeout=1,verbose=False)
        if result:
            print(self.ip,'Reachable')
        else:
            print(self.ip,'Unreachable')

    def ping(self):
        for i in range(5):
            result = sr1(self.pkt,timeout=1,verbose=False)
            if result:
                print('!',end='',flush=True)
            else:
                print('.',end='',flush=True)
        print()