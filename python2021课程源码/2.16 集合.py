#集合set
#特性：无序；元素不重复；集合本质上是只有键的字典
seta={21,232,33,43,13,33,22,22,"hello"}
# print(seta)


#去重
lista=[1,2,1,1323,2121,2,32323,23,23,23]
seta=set(lista) #将其他序列转换成set
newList=list(seta) #将其他序列转换成list
# print(newList)


#集合运算
seta={1,2,3,4,5,6}
setb={7,8,9,4,5,6}
print(seta&setb) #获取交集
print(seta|setb) #获取并集
print(seta-setb) #获取差集
