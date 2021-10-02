#for循环

# for 变量名 in 序列:
# 	循环语句

#执行次数=序列中元素的个数
# for s in range(1,11):
# 	print("第",s,"次打印hello world!")

# #步长
# for s in range(1,101,4):
# 	print(s)

# #range(开始值,结束值（不包含）,步长)

# for x in ["a","b","c"]:
# 	print(x)


#1.循环操作是什么？
#2.循环的次数


#求和问题
#大宝买车时，贷款12万，分10年还清
# totalMoney=0  #保存累计还款金额
# for year in range(1,11):
# 	totalMoney=totalMoney+1.2
# 	print("第",year,"年到了！还款1.2万！累计已还",round(totalMoney,2),"万！还剩",round(12-totalMoney,2),"万！")



#1-100之间所有数的和
t=0
for x in range(1,101):
	t=t+x
	print(x)
print(t)