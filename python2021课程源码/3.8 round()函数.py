num1="1001"
price1=7.9
name1="苹果"

num2="1002"
price2=4.9
name2="香蕉"

num3="1003"
price3=5.9
name3="梨子"

num=input("请输入商品编号：")
count=int(input("请输入商品数量："))

#提前声明变量保存需要的商品价格和名称
price=0
name=""
if num==num1:
	price=price1
	name=name1
elif num==num2:
	price=price2
	name=name2
elif num==num3:
	price=price3
	name=name3
else:
	print("没有此商品！")
	
if price!=0:	
	amount=price*count #计算商品金额
	print("****您当前购买的是：",name,"，单价：",price,"元，数量：",count,"件，金额：",round(amount,2),"元！")

	money=float(input("请输入付款金额："))
	if money<amount:
		print("金额不足！")
	else:
		print("****付款",money,"元！找零",round(money-amount,2),"元！")



# round()函数:保留指定的小数位
# a=15.3
# b=3
# c=a/b

# print(round(c,1))
# print(round(3.1415926,5))
