#字典 dict
#键:值
#特性：无序；键值对形式；键不可以重复，一般使用字符串作为键
dicta={"name":"zhangsan","age":18,"hobby":"playBall"}

#使用键来获取值
# print(dicta["hobby"])
# print(dicta["name"])
# print(dicta["age"])

#修改字典的值
dicta={"name":"zhangsan","age":18,"hobby":"playBall"}
dicta["hobby"]="看书"
# print(dicta)

#增加数据---给一个原本不存在的键赋值
dicta["sex"]="男"
# print(dicta)

#删除数据
dicta.pop("hobby")
# print(dicta)

#判断一个键是否存在
print("money" in dicta)