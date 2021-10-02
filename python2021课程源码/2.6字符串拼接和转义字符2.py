#字符串拼接
#+拼接时，需要保证每一个子字符串必须都是字符串类型
# a1="张三"
# a2="李四"
# c=a1+"爱"+a2
# print(c)

#format函数拼接
# s1="hello!{}{}{}".format("张三","李四",666)
# s2="hello!{0}{1}{2}".format("张三","李四",666)
# s3="hello!{a}{b}{c}".format(a="张三",b="李四",c=666)
# print(s3)


# a1="张三"
# a2="李四"
# a3="王五"
# print(a1+a2+a3)
# print(a1,a2,a3,6) #分别打印多个内容,没有拼接



#转义字符
#字符串中一些表达特殊意义的字符
# s1="这是第一行！\n这是第二行！"   #\n换行符
# s2="你是谁？ \t\t\t\t离我远点！"  #\t制表符
# print(s2)

#取消转义 文件路径 网址
s1=r"C:\Users\mango\Desktop\python代码\test"
s1="C:\\Users\\mango\\Desktop\\python代码\\test" #双重转义=不转义
print(s)