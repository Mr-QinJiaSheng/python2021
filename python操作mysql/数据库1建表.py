import pymysql
#建立连接  注意数据库需要提前创建
db=pymysql.Connect(host="localhost",port=3306,
					user="root",passwd="123456",
	                db="51db",charset="utf8")
cursor=db.cursor()#创建游标对象(用来处理数据库查询结果以及执行sql语句)

sql="CREATE TABLE test(id int,name varchar(10),age int);"

cursor.execute(sql)  #执行sql语句
db.commit()#增加修改数据需要提交

#关闭数据库连接和游标
cursor.close()
db.close()


#报错：1.检查port是不是数字，utf8是不是写成了utf-8
#     2.升级pymysql    python -m pip install --upgrade pymysql