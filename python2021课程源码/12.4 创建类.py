#创建对象(实例化)

#猫类
class Cat:
	#初始化方法
	def __init__(self,nick,color,age):
		#属性：昵称，颜色，年龄
		self.nick=nick
		self.color=color
		self.age=age
		self.strain="加菲猫"

	def eat(self): #每个函数中都有固定参数self
		print("猫在吃鱼！")

	def sleep(self):
		print("猫在睡觉！")

#----------------------------------------
# 对象名=类名(属性值1,属性值2,属性值3)
cat1=Cat("小苗","白色",2)
cat2=Cat("小黑","黑色",1)

#1.获取某个对象的属性   对象名.属性名
print(cat1.nick)
print(cat2.strain)


#2.通过某个对象调用方法  对象名.方法名()
cat1.eat()
cat2.sleep()


print(cat2)

