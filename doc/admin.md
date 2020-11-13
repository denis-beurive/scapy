# Networking notes

![](OSI-1.jpg)

![](OSI-2.gif)

# Find your IP address

    $hostname -I
    192.168.1.22 2001:861:3005:c5f0:f12c:1e35:9be1:bfc5 2001:861:3005:c5f0:e5c0:74c0:ee4:c3cc 

    $ /sbin/ifconfig

    $ ip a
    
# Find my public address

    $ dig +short ANY whoami.akamai.net @ns1-1.akamaitech.net
    176.144.220.100

# Find my default gateway

    $ ip route | grep default
    default via 192.168.1.254 dev enp5s0 proto dhcp metric 100 
    
    $ ip r
    default via 192.168.1.254 dev enp5s0 proto dhcp metric 100 
    169.254.0.0/16 dev enp5s0 scope link metric 1000 
    192.168.1.0/24 dev enp5s0 proto kernel scope link src 192.168.1.22 metric 100 

    $ route -n
    Kernel IP routing table
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    0.0.0.0         192.168.1.254   0.0.0.0         UG    100    0        0 enp5s0
    169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 enp5s0
    192.168.1.0     0.0.0.0         255.255.255.0   U     100    0        0 enp5s0

# ARP table

Print the ARP table:

    arp -na

Delete an entry in the ARP table:

    arp -d <IP address>
