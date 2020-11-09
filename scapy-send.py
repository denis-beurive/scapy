from scapy.layers.inet import IP, ICMP
from scapy.all import *


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

res = sr1(IP(dst="10.0.4.254") / ICMP())
for p in res:
    p.show()
    print("-------------------------------------------")
    p.underlayer.show()

# Using traceroute
r = traceroute(["google.fr", "yahoo.fr"])
print(r)
r[0].summary()
r[0].graph()

# sudo apt-get install net-tools
# sudo ifconfig | grep -i mask
arping("10.0.0.0/24")

