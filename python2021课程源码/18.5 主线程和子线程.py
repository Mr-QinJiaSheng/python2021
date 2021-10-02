import threading
import time

def run(name):
	time.sleep(5)
	print(name,"执行了任务！")

#程序执行时，程序本身就是一个线程，称为主线程
#手动创建的线程，称为子线程
#主线程执行中不会等待子线程执行完毕，会直接执行后面代码

#创建线程对象
t1=threading.Thread(target=run,args=("t1",))
t2=threading.Thread(target=run,args=("t2",))
t3=threading.Thread(target=run,args=("t3",))

#启动线程
t1.start()
t2.start()
t3.start()

t1.join() #需要等待当前线程执行完毕，才能继续执行主线程
t2.join()
t3.join()

print("执行完毕！")

