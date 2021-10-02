# 案例1：
# 为一家超市开发一个简易的收银系统(以3-5种商品为例): 
# 使用变量保存：商品编号 商品价格 商品名字

# 1.提示用户输入商品编号和数量,然后显示总价多少钱。
# 2.提示用户输入付款金额,然后显示找零金额。

num1="1001"
price1=7
name1="苹果"

num2="1002"
price2=4
name2="香蕉"

num3="1003"
price3=5
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
	print("****您当前购买的是：",name,"，单价：",price,"元，数量：",count,"件，金额：",amount,"元！")

	money=float(input("请输入付款金额："))
	if money<amount:
		print("金额不足！")
	else:
		print("****付款",money,"元！找零",money-amount,"元！")

