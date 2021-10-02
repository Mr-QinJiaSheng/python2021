#客户端：发送消息给服务端
from socket import *

#创建socket对象
#AF_UNIX本机通信 AF_INET（IPV4） AF_INET6（IPV6）
#SOCK_STREAM（TCP）  SOCK_DGRAM（UDP） 
s=socket(AF_INET,SOCK_DGRAM)

#发送信息
while 1==1:
	msg=input("---------<<:")
	s.sendto(msg.encode(),("localhost",3435))

#关闭socket
s.close()
