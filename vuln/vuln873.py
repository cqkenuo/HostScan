# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

from lib import *
import socket

timeout = 2

def p873(portdic):
	p873list=[]
	for ip in portdic:
		ip = ip.split(":")
		if ip[-1] == "873":
			p873list.append(do_nmap(ip[0]))
	return p873list

def do_nmap(ip):
	try:
		payload = b"\x40\x52\x53\x59\x4e\x43\x44\x3a\x20\x33\x31\x2e\x30\x0a"
		socket.setdefaulttimeout(timeout)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = (ip, 873)
		sock.connect(server_address)
		sock.sendall(payload)
		initinfo = sock.recv(400)
		if "RSYNCD" in initinfo:
			sock.sendall(b"\x0a")
		modulelist = sock.recv(200)
		sock.close()
		if len(modulelist) > 0:
			print("存在Rsync未授权访问漏洞")
			a =ip +":873:存在Rsync未授权访问漏洞"
			return a
		else:
			pass
	except:
		pass
