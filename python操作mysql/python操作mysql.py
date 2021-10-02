import pymysql

#建立连接  注意数据库需要提前创建
db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="123456",db="db2",charset="utf8")

#创建游标对象(用来处理数据库查询结果以及执行sql语句)
cursor=db.cursor()

#定义sql语句
sql="insert into emp values(id,'张三',12,'销售部')"
sql="select * from stu where name='虚竹'"

#执行sql语句
cursor.execute(sql)

#fetchone()查询单行数据 fetchall()查询多行数据
data=cursor.fetchall()
print(data[0][1],data[0][6])

# #更新数据需要提交
# db.commit()

#关闭数据库连接和游标
cursor.close()
db.close()

print("执行成功！")


#报错：1.检查port是不是数字，utf8是不是写成了utf-8
#     2.升级pymysql    python -m pip install --upgrade pymysql