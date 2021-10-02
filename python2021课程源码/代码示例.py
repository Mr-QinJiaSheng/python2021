#系统名称：学生管理系统
stu1={"学号":"1001","姓名":"张三", "性别":"男", "年龄":12, "班级":"3班"}
stu2={"学号":"1002","姓名":"李四", "性别":"男", "年龄":13, "班级":"4班"}
stu3={"学号":"1003","姓名":"王五", "性别":"女", "年龄":12, "班级":"1班"}
stu4={"学号":"1004","姓名":"大宝", "性别":"男", "年龄":13, "班级":"3班"}
stu5={"学号":"1005","姓名":"二宝", "性别":"女", "年龄":12, "班级":"2班"}
stuList=[stu1,stu2,stu3,stu4,stu5]

#保存学生信息
user1={"name":"admin", "password":"123"}
user2={"name":"aaa", "password":"666"}
userList=[user1,user2]

#循环执行登录
while 1==1:
	#登录功能
	uname=input("请输入用户名：") 
	upwd=input("请输入密码：")

	msg1=0 #记录登录状态
	for user in userList:
		if uname==user["name"] and upwd==user["password"]:
			msg1=1 #改变登录状态
			break
	if msg1==1:
		print("登陆成功！")
	else:
		print("登录失败！请重新登录！")
		continue

	#显示功能菜单
	print("-----欢迎来到学生管理系统------")
	while 1==1:
		print("-----1.显示所有学生信息-------")
		print("-----2.增加学生--------------")
		print("-----3.学生毕业--------------")
		print("-----4.修改学生信息-----------")
		print("-----5.退出------------------")
		choice=input("请输入选择的功能编号：")
		if choice=="1":
			print("学号----姓名----性别----年龄----班级")
			for stu in stuList:
				print(stu["学号"],"---",stu["姓名"],"---",stu["性别"],"---",stu["年龄"],"---",stu["班级"])
			print("-----------------------------------")
		elif choice=="2":
			stunum=""
			msg2=0 #记录学号是否存在
			while 1==1:
				stunum=input("请输入新学生的学号：")
				for stu in stuList:
					if stu["学号"]==stunum:
						msg2=1
				if msg2==1:
					print("学号已存在，请重新输入")
				else:
					print("学号有效！")
					break
			stuname=input("请输入姓名：")
			stusex=input("请输入性别（男、女）：")
			stuage=int(input("请输入年龄："))
			stuclass=input("请输入班级：")
			print("学生",stuname,"添加成功！")
			stuList.append({"学号":stunum,"姓名":stuname, "性别":stusex, "年龄":stuage, "班级":stuclass}) #添加到学生列表
			
			print("学号----姓名----性别----年龄----班级")
			for stu in stuList:
				print(stu["学号"],"---",stu["姓名"],"---",stu["性别"],"---",stu["年龄"],"---",stu["班级"])
			print("-----------------------------------")

		elif choice=="3":
			msg3=0 
			while 1==1:
				stunum=input("请输入要删除的学生学号：")
				for stu in stuList:
					if stu["学号"]==stunum:
						print("学生",stu["姓名"],"删除成功！")
						stuList.remove(stu) #从类表中删除学生信息
						msg3=1
						break
				if msg3==0:
					print("学号不存在，请重新输入！")
					continue
				else:
					break
			if msg3==1:
				print("学号----姓名----性别----年龄----班级")
				for stu in stuList:
					print(stu["学号"],"---",stu["姓名"],"---",stu["性别"],"---",stu["年龄"],"---",stu["班级"])
			print("-----------------------------------")

		elif choice=="4":
			msg4=0 
			while 1==1:
				stunum=input("请输入要修改的学生学号：")
				for stu in stuList:
					if stu["学号"]==stunum:
						msg4=1
						choice2=input("请输入要修改的内容（1.年龄 2.班级）：")
						if choice2=="1":
							stuage=int(input("请输入新的年龄："))
							stu["年龄"]=stuage #修改
						elif choice2=="2":
							stuclass=int(input("请输入新的班级："))
							stu["班级"]=stuclass #修改
						else:
							print("输入错误！")
						break
				if msg4==0:
					print("学号不存在，请重新输入！")
					continue
				else:
					print("学生信息修改成功！")
					break
			if msg4==1:
				print("学号----姓名----性别----年龄----班级")
				for stu in stuList:
					print(stu["学号"],"---",stu["姓名"],"---",stu["性别"],"---",stu["年龄"],"---",stu["班级"])
			print("-----------------------------------")
		elif choice=="5":
			print("用户",uname,"已退出！")
			break
		else:
			print("没有此功能，请重新输入！")

