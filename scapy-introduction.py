# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.vxlan import VXLAN
from scapy.all import *

# Build packets.
p = IP() / VXLAN() / IP() / UDP()
p.ttl = (10, 12)  # TTL from 10 to 12.
p.dport = [80, 453]  # Destination port 80 and 453.
for k in p:
    print(p.sprintf("%IP.src% > %IP.dst%"))
    raw(k)

# Sniff packets...
# Note: to make it work:
#       xhost +
#       Then log as "root": sudo su
a = sniff(count=6)
a.conversations()
for p in a.sr():
    print(p.show())

# Get all sessions (from >> to).
sessions: dict = a.sessions()
for key in sessions.keys():
    # The session (from >> to)
    print(key)
    # The list of packets within the current session.
    print(sessions[key])

# Keep all packets in "a" that contain TCP.
for k in a.filter(lambda p: TCP in p):
    print(k)

# Keep all packets in "a" that contain TCP, and that have layers on top of TCP.
# Have TCP: "TCP in p"
# Have layers on top of TCP: "p[TCP].payload".
for k in a.filter(lambda p: TCP in p and p[TCP].payload):
    print(k)

# Test if a layer has padding.
p = IP() / TCP() / Padding(b"toto")
print("p[TCP] has padding" if isinstance(p[TCP].payload, Padding) else "has no padding")

p = IP() / TCP() / Raw(b"toto") / Padding(b"toto")
print("p[TCP] has padding" if isinstance(p[TCP].payload, Padding) else "has no padding")





