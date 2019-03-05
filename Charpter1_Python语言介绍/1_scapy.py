from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错

ping_one_reply = sr1(IP(dst='137.78.5.254')/ICMP(), timeout = 1, verbose=False)
ping_one_reply.show()
