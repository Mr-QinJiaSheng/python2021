#数据库操作
import pymysql

host="localhost"
port=3306 
user="root"
password="123456"
dbname="market" #数据库名称
charset="utf8"

#连接数据库
def getConnection():
	db=pymysql.Connect(host=host,port=port,user=user,passwd=password,db=dbname,charset=charset)
	return db

#查询数据
def getData(sql):
	db=getConnection()
	cursor=db.cursor()
	data=None #保存返回数据
	try:
		cursor.execute(sql)
		data=cursor.fetchall()
	except Exception as e:
		print("异常：",e)
	finally:
		cursor.close()
		db.close()
	return data


#更新数据
def writeData(sql):
	db=getConnection()
	cursor=db.cursor()
	r=0
	try:
		r=cursor.execute(sql)
		db.commit()
		print("---------数据已更新！",r)
	except Exception as e:
		print("异常：",e)
	finally:
		cursor.close()
		db.close()
	return r #返回受影响的行数



