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

#编写sql  
# sql="SELECT salary FROM emps WHERE name='王五';"
# sql="SELECT * FROM emps WHERE name='王五';"
sql="SELECT * FROM emps;"

cursor.execute(sql) #执行sql
# db.commit() #提交(只在更新操作中使用)

# data=cursor.fetchone() #获取一行数据
data=cursor.fetchall() #获取多行数据
print(data)


#关闭
cursor.close()
db.close() 