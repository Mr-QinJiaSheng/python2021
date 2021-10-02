#json模拟数据库
#在文本文件中保存json字符，通过文件读写来操作数据
import json

#创建文本文件（数据库文件）
# with open(r"user.txt","w") as f:
# 	users='[{"uname":"zhangsan","upwd":"123"},{"uname":"lisi","upwd":"123"},{"uname":"wangwu","upwd":"123"}]'
# 	f.write(users)

#读数据（查询）
def readData():
	with open(r"user.txt","r") as f:
		jsonData=f.read()
	usersList=json.loads(jsonData)
	return usersList

#写数据（修改）
def writeData(usersList):
	jsonData=json.dumps(usersList,ensure_ascii=False)
	with open(r"user.txt","w") as f:
		f.write(jsonData)
		print("----数据写入成功！")

#登录
def login():
	name=input("请输入用户名：")
	password=input("请输入密码：")
	usersList=readData() #读取所有用户列表
	msg="失败"
	for user in usersList:
		if name==user["uname"] and password==user["upwd"]:
			msg="成功"
			print("----恭喜登陆成功！")
	if msg=="失败":
		print("----登录失败！")
	return msg


#注册（在数据库中增加用户）
def reg():
	name=input("请输入新用户名：")
	password=input("请输入密码：")
	newuser={"uname":name,"upwd":password} #新用户
	usersList=readData()
	usersList.append(newuser) #将新用户添加到用户列表
	writeData(usersList)
	print("-----新用户添加成功！")

#-------------------------
if __name__ == '__main__':
	login()