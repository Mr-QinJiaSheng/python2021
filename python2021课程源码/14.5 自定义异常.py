exp=Exception("性别只能是男或者女！") #创建一个异常对象

sex=input("请输入您的性别（男，女）")
if sex=="男" or sex=="女":
	print("您输入的性别：",sex)
else:
	print("您输入的性别有误！")
	raise exp