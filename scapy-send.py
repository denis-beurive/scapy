# Notes:
#    - sendp(): send layer 2
#    - sr(), sr1(): send layer 3


from scapy.all import *
from scapy.layers.inet import IP, ICMP, traceroute, TracerouteResult
from scapy.layers.l2 import arping, ARPingResult, PacketList
from typing import Tuple

# Send a packet and get the response.
# sr / sr1 / srloop: use layer 3.
# Options:
#    - retry
#    - timeout
#    - verbose
#    - multi: whether to accept more that one response
#    - filter
#    - iface

# Note: ip route | grep default
#       default via 10.0.4.254 dev eno1 proto dhcp metric 100
# To print the attributes of ICMP: ICMP().show()

packets: tuple = sr(IP(dst="192.168.1.254") / ICMP(code=(0, 3)))
print(f'Number of packets tuple (request, response): {len(list(packets)):d}')
req_resp_list: SndRcvList
for req_resp_list in packets:
    req_resp_list.show()

# Only send and receive one packet.
packet: Packet = sr1(IP(dst="www.slashdot.org")/ICMP()/"XXXXXXXXXXX")
packet.show()


print("\n--------------------------------------------------\n")


# Using traceroute
results: Tuple[TracerouteResult] = traceroute(["google.fr", "yahoo.fr"])
packets: PacketList
for packets in results:
    print("\n--------------------------------------------------\n")
    packets.summary()


# sudo apt-get install net-tools
# sudo ifconfig | grep -i mask
result: Tuple[ARPingResult, PacketList] = arping("10.0.0.0/24")
print("ARPing result:")
print(result[0])
print(f"List of packets ({len(list(result[1])):d})")
packet: Packet
for packet in result[1]:
    packet.show()

