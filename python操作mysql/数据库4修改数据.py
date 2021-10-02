import pymysql

#建立连接
db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="123456a",db="pythondb",charset="utf8")

#创建游标对象(用来处理数据库查询结果以及执行sql语句)
cursor=db.cursor()

#定义sql语句 这里id是自增列，添加时直接用id
sql='''
	update emp set name='张三' where name='lisi';
'''

#执行sql语句
cursor.execute(sql)

#增加修改数据需要提交
db.commit()

#关闭数据库连接和游标
cursor.close()
db.close()


#报错：1.检查port是不是数字，utf8是不是写成了utf-8
#     2.升级pymysql    python -m pip install --upgrade pymysql