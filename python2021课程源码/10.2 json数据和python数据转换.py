#json数据和python数据转换
import json


#保存一个学员信息
stu1='{"name":"zhangsan","age":18,"hobby":"play"}'

#保存多个学员信息
stus='[\
{"name":"zhangsan","age":18,"hobby":"play"},\
{"name":"lisi","age":15,"hobby":"sleep"},\
{"name":"wangwu","age":17,"hobby":"eat"}\
]'


#1.json转python（转成字典或者列表嵌套字典）
jsonData='{"name":"zhangsan","age":18,"hobby":"play"}'
pythonData=json.loads(jsonData)
# print(pythonData["hobby"])

#2.python转json
pythonData={"cname":"1001","cpwd":"123","cbalance":1000,"name":"张三"}
# r=str(pythonData) #XXXXXXX错误
josnData=json.dumps(pythonData,ensure_ascii=False) #ensure_ascii=False 禁止ascii转换
print(josnData,type(josnData)) 

