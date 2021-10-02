import threading
import time

def run(name):
	print(name,"执行了任务！")
	time.sleep(5)

#创建线程对象
t1=threading.Thread(target=run,args=("t1",))
t2=threading.Thread(target=run,args=("t2",))
t3=threading.Thread(target=run,args=("t3",))

#启动线程
t1.start()
t2.start()
t3.start()

