#商品管理系统
# a.	使用列表嵌套字典的方式保存用户数据（包含用户名，密码，姓名）；
# b.	使用列表嵌套字典的方式保存商品数据（包含编号，名称，价格，折扣）；
# c.	编写用户登录的函数，返回登录结果；
# d.	循环提示菜单，业务完毕时返回主菜单，退出时回到登陆页面；
# e.	将功能菜单中的业务功能各自编写到函数中；
# f.	用户选择不同业务编号时，调用已经写好的各种函数。

#数据准备
user1={"用户名":"aaa","密码":"123","姓名":"张三"}
user2={"用户名":"bbb","密码":"123","姓名":"李四"}
user3={"用户名":"ccc","密码":"123","姓名":"王五"}
usersList=[user1,user2,user3] #用户列表

p1={"编号":"1001","名称":"苹果","价格":5,"折扣":1}
p2={"编号":"1002","名称":"香蕉","价格":3,"折扣":1}
p3={"编号":"1003","名称":"牛奶","价格":4,"折扣":1}
p4={"编号":"1004","名称":"白菜","价格":1,"折扣":1}
p5={"编号":"1008","名称":"西瓜","价格":3,"折扣":1}
productsList=[p1,p2,p3,p4,p5] #商品列表

#登录
def login():
	msg="失败"
	while 1==1:
		uname=input("请输入用户名：")
		upwd=input("请输入密码：")
		for user in usersList:
			if uname==user["用户名"] and upwd==user["密码"]:
				print("---------验证成功！欢迎你，",user["姓名"],"！")
				msg="成功"
				break
		if msg=="失败":
			print("用户名密码错误，请重新输入！")
			continue
		else:
			break
	return msg #返回登录结果

# 1.显示商品列表
def showProcucts():
	print("-编号----名称----价格----折扣-")
	for product in productsList:
		print(product["编号"]+"-----"+product["名称"]+"-----"+str(product["价格"])+"-------"+str(product["折扣"]))
	print("-----------------------------")

# 2.增加商品信息
def addProcuct():
	#生成新编号
	lista=[] #存放所有商品的编号
	for product in productsList:
		lista.append(int(product["编号"]))
	newNum=str(max(lista)+1)
	name=input("请输入商品名称：")
	price=float(input("请输入商品单价："))
	newProduct={"编号":newNum,"名称":name,"价格":price,"折扣":1}
	productsList.append(newProduct)
	print("-------商品",name,"添加成功！")
	showProcucts()

# 3.删除商品（通过编号删除）
def delProcuct():
	while 1==1:
		msg=0 #记录商品是否存在
		num=input("请输入要删除的商品编号：")
		for product in productsList:
			if num==product["编号"]:
				print("---正在删除",product["名称"],"商品...........")
				productsList.remove(product) #删除商品
				print("----删除成功！")
				msg=1
				break
		if msg==0:
			print("商品编号不存在！")
			choice=int(input("取消请按1，重新输入请按2："))
			if choice==1:
				break
			else:
				continue
		else:
			showProcucts()
			break

# 4.设置商品折扣
def setDiscout():
	while 1==1:
		msg=0 #记录商品是否存在
		num=input("请输入要设置折扣的商品编号：")
		for product in productsList:
			if num==product["编号"]:
				newDiscount=float(input("请输入新的折扣（0.1-1）："))
				product["折扣"]=newDiscount #设置折扣
				print("---商品",product["名称"],"折扣已设置成功，",newDiscount*10,"折！")
				msg=1
				break
		if msg==0:
			print("商品不存在！")
			choice=int(input("取消请按1，重新输入请按2："))
			if choice==1:
				break
			else:
				continue
		else:
			showProcucts()
			break

# 5.修改商品价格信息
def setPrice():
	while 1==1:
		msg=0 #记录商品是否存在
		num=input("请输入要调整价格的商品编号：")
		for product in productsList:
			if num==product["编号"]:
				newPrice=float(input("请输入新的价格："))
				product["价格"]=newPrice #设置价格
				print("---商品",product["名称"],"价格已设置成功，",newPrice,"元！")
				msg=1
				break
		if msg==0:
			print("商品不存在！")
			choice=int(input("取消请按1，重新输入请按2："))
			if choice==1:
				break
			else:
				continue
		else:
			showProcucts()
			break

# 6.根据价格排序显示商品列表
def sort():
	choice=int(input("请选择升序或者降序（1.升序  2.降序）："))
	pList=[] #存放所有价格信息
	for product in productsList:
		pList.append(product["价格"])
	pList=list(set(pList)) #去掉重复价格

	print("-编号----名称----价格----折扣-")
	if choice==1:
		newList=sorted(pList)
		for price in newList:
			for product in productsList:
				if price==product["价格"]:
					print(product["编号"]+"-----"+product["名称"]+"-----"+str(product["价格"])+"-------"+str(product["折扣"]))
	else:
		newList=sorted(pList,reverse=True)
		for price in newList:
			for product in productsList:
				if price==product["价格"]:
					print(product["编号"]+"-----"+product["名称"]+"-----"+str(product["价格"])+"-------"+str(product["折扣"]))

#模块化
#-------------------------------------
#显示主菜单，调用已经写好的业务函数

while 0==0:
	# result=login()
	# if result=="成功":
	if 1==1:
		while 2==2:
			print("----------------主菜单---------------")
			print("---1.显示商品列表")
			print("---2.增加商品信息")
			print("---3.删除商品")
			print("---4.设置商品折扣")
			print("---5.修改商品信息")
			print("---6.按照价格排序显示")
			print("---7.退出")

			choice=int(input("请选择业务编号（输入1-6）："))
			if choice==1:
				showProcucts()
			elif choice==2:
				addProcuct()
			elif choice==3:
				delProcuct()
			elif choice==4:
				setDiscout()
			elif choice==5:
				setPrice()
			elif choice==6:
				sort()
			elif choice==7:
				print("-------------正在退出...")
				break
			else:
				print("没有此功能，请重新选择！")
				continue
