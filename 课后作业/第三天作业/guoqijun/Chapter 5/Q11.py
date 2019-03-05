import re

ifconfig_result = 'eno33554944:flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500\n   inet 202.100.1.138 netmask 255.255.255.0 broadcast 202.100.1.255\n   inet6 fe80::20c:29ff:fe8d:5cb6 prefixlen 64 scopeid 0x20<link>\n   ether 00:0c:29:8d:5c:b6 txqueuelen 1000 (Ethernet)\n   RX packets 0 bytes 0 (0.0 B)\n   RX errors 0 dropped 0 overruns 0 frame 0\n   TX packets 33 bytes 4290 (4.1 KiB)\n TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0\n\n'

re_findall_result = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)

for ip in re_findall_result:
    if ip.split('.')[3] == '0':
        mask = ip
    elif ip.split('.')[3] == '255':
        broadcast = ip
    else:
        ipv4_ip = ip

print('%15s : %-15s' % ('Network Mask',mask))
print('%15s : %-15s' % ('Broadcast',broadcast))
print('%15s : %-15s' % ('IPv4 Addr',ipv4_ip))