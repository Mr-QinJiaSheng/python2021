# with open()语法
# with open(r"G:\python教程2021\python2021资料和练习\file\再别康桥.txt","r") as file:
# 	data=file.read()
# 	print(data)

#文件复制
with open(r"G:\python教程2021\python2021资料和练习\file\aaa\cat.jpg","rb") as file1,open(r"G:\python教程2021\python2021资料和练习\file\bbb\cat-2.jpg","wb") as file2:
	data=file1.read()
	file2.write(data)


