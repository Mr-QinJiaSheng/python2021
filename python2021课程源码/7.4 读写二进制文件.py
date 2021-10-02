#写文件
#如果文件不存在，则创建新文件  如果存在，则覆盖写入
#问价路径必须已经存在
# s="你好，武汉！"
# file=open(r"G:\python教程2021\python2021资料和练习\file\hello0402.txt","w")   #w---write写
# file.write(s)
# file.close()


# 文本文件：r w a
# 二进制文件:rb wb ab

#读文件
file1=open(r"G:\python教程2021\python2021资料和练习\file\aaa\cat.jpg","rb")
data=file1.read()
file1.close()

#写文件
file2=open(r"G:\python教程2021\python2021资料和练习\file\bbb\cat_b.jpg","wb")
file2.write(data)
file2.close()