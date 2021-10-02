#编写业务方法
import orm
import random

#查看商品列表
def getAllProducts():
	sql="SELECT * FROM products;"
	data=orm.getData(sql)
	print("序号    编号    名称    单价   折扣")
	for product in data:
		for x in product:
			print(x,end="    ")
		print()

#根据编号查询商品
def getProduct():
	num=input("请输入商品编号：")
	sql="SELECT * FROM products WHERE num="+num+";"
	data=orm.getData(sql)
	if data!=None:
		print("-----商品名称：",data[0][2],"单价：",data[0][3],"折扣：",data[0][4])
		return data[0][2],data[0][3],data[0][4]
	else:
		print("-----商品不存在！")
		return None

#添加商品
def addProduct():
	name=input("请输入商品名称：")
	num=str(random.randint(1000,9999))
	price=input("请输入商品价格：")
	sql="INSERT INTO products(num,name,price,discount) VALUES("+num+",'"+name+"',"+price+",1);"
	r=orm.writeData(sql)
	print(r)

#根据编号删除商品
def delProduct():
	num=input("请输入商品编号：")
	sql="DELETE FROM products WHERE num="+num+";"
	r=orm.writeData(sql)
	if r==0:
		print("删除失败！")
	else:
		print("商品",num,"已删除！")

#商品打折（修改折扣）
def setDiscount():
	num=input("请输入要修改的商品编号：")
	discount=float(input("请输入设置的折扣："))
	if 0.1<=discount<=1:
		sql="UPDATE products SET discount="+str(discount)+" WHERE num="+num+";"
		r=orm.writeData(sql)
		if r==0:
			print("设置失败！")
		else:
			print("商品",num,"折扣设置成功！")
	else:
		print("折扣输入错误！")



# 查看所有订单；
def getAllOrders():
	sql="SELECT * FROM orders;"
	data=orm.getData(sql)
	print("序号    编号    数量    金额")
	for order in data:
		for x in order:
			print(x,end="    ")
		print()

# 删除订单；（通过订单号删除）
def delOrder():
	num=input("请输入订单编号：")
	sql="DELETE FROM orders WHERE num="+num+";"
	r=orm.writeData(sql)
	if r==0:
		print("删除失败！")
	else:
		print("订单",num,"已删除！")

# 订单统计(总销量，销售额)；	
def accordOrder():
	sql="SELECT * FROM orders;"
	data=orm.getData(sql)
	totalCount=0
	totalAmount=0
	for order in data:
		totalCount+=order[2]
		totalAmount+=order[3]
	print("总销量",totalCount,"件！，销售额",totalAmount,"元！")

#商品结算
def settle():
	orderCount=0
	orderAmount=0
	msg=0 #保存订单是否有效
	while 1==1:
		data=getProduct()
		num=int(input("请输入商品数量："))
		if data!=None:
			msg=1
			price=data[1]
			discount=data[2]
			amount=price*num*discount
			orderCount+=num
			orderAmount+=amount
			print("当前添加",num,"件！金额",amount,"元！")
		r=input("继续添加请输入1，结算请输入2：")
		if r=="1":
			continue
		else:
			print("--------------------------------------")
			break
	print("****您购买的总数量",orderCount,"件！总金额",orderAmount,"元！")

	#添加订单
	if msg==1:
		oid=str(random.randint(1000,9999))
		sql="INSERT INTO orders(num,count,amount) VALUES("+oid+","+str(orderCount)+","+str(orderAmount)+"); "
		orm.writeData(sql)
		print("--------添加成功！")
#----------------------------------------