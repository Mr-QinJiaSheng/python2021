#创建对象

#猫类
class Cat:

	def __init__(self,nick,color,age):
		self.nick=nick
		self.color=color
		self.age=age
		self.strain="加菲猫"

	def eat(self): 
		print("猫在吃鱼！")

	def sleep(self):
		print("猫在睡觉！")

#----------------------------------------
cat1=Cat("小苗","白色",2)
cat2=Cat("小黑","黑色",1)


cat1.age=3 #给对象的属性重新赋值
cat2.eat(3)

