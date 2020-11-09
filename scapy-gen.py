from scapy.layers.inet import IP, TCP, Ether
from scapy.all import *

# Create packets and send them.
# Note : you must be "root" to execute this script.
#        Number of packet in "p": len(list(p)).
#        The code below sends 4 packets.
p = IP(dst="8.8.8.8", ttl=[1, 10]) / TCP(dport=[80, 543])
print(f"Number of packets: {len(list(p)):d}")
for k in p:
    print(p.sprintf("   SEND> %IP.src% > %IP.dst%"))
    raw(k)
send(p)

# Create a funky packet.
p = Ether(b"Ceci est un exemple")
p.show()

# Call WireShark on the packet.
wireshark(p)


