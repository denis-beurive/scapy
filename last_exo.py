# Please remember:
#    - sendp(): send layer 2
#    - sr(), sr1(): send layer 3

from scapy.layers.inet import Ether, IP, UDP, TCP, ICMP
from scapy.layers.vxlan import VXLAN
from scapy.layers.l2 import ARP, Dot1Q
from scapy.all import *

MY_ID = 0x272a
SRC_IP = '1.2.3.4'
DST_IP = '5.6.7.8'
MAC = '00:5c:a4:75:ca:47'
BASE_IP_FRAME = Ether(dst=MAC) / IP(id=MY_ID, src=SRC_IP, dst=DST_IP)

# Print the default configuration.
print(conf.iface)


# Exo #1
if False:
    print("Exo 1")
    packet = BASE_IP_FRAME /\
             ICMP(type=8)  # code=0
    packet.add_payload(b"Denis BEURIVE")
    packet.show()
    sendp(packet, iface='eno1')


# Exo #2
if False:
    print("Exo 2")
    pad = Padding(b"EVIRUEB sineD")
    packet = BASE_IP_FRAME /\
             ICMP(type='echo-reply')
    packet.add_payload(b"Denis BEURIVE")
    packet /= pad
    packet.show()
    sendp(packet, iface='eno1')


# Exo #3
if False:
    print("Exo 3")
    packet = Ether(dst=MAC) / IP(id=MY_ID, src=DST_IP, dst=DST_IP) / TCP(sport=1234, dport=1234)
    packet.add_payload(b"Denis BEURIVE")
    packet.show()
    sendp(packet, iface='eno1')


# Exo #4
if False:
    print("Exo 4")
    packet = Ether(dst=MAC) / IP(id=MY_ID, src=SRC_IP, dst=DST_IP) / UDP(dport=5353, len=8)
    packet.add_payload(b"Denis BEURIVE")
    packet.show()
    sendp(packet, iface='eno1')


# Exo #5
if False:
    print("Exo 5")
    packet = Ether(dst=MAC) / IP(id=MY_ID, src='8.8.8.8', dst=DST_IP) / \
             UDP(sport=1234, dport=5678, len=13) /\
             Raw(load='MAGIC')
    packet.add_payload(b"Denis BEURIVE")
    packet.show()
    sendp(packet, iface='eno1')






