import pymysql

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

#编写sql语句  列名，列数据类型
sql="CREATE TABLE stu(id int,name varchar(10),age int)"

#执行sql
cursor.execute(sql) 

#提交数据
db.commit() 

#关闭游标
cursor.close()

#关闭数据库连接
db.close() 