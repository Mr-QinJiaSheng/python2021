import json
import time
import datetime

# #写入初始数据 记得要使用程序编写，否则可能会报编码错误
# d='[{"时间": "2021/03/04 15:20:21", "项目": "收到王敏货款", "金额": 20000, "分类": "收入"}]'
# with open(r"data.txt","w") as f:
# 		f.write(d)

#读json数据
def readData():
	with open(r"data.txt","r") as f:
		jsonData=f.read()
	dataList=json.loads(jsonData)
	return dataList

#写json数据
def writeData(dataList):
	jsonData=json.dumps(dataList,ensure_ascii=False)
	with open(r"data.txt","w") as f:
		jsonData=f.write(jsonData)
		print("-----数据写入成功！")

def showData():
	sumin=0
	sumout=0
	dataList=readData()
	print("**********************账单**********************")
	for data in dataList:
		if data["分类"]=="收入":
			sumin+=data["金额"]
			print(data["时间"],"  ",data["项目"],"  ",data["金额"],"元")
		else:
			sumout+=data["金额"]
			print(data["时间"],"  ",data["项目"],"  ",data["金额"]*-1,"元")
	print("************************************************")
	print("-----总收入：",sumin,"元，总支出:",sumout,"元，结余:",sumin-sumout,"元！")

def addData():
	dataList=readData()
	content=input("请输入项目明细：")
	amount=float(input("请输入金额："))
	cla="支出"
	c=int(input("请选择（1.收入  2.支出）："))
	if c==1:
		cla="收入"
	t=datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	data={"时间":t,"项目":content,"金额":amount,"分类":cla}
	dataList.append(data)
	writeData(dataList)


if __name__ == '__main__':
	while 1==1:
		showData()
		c=int(input("增加新账目请输入1："))
		if c==1:
			addData()
		time.sleep(2)
		print("\n\n\n")
	