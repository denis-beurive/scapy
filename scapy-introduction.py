from scapy.layers.inet import IP, UDP, TCP, Ether, IPTools
from scapy.layers.vxlan import VXLAN
from scapy.all import *


# Build 6 packets.
packets: Packet = Ether() / IP() / VXLAN() / UDP()
packets.ttl = (10, 12)  # TTL from 10 to 12.
packets.dport = [80, 453]  # Destination port 80 and 453.
print(f"Number of packets: {len(list(packets)):d}")
packet: Packet
for packet in packets:
    print(packet.sprintf("%IP.src%:%IP.sport% > %IP.dst%:%IP.dport%"))
    if TCP in packet:
        print("This packet has a TCP packet")
    if UDP in packet:
        print("This packet has a UDP packet")
print("")


# Print the description of the first packet.
p: Packet = list(packets)[0]
p.show()


# Build packets: condensed notation
# Build 1 packet
packets: Ether = Ether(dst='01:02:03:04:05:06') /\
                 IP(id=1, ttl=15, src='192.0.0.1', dst='192.0.0.2') /\
                 TCP(sport=10, dport=20)
list(packets)[0].show()

# Build 2 packets
packets: Ether = Ether(dst='01:02:03:04:05:06') /\
                 IP(id=1, ttl=15, src='192.0.0.1', dst='192.0.0.2') /\
                 TCP(sport=[10, 20], dport=20)
list(packets)[0].show()
list(packets)[1].show()


# Load a PPACP file
packets: PacketList = rdpcap('file.pcap')
packet: Packet
for packet in packets:
    if IP in packet:
        print(packet.sprintf("in PCAP %IP.src%:%IP.sport% > "
                             "%IP.dst%:%IP.dport%"))
print("")


# Filter a list of packets. Keep all packets in "packets" that contain TCP.
packet: Packet
for packet in packets.filter(lambda p: UDP in p):
    print(packet.sprintf("in PCAP UDP %IP.src%:%IP.sport% > "
                         "%IP.dst%:%IP.dport%"))
print("")


# Keep all packets in "a" that contain TCP, and that have layers on top of TCP.
# Have TCP: "TCP in p"
# Have layers on top of TCP: "p[TCP].payload".
packet: Packet
for packet in packets.filter(lambda p: TCP in p and p[TCP].payload):
    print(packet.sprintf("in PCAP TCP with payload %IP.src%:%IP.sport% > "
                         "%IP.dst%:%IP.dport%"))
print("")


# Test if a layer has padding or not.
p: IP = IP() / TCP() / Padding(b"toto")
print("\"p\" has padding" if isinstance(p[TCP].payload, Padding) else
      "\"p\" has no padding")  # => has padding
p: IP = IP() / TCP() / Raw(b"toto") / Padding(b"toto")
print("\"p\" has padding" if isinstance(p[TCP].payload, Padding) else
      "\"p\" has no padding")  # => has no padding

