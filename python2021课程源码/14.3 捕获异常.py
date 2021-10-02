# try:
# 	可能出现异常的代码
# except Exception as e:
# 	出现异常时执行的代码

lista=[12,12,12,323,24,0,43,43,54,0,56,565,65,56]
for s in lista:
	try:
		r=10/s
		print(r)
	except Exception as e:   #Exception 捕获的错误类型  e保存具体错误内容
		print("出现错误：",e)

