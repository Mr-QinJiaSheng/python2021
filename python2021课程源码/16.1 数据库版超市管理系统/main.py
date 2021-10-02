#调用
import market


def main():
	print("***********************超市管理系统*************************")
	print("***********************1.查看商品列表")
	print("***********************2.根据编号查询商品")
	print("***********************3.添加商品")
	print("***********************4.根据编号删除商品")
	print("***********************5.商品打折")
	print("***********************6.查看所有订单")
	print("***********************7.删除订单")
	print("***********************8.订单统计")
	print("***********************9.商品结算")
	print("***********************10.退出")
	print("***********************************************************")
	c=int(input("请选择："))
	if c==1:
		market.getAllProducts()
	elif c==2:
		market.getProduct()
	elif c==3:
		market.addProduct()
	elif c==4:
		market.delProduct()
	elif c==5:
		market.setDiscount()
	elif c==6:
		market.getAllOrders()
	elif c==7:
		market.delOrder()
	elif c==8:
		market.accordOrder()
	elif c==9:
		market.settle()
	else:
		print("***********************************************************")

	

if __name__ == '__main__':
	main()