import pymysql

#建立连接
db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="123456",db="db2",charset="utf8")

#创建游标对象(用来处理数据库查询结果以及执行sql语句)
cursor=db.cursor()

i=5
#定义sql语句 这里id是自增列，添加时直接用id
sql="select * from stu;"

#执行sql语句
cursor.execute(sql)

#查询数据需要用游标定义的一些方法  fetchone()查询单行数据 fetchall()查询多行数据
# data1=cursor.fetchone()
# print(type(data1),data1)

data2=cursor.fetchall()
print(data2)
#关闭数据库连接和游标
cursor.close()
db.close()


#报错：1.检查port是不是数字，utf8是不是写成了utf-8
#     2.升级pymysql    python -m pip install --upgrade pymysql