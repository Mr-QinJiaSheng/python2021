#break和continue

# break: 结束整个循环操作
# continue:结束本次循环,继续下次循环

for year in range(1,11):
	if year==5:
		print("第5年疫情原因，今年不用还款了！")
		continue
	if year==6:
		print("第",year,"年到了！还款2.4万！")
		continue
	if year==8:
		print("第8年，提前还清，以后都不用还了！")
		break
	print("第",year,"年到了！还款1.2万！")


