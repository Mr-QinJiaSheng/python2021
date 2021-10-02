import pymysql

#建立连接
db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="123456a",db="pythondb",charset="utf8")

#创建游标对象(用来处理数据库查询结果以及执行sql语句)
cursor=db.cursor()

#外部待拼接参数 这里要注意统一使用字符串
idd="2"
name="张三"


#定义sql语句 这里id是自增列，添加时直接用id
sql='''
	select * from emp where id=(%s) && name=(%s);
'''

#执行sql语句
cursor.execute(sql,[idd,name]) #拼接了外部数据到sql

#查询数据
data2=cursor.fetchall()
print(type(data2),data2)


#关闭数据库连接和游标
cursor.close()
db.close()


#报错：1.检查port是不是数字，utf8是不是写成了utf-8
#     2.升级pymysql    python -m pip install --upgrade pymysql