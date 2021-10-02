#读文件
f=r"G:\python教程2021\python2021资料和练习\file\再别康桥.txt"  #不要忘记加r
file=open(f,"r")  #open(文件路径名，访问模式)  r---read读文件
data=file.read()
file.close() #关闭文件资源


print(data)
print(type(data))
