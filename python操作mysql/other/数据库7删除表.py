import pymysql

#建立连接
db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="123456a",db="pythondb",charset="utf8")

#创建游标对象(用来处理数据库查询结果以及执行sql语句)
cursor=db.cursor()

#定义sql语句 这里id是自增列，添加时直接用id
sql='''
	drop table emp;

'''

#执行sql语句
cursor.execute(sql)

#关闭数据库连接和游标
cursor.close()
db.close()