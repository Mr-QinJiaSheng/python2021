# return的另一个用法

# def function1():
# 	print("function1被执行了！")
# 	return "hello"



#嵌套循环终止问题
def function2():
	for x in range(1,11):
		print("--------------第",x,"年！")
		for y in range(1,13):
			print("第",x,"年！，第",y,"月！")
			if x==5 and y==5: #在第5年第5月终止整个循环
				msg=1
				return #退出整个函数

function2()