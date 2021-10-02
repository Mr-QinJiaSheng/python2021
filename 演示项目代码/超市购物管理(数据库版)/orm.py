#pymysql
import pymysql

host="localhost" #主机地址
port=3306 #端口号
user='root' #用户名
passwd="123456" #密码
dbName="db3" #数据库名称
charset="utf8" #编码

#数据库连接
def getConnection():
	db=pymysql.Connect(host=host,port=port,user=user,passwd=passwd,db=dbName,charset=charset)
	return db

#查询数据
def getData(sql):
	db=getConnection()
	cursor=db.cursor()
	data=None
	try:
		cursor.execute(sql)
		data=cursor.fetchall() #获取多条结果
	except Exception as e:
		print("发生错误：",e)
	finally:
		#5.关闭数据库连接和游标
		cursor.close()
		db.close()
	return data

#写入数据
def writeData(sql):
	db=getConnection()
	cursor=db.cursor()
	result=None
	try:
		result=cursor.execute(sql)
		db.commit() #更新操作时需要提交
		print("----数据已更新！",result)
	except Exception as e:
		print("发生错误：",e)
	finally:
		#5.关闭数据库连接和游标
		cursor.close()
		db.close()
	return result