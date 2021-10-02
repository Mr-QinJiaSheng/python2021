from threading import Thread
from socket import *

#接收信息
def recvData():
	while 1==1:
		msg=s.recv(1024)
		print(">>:",msg.decode())

#发送信息
def sendData():
	while 1==1:
		info=input("<<:")
		s.sendto(info.encode(),(ip,port))

#----------------------------
ip="localhost" #对方ip
port=9012 #对方端口号

s=socket(AF_INET,SOCK_DGRAM)
s.bind(("localhost",9011))

#创建线程
tr=Thread(target=recvData)
ts=Thread(target=sendData)

tr.start()
ts.start()