# 案例：模拟银行ATM存款取款

# 1.模拟3张银行卡,1001,1002,1003,分别设置密码和余额(使用列表嵌套字典的方式)；

# 2.提示用户输入银行卡和密码，遍历每张卡的信息验证是否成功；

# 3.如果用户输入正确---提示让用户选择取款.存款还是退出,并提示余额多少.  输入错误---重新输入卡号密码；
# 选择取款---提示输入取款额度,如果超过余额,提示余额不足;否则,在余额上减掉相应金额；
# 选择存款---输入存款额度,余额加上相应额度,并提示余额多少；
# 选择退出---重新登录；

# 4.连续3次输入错误账号密码,提示银行卡已被锁定，程序结束。

card1={"姓名":"张三","卡号":"1001","密码":"123","余额":10000}
card2={"姓名":"李四","卡号":"1002","密码":"123","余额":20000}
card3={"姓名":"王五","卡号":"1003","密码":"123","余额":30000}
card4={"姓名":"赵六","卡号":"1004","密码":"123","余额":40000}
cardsList=[card1,card2,card3,card4]
count=0 #记录输入错误的次数
while 1==1:
	cnum=input("请输入卡号：")
	cpwd=input("请输入密码：")
	msg=0 #记录登录状态 0失败 1成功！
	for card in cardsList:
		if cnum==card["卡号"] and cpwd==card["密码"]:
			msg=1
			count=0 #当验证成功时，错误次数清零
			print("恭喜你！",card["姓名"],"！验证成功！")
	if msg==0:
		count+=1
		if count==3:
			print("您已经连续3次输入错误，银行卡被锁定！")
			break
		else:
			print("验证失败！您已经连续",count,"次输入错误,还有",3-count,"次机会！")
			continue

	#银行业务
	while 2==2:
		choice=int(input("请输入要办理的业务编号（1.存款 2.取款 3.退出）："))
		if choice==1:
			money1=float(input("请输入存款金额："))
			for card in cardsList:
				if card["卡号"]==cnum:
					card["余额"]=card["余额"]+money1
					print("存款成功！存入",money1,"元！余额",card["余额"],"元！")
					break
		elif choice==2:
			money2=float(input("请输入取款金额："))
			for card in cardsList:
				if card["卡号"]==cnum:
					card["余额"]=card["余额"]-money2
					print("取款成功！取出",money2,"元！余额",card["余额"],"元！")
					break
		elif choice==3:
			print("-----------已退出！-------------")
			break
		else:
			print("没有此业务，请重新选择！")
			continue






