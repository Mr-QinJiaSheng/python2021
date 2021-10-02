# # 1.写函数，接收3个数字参数，返回最大的那个数字。
# def getMax(a,b,c):
# 	r=max([a,b,c]) #在函数中调用函数
# 	return r
# d=getMax(23,56,34)
# print(d)

# # 2.编写一个用户登录函数（用户名密码提前设置）；
# # 返回用户登录成功或者失败的结果；
# name="aaa"
# password="123"
# def login():
# 	msg="失败"
# 	uname=input("请输入用户名：")
# 	upassword=input("请输入密码：")
# 	if name==uname and upassword==password:
# 		print("登录成功！")
# 		msg="成功"
# 	else:
# 		print("失败！！！！")
# 	return msg  #函数一旦执行到return将会停止

# r=login()
# print("登录结果：",r)
  
# 3.做一个分数统计器：
# 函数中让用户循环输入一组分数，输入结束后保存到一个列表中。
# 把平均分，最高分，最低分，及格人数，及格率返回出来。
def getData():
	avgScore=0
	maxScore=0
	minScore=0
	passCount=0
	passPercent=0
	scoreList=[]
	while 1==1:
		s=int(input("------请输入一个分数"))
		scoreList.append(s)
		if s>=60:
			passCount+=1
		c=int(input("结束请按1，继续输入请按2："))
		if c==1:
			break
	avgScore=sum(scoreList)/len(scoreList)
	maxScore=max(scoreList)
	minScore=min(scoreList)
	passPercent=passCount/len(scoreList)

	return avgScore,maxScore,minScore,passCount,passPercent

avgScore,maxScore,minScore,passCount,passPercent=getData()
print("******",avgScore,maxScore,minScore,passCount,passPercent)


