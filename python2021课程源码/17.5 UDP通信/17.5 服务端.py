#服务端：接收客户端消息并显示
from socket import *
import time

#创建socket对象 
s=socket(AF_INET,SOCK_DGRAM)

#绑定端口
s.bind(("localhost",3435))

#接收信息
while 1==1:
	msg=s.recv(1024)
	print("----:",msg.decode())

s.close()