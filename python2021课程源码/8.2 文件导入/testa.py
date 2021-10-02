def function1():
	print("A中的函数1被执行了！")

def function2():
	print("A中的函数2被执行了！")

def function3():
	print("A中的函数3被执行了！")


#-----------------------------
def main():
	if 1==1:
		function1()
		print("A中默认执行语句！")

if __name__ == '__main__': #当直接执行当前文件时运行的语句
	main()