#服务端：接收客户端消息并显示
from socket import *

#创建socket对象 
s=socket(AF_INET,SOCK_STREAM)

#绑定监听端口
s.bind(("localhost",6363))

#监听
s.listen()

#等待消息
conn,adr=s.accept()

#接收信息
msg=conn.recv(1024)

print("--------:",msg.decode())

s.close()