import pymysql
import random

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

for x in range(3,13):
	num=x #id
	name=random.choice(["王五","赵六","老七","大宝"])
	age=random.choice([2,13,32,32,32,43,35,43])

	#编写sql  拼接时字符串中的单引号需要加上
	sql="INSERT INTO stu VALUES("+str(num)+",'"+name+"',"+str(age)+");"

	cursor.execute(sql) #执行sql
	db.commit() #提交

#关闭
cursor.close()
db.close() 