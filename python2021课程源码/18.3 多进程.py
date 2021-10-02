# 多进程：一个程序运行过程中，产生了多个进程

# n个正在运行的程序----至少n个进程
# 1个程序-----可能只有一个进程，也可能有多个进程


#引入进程类
from multiprocessing import Process
import time

#任务1
def run1():
	print("执行了任务1！")
	time.sleep(5)

#任务2
def run2():
	print("执行了任务2！")
	time.sleep(5)

#任务3
def run3():
	print("执行了任务3！")
	time.sleep(5)


#--------------------串行
# run1()
# run2()
# run3()


#--------------------并行
#创建进程对象
p1=Process(target=run1)  #(target=要执行的任务方法)
p2=Process(target=run2)
p3=Process(target=run3)

if __name__ == '__main__':
	p1.start() #启动进程,只能写道main中
	p2.start()
	p3.start()
