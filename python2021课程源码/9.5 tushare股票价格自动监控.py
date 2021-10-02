# tushare股票价格自动监控
# 需求：设置一只股票卖出和买入价格，程序对价格进行监控，当价格达到预定值时发送邮件提醒---盯盘

import tushare
import time

while 1==1:
	buyPoint=5.2
	salePoint=5.6

	data=tushare.get_realtime_quotes("601398")
	name=data.loc[0][0] #名称
	pre_close=float(data.loc[0][2]) #昨收
	price=float(data.loc[0][3])  #现价
	change=round((price-pre_close)/pre_close,4) #今日涨幅
	msg="股票名称："+name+"，当前价格："+str(price)+"元，涨幅："+str(change*100)+"%"
	print(msg)
	if price<=buyPoint:
		print("价格达到买点！如果空仓请买进！")
		print("邮件发送...")
	elif price>=salePoint:
		print("价格达到卖点！如果持仓请卖出！")
	else:
		print("不要做任何操作！")

	time.sleep(5)

