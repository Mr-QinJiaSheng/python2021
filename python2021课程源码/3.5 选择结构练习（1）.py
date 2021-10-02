
# #选择结构练习

# 1.星期一特价菜：水煮鱼
#   星期二特价菜：烧排骨
#   星期三，四特价菜：宫爆鸡丁
#   星期五，六特价菜：清蒸鲈鱼
#   其它：干锅肥肠
# 根据用户输入星期几，输出特价菜是什么？

# day=int(input("你周几过来吃饭呢（1-7）？"))
# if day==1:
# 	print("特价菜：水煮鱼！")
# elif day==2:
# 	print("特价菜：烧排骨！")
# elif day==3 or day==4:
# 	print("特价菜：宫爆鸡丁！")
# elif day==5 or day==6:
# 	print("特价菜：清蒸鲈鱼！")
# else:
# 	print("特价菜：干锅肥肠！")


# 2.根据输入判断学生的成绩等级，
# 如果成绩>=90分，则输出“优秀”;
# 如果成绩>=80分，则输出“良好”;
# 如果成绩>=60分，则输出“中等”;
# 否则，输出“差”

# score=int(input("请输入学生分数："))
# if score>=90:
# 	print("优秀！")
# elif score>=80:
# 	print("良好！")
# elif score>=60:
# 	print("中等！")
# else:
# 	print("太差了！")


# 3.现在有一个银行保险柜，有两道密码。想拿到里面的钱必须两次输入的密码都要正确。
# 如果第一道密码都不正确，那直接把你拦在外面；
# 如果第一道密码输入正确，才能有权输入第二道密码。
# 只有当第二道密码也输入正确，才能拿到钱！(两道密码自己设)(嵌套if)

# password1="123"
# password2="abc"

# pwd1=input("请输入第一道密码：")
# if pwd1==password1:
# 	print("第一道密码输入正确！")
# 	pwd2=input("请输入第二道密码：")
# 	if pwd2==password2:
# 		print("恭喜你，输入正确！拿到5毛钱！")
# 	else:
# 		print("很遗憾！第二道密码错误！")
# else:
# 	print("第一道密码输入错误，请出去吧！")



# 4.开发一个计算器，用户输入第一个数、加减乘除、第二个数，控制台显示计算结果。

a=int(input("请输入第一个数："))
b=int(input("请输入第二个数："))
s=input("请输入计算方式（+ - * /）：")
result=0  #保存计算结果
msg=1  #记录是否有结果  1有结果  0没结果
if s=="+":
	result=a+b
elif s=="-":
	result=a-b
elif s=="*":
	result=a*b
elif s=="/":
	result=a/b
else:
	print("没有这个计算方式！")
	msg=0
	
if msg==1:
	print("计算结果：",result)


