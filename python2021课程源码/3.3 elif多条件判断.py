#elif多条件判断

money=20
if money>=100: #如果
	print("可以买宝马了！")
	print("真开心！")
elif money>=50:
	print("买丰田！")
elif money>=20:
	print("买二手车！")
elif money>=10:
	print("买电动车！")
else:
	print("共享单车了解一下！")

#if在开头，只有一个，不可省略
#elif可以有任意个
#else只有末尾一个，可以省略
#elif多条件判断中，只执行第一个满足条件的语句


