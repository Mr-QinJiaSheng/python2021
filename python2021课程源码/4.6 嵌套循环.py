# #嵌套循环
# for year in range(1,11):
# 	print("----------第",year,"年到了！")
# 	for month in range(1,13):
# 		print("第",year,"年，第",month,"月，还款1000元！")

# print("----",year)


#遍历多维容器
lista=[1,213,13,232,3,43,3,3]
listb=[21,13,243,4,54,6]
listc=[23,545,465,65,6565,76]
listx=[lista,listb,listc]

for x in listx:
	for s in x:
		print(s)
