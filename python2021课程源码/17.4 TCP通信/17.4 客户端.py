#客户端：发送消息给服务端
from socket import *

#创建socket对象
#AF_UNIX本机通信 AF_INET（IPV4） AF_INET6（IPV6）
#SOCK_STREAM（TCP）  SOCK_DGRAM（UDP） 
s=socket(AF_INET,SOCK_STREAM)

#和目标建立连接
s.connect(("localhost",6363))

#发送消息
s.send("你好！服务端！".encode())  #.encode()对字符串进行编码

#关闭socket
s.close()
