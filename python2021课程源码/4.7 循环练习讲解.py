# 1.用户输入任意10个数，for循环求他们的平均值；
# total=0
# for x in range(1,6):
# 	num=int(input("请输入"+str(x)+"一个数："))  #input中使用+进行拼接
# 	total+=num
# print(total/5)


#用户输入任意个数，求他们的平均值；
total=0
count=0 #计算循环执行的次数（记录数的个数）
i=1
while i<=3:
	num=int(input("请输入"+str(count+1)+"一个数："))
	total+=num
	count+=1
	msg=int(input("继续输入请按1，结束请按2："))
	if msg==2:
		i=1000 #改变i，让循环结束
print(total,"---",count,"---",total/count)



# # 2.一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8848米）？
# p=0.08
# m=8848000
# count=0 #记录对折次数
# while p<m:
# 	p=p*2 #对折
# 	count+=1
# print(count)




# 3.鸡兔同笼问题：今有鸡兔同笼，上有三十五头，下有九十四足，问鸡兔各几只？
#穷举法：列举所有可能性，找到正确结果
# 鸡 0---35   兔=35-鸡
# for j in range(0,36):
# 	t=35-j
# 	if j*2+t*4==94:
# 		print(j,t)




# 4.我国古代数学家张邱建在《算经》中出了一道“百钱买百鸡”的问题，题意是这样的：
# 5文钱可以买一只公鸡，3文钱可以买一只母鸡，1文钱可以买3只雏鸡。
# 现在用100文钱买100只鸡，那么各有公鸡、母鸡、雏鸡多少只？请编写程序实现。

# #公鸡 0-20  母鸡0-33  雏鸡0-100   
# for g in range(0,21):
# 	for m in range(0,34):
# 		for c in range(0,100,3):
# 			if g+m+c==100 and g*5+m*3+c/3==100:
# 				print(g,m,c)


#雏鸡=100-公鸡-母鸡
for g in range(0,21):
	for m in range(0,34):
		c=100-g-m
		if g+m+c==100 and g*5+m*3+c/3==100:
			print(g,m,c)