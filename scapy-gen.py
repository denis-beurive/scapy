from scapy.layers.inet import IP, TCP, Ether
from scapy.all import *

# Create packets and send them.
# Note : you must be "root" to execute this script.
#        Number of packet in "p": len(list(p)).
#        The code below sends 4 packets.
packets: IP = IP(dst="8.8.8.8", ttl=[1, 10]) / TCP(dport=[80, 543])
print(f"Number of packets: {len(list(packets)):d}")
packet: IP
for packet in packets:
    print(packet.sprintf("   SEND> %IP.src% > %IP.dst%"))
send(packets)

# Create a funky packet.
packet: Ether = Ether(b"Ceci est un exemple")
packet.show()

# Call WireShark on the packet.
wireshark(packet)


