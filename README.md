# WebSniff
### http流量嗅探，并获取登陆的账号密码

局域网arp欺骗攻击+本地http流量嗅探，可获取局域网http账号登录密码


#### 进行ARP欺骗：

python ArpPoison.py         (arp欺骗)

#### 进行网络嗅探：

python WebSniff.py          (流量嗅探)

*注：如果局域网做了MAC地址与IP地址绑定，或者网关有防ARP攻击，则嗅探不会成功！*
<hr>

By   nmask    2016
