from scapy.all import *

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

# Get 6 packets.
sniff(count=6, filter="tcp")

# Execute a function on the fly and print a summary for each packet.
#    - store: (0|1) store packets or not.
#    - filter: BPF filter.
#    - lfilter: lambda x: TCP in p.
#    - offline: read a PCAP file.
#    - prn: callback function.
#    - iface: set an interface to sniff to.
#    - stop.filter: callback function. If True, then stop the filter.
a = sniff(count=6, prn=lambda x: x.summary())

# Write the packets into a PCAP file.
wrpcap("file.pcap", a)
