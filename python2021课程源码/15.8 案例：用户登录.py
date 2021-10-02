import pymysql
import random

def getData(sql):
	#需要先创建一个数据库，才能连接
	host="localhost"
	port=3306 #注意使用数字
	user="root"
	password="123456"
	db="51db" #数据库名称
	charset="utf8"

	#创建数据库连接对象，并建立连接
	db=pymysql.Connect(host=host,port=port,user=user,passwd=password,db=db,charset=charset)
	print("数据库已连接.....")
	#创建游标对象(1.执行sql语句，2.处理数据查询结果)
	cursor=db.cursor()
	cursor.execute(sql) #执行sql
	data=cursor.fetchone() #获取一行数

	#关闭
	cursor.close()
	db.close() 

	return data

#登录
def login():
	uname=input("请输入用户名：")
	upwd=input("请输入密码：")
	sql="SELECT * FROM users WHERE username='"+uname+"' and password='"+upwd+"'"
	data=getData(sql)
	if data==None:
		print("失败！")
	else:
		print("成功！")


#
if __name__ == '__main__':
	login()