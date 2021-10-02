import orm
import random

#商品结算
def settle():
	mName="非会员"
	mConpon=0
	mid=int(input("请输入会员编号："))
	#查询会员信息
	member=orm.getData("select * from members where mid="+str(mid)+";")
	if member!=None: #判断会员是否存在
		if len(member)>0:
			mName=member[0][2]
			mConpon=float(member[0][4])
	print("-------",mName,",欢迎你！")

	totalAmount=0 #总金额
	totalCount=0  #总数量
	#循环添加商品
	while 1==1:
		gid=int(input("请输入商品编号："))
		gCount=int(input("请输入数量："))
		gName=None
		gPrice=0
		gDiscount=0
		msg=0 #记录商品是否存在
		good=orm.getData("select * from goods where gid="+str(gid)+";")
		if good!=None: #判断商品是否存在
			if len(good)>0:
				gid=good[0][1]
				gName=good[0][2]
				gPrice=good[0][3]
				gDiscount=good[0][4]
				msg=1
		if msg==0:
			print("商品不存在，请重新输入！")
			continue
		else:
			amount=gCount*float(gPrice)*float(gDiscount) #单个商品金额
			print("--您当前添加的是：",gName,"单价：",gPrice,"元，金额：",amount,"元！")
			totalAmount+=amount #总金额
			totalCount+=gCount  #总数量
		choice=input("结算请输入1，输入其他内容继续添加商品：")
		if choice=="1":
			break
		else:
			continue
	
	print("*******您当前共添加了",totalCount,"件商品，总金额",totalAmount,"元！")
	#优惠券处理
	money=0 #减掉的钱
	if mConpon>=totalAmount:
		money=totalAmount
		totalAmount=0
	else:
		totalAmount-=mConpon
		money=mConpon
	print("*******使用优惠券减掉",money,"元！实际金额",totalAmount,"元！")
	#在会员账户上减掉优惠券
	sql="update members set coupon=coupon-"+str(money)+" where mid="+str(mid)+";"
	orm.writeData(sql)

	#添加订单
	oid="" #订单号
	for x in range(10):
		oid+=str(random.randint(1,9))
	print("订单号：",oid)
	sql="insert into orders(oid,count,mname,amount) values('"+oid+"',"+str(totalCount)+",'"+mName+"',"+str(totalAmount)+")"
	orm.writeData(sql)

# 查看所有订单；
def getAllOrders():
	pass

# 删除订单；（通过订单号删除）
def delOrder():
	pass

# 统计会员购物比例；	
def getMemberPercent():
	pass

# 幸运抽奖；（5%几率一等奖，10%几率2等奖，15%几率三等奖，奖品自由设置）
def bonus():
	pass


# 优惠券发放；(选择2元，5元，10元优惠券，发放到会员账上)
def setCoupon():
	pass

# 会员注册；
def addMember():
	pass

# 会员注销；
def delMember():
	pass


#----------------------------------------
