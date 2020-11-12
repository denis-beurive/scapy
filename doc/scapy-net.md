# Layer 2

## Ether

    >>> ls(Ether)
    dst        : DestMACField                        = ('None')
    src        : SourceMACField                      = ('None')
    type       : XShortEnumField                     = ('36864')

# Layer 3

## IP

    >>> ls(IP)
    version    : BitField  (4 bits)                  = ('4')
    ihl        : BitField  (4 bits)                  = ('None')
    tos        : XByteField                          = ('0')
    len        : ShortField                          = ('None')
    id         : ShortField                          = ('1')
    flags      : FlagsField                          = ('<Flag 0 ()>')
    frag       : BitField  (13 bits)                 = ('0')
    ttl        : ByteField                           = ('64')
    proto      : ByteEnumField                       = ('0')
    chksum     : XShortField                         = ('None')
    src        : SourceIPField                       = ('None')
    dst        : DestIPField                         = ('None')
    options    : PacketListField                     = ('[]')

## ICMP

    >>> ls(IP)
    version    : BitField  (4 bits)                  = ('4')
    ihl        : BitField  (4 bits)                  = ('None')
    tos        : XByteField                          = ('0')
    len        : ShortField                          = ('None')
    id         : ShortField                          = ('1')
    flags      : FlagsField                          = ('<Flag 0 ()>')
    frag       : BitField  (13 bits)                 = ('0')
    ttl        : ByteField                           = ('64')
    proto      : ByteEnumField                       = ('0')
    chksum     : XShortField                         = ('None')
    src        : SourceIPField                       = ('None')
    dst        : DestIPField                         = ('None')
    options    : PacketListField                     = ('[]')

## ARP 

    >>> ls(ARP)
    hwtype     : XShortField                         = ('1')
    ptype      : XShortEnumField                     = ('2048')
    hwlen      : FieldLenField                       = ('None')
    plen       : FieldLenField                       = ('None')
    op         : ShortEnumField                      = ('1')
    hwsrc      : MultipleTypeField                   = ('None')
    psrc       : MultipleTypeField                   = ('None')
    hwdst      : MultipleTypeField                   = ('None')
    pdst       : MultipleTypeField                   = ('None')

# Layer 4

## UDP

    >>> ls(UDP)
    sport      : ShortEnumField                      = ('53')
    dport      : ShortEnumField                      = ('53')
    len        : ShortField                          = ('None')
    chksum     : XShortField                         = ('None')

## TCP

    >>> ls(TCP)
    sport      : ShortEnumField                      = ('20')
    dport      : ShortEnumField                      = ('80')
    seq        : IntField                            = ('0')
    ack        : IntField                            = ('0')
    dataofs    : BitField  (4 bits)                  = ('None')
    reserved   : BitField  (3 bits)                  = ('0')
    flags      : FlagsField                          = ('<Flag 2 (S)>')
    window     : ShortField                          = ('8192')
    chksum     : XShortField                         = ('None')
    urgptr     : ShortField                          = ('0')
    options    : TCPOptionsField                     = ("b''")

# Application layer

## DNS

    >>> ls(DNS)
    length     : ShortField (Cond)                   = ('None')
    id         : ShortField                          = ('0')
    qr         : BitField  (1 bit)                   = ('0')
    opcode     : BitEnumField                        = ('0')
    aa         : BitField  (1 bit)                   = ('0')
    tc         : BitField  (1 bit)                   = ('0')
    rd         : BitField  (1 bit)                   = ('1')
    ra         : BitField  (1 bit)                   = ('0')
    z          : BitField  (1 bit)                   = ('0')
    ad         : BitField  (1 bit)                   = ('0')
    cd         : BitField  (1 bit)                   = ('0')
    rcode      : BitEnumField                        = ('0')
    qdcount    : DNSRRCountField                     = ('None')
    ancount    : DNSRRCountField                     = ('None')
    nscount    : DNSRRCountField                     = ('None')
    arcount    : DNSRRCountField                     = ('None')
    qd         : DNSQRField                          = ('None')
    an         : DNSRRField                          = ('None')
    ns         : DNSRRField                          = ('None')
    ar         : DNSRRField                          = ('None')

