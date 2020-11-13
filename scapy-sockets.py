from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from scapy.layers.inet import IP, TCP, UDP
from scapy.volatile import RandShort
from scapy.packet import Raw



try:
    s = socket(AF_INET, SOCK_STREAM)
    p = IP(dst="192.168.1.254") / \
        TCP(flags="S", sport=RandShort(), dport=80) / \
        Raw("Hello world!")
    s.connect(("192.168.1.254", 80))
    s.send(bytes(p))
except Exception as e:
    raise e


try:
    s = socket(AF_INET, SOCK_DGRAM)
    p = IP(dst="192.168.1.254") / \
        UDP(sport=RandShort(), dport=80) / \
        Raw("Hello world!")
    s.sendto(bytes(p), ("192.168.1.254", 80))
except Exception as e:
    raise e

