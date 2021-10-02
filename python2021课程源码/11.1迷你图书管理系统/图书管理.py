import json
import datetime
import time

# #写入初始数据 
# d1='[{"用户名": "admin", "密码": "123", "姓名": "张三"},{"用户名": "aaa", "密码": "123", "姓名": "李四"}]'
# with open(r"users.txt","w") as f:
# 		f.write(d1)

# d2='[{"编号":1001, "书名": "<红楼梦>", "作者": "曹雪芹", "借出状态": "可借"},\
# {"编号":1002, "书名": "<java教程>","作者": "齐一天", "借出状态": "可借"},\
# {"编号":1003, "书名": "<圣经>","作者": "耶稣", "借出状态": "已借出"},\
# {"编号":1004, "书名": "<李白诗集>","作者": "李白", "借出状态": "可借"},\
# ]'
# with open(r"books.txt","w") as f:
# 		f.write(d2)


#读json数据
def readUsers():
	with open(r"users.txt","r") as f:
		jsonData=f.read()
	dataList=json.loads(jsonData)
	return dataList

def readData():
	with open(r"books.txt","r") as f:
		jsonData=f.read()
	dataList=json.loads(jsonData)
	return dataList

#写json数据
def writeData(dataList):
	jsonData=json.dumps(dataList,ensure_ascii=False)
	with open(r"books.txt","w") as f:
		f.write(jsonData)
		print("------数据写入成功！")


# 1.用户登录；login()
def login():
	msg="失败"
	usersList=readUsers()
	name=input("请输入用户名：")
	pwd=input("请输入密码：")
	for user in usersList:
		if name==user["用户名"] and pwd==user["密码"]:
			print("---恭喜你登陆成功！",user["姓名"],"！")
			msg="成功"
			break
	if msg=="失败":
		print("-----验证失败！")
	return msg


# 2.显示图书列表；showAllBooks()
def showAllBooks():
	booksList=readData()
	print("-----------------------------------------")
	for book in booksList:
		print(book["编号"],"  ",book["书名"],"  ",book["作者"],"  ",book["借出状态"])
	print("-----------------------------------------")

# 3.图书上架；addBook()
def addBook():
	booksList=readData()
	numList=[]
	for book in booksList:
		numList.append(book["编号"])
	newNum=max(numList)+1
	bookName=input("请输入图书名：")
	bookName="<"+bookName+">"
	author=input("请输入作者：")
	state="可借"
	newBook={"编号":newNum, "书名":bookName,"作者":author, "借出状态":state}
	booksList.append(newBook)
	writeData(booksList)

# 4.图书下架；delBook()
def delBook():
	booksList=readData()
	data1=input("请输入要下架的图书名称：")
	data2=int(input("请输入要下架的图书编号："))
	for book in booksList:
		if data2==book["编号"] or data1==book["书名"]:
			booksList.remove(book) #删除图书信息
			print("-----图书",book["书名"],"已下架！")
	writeData(booksList)

# 5.借书；lendBook()
def lendBook():
	booksList=readData()
	num=int(input("请输入要借的图书编号："))
	msg=0  #0没有
	for book in booksList:
		if num==book["编号"]:
			msg=2
			if book["借出状态"]=="可借":
				print("----您已成功借出图书：",book["书名"],"！")
				book["借出状态"]="已借出"
				writeData(booksList)
			else:
				print("----",book["书名"],"已经借出！下次再来吧！")
	if msg==0:
		print("-----没有此图书！")

# 6.还书；returnBook()
def returnBook():
	booksList=readData()
	num=int(input("请输入要归还的图书编号："))
	msg=0  #0没有
	for book in booksList:
		if num==book["编号"]:
			msg=2
			if book["借出状态"]=="已借出":
				print("----成功归还图书",book["书名"],"!")
				book["借出状态"]="可借"
				writeData(booksList)
			else:
				print("---该图书不允许归还！")
	if msg==0:
		print("-----没有此图书！")


#---主函数
def main():
	print("***********************图书管理系统1.0*************************")
	msg=login()
	# msg="成功"
	if msg=="成功":
		while 1==1:
			print("1.显示所有图书；\n2.图书上架；\n3.图书下架；\n4.借书；\n5.还书。")
			print("*************************************************************")
			c=int(input("请输入业务编号（1-5）："))
			if c==1:
				showAllBooks()
			elif c==2:
				addBook()
				showAllBooks()
			elif c==3:
				delBook()
				showAllBooks()
			elif c==4:
				lendBook()
				showAllBooks()
			elif c==5:
				returnBook()
				showAllBooks()
			else:
				print("没有此业务！")

#---
if __name__ == '__main__':
	main()




	