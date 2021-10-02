#python连接数据库
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

#.......


#
db.close() #关闭数据库连接