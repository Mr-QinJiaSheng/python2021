import time
import pygame
from pygame.locals import *   #检测事件，如监控键盘按键
import sys
import random


#玩家类：
#属性：显示窗口、位置、图片、子弹列表、移动状态
#方法：显示、移动、开火
class Player():
	def __init__(self,screen):
		self.screen=screen  #将一个窗口对象作为了属性值，表示玩家对象显示的窗口
		self.x=150
		self.y=500
		self.img=pygame.image.load(r"feiji/hero1.png") #玩家图片
		self.bulletList=[]  #子弹列表
		self.moveLeftState=0  #0不移动  1移动
		self.moveRightState=0  #0不移动  1移动

	def display(self):
		self.screen.blit(self.img,(self.x,self.y)) #显示到窗口
		for b in self.bulletList:
			b.display()
			b.move()
			if b.y<0:
				self.bulletList.remove(b)

	def move(self):
		if self.moveLeftState==1 and self.x>-30:
			self.x-=5
		if self.moveRightState==1 and self.x<360:
			self.x+=5
	def fire(self):
		b=PlayerBullet(self.screen,self.x,self.y) 
		self.bulletList.append(b)

#玩家子弹类：
#属性：显示窗口、位置、图片
#方法：显示、移动
class PlayerBullet():
	def __init__(self,screen,x,y):
		self.screen=screen  #将一个窗口对象作为了属性值
		self.x=x+40 #子弹初始位置，需要跟随飞机
		self.y=y-20
		self.img=pygame.image.load(r"feiji/bullet.png") 

	def display(self):
		self.screen.blit(self.img,(self.x,self.y)) #显示到窗口

	def move(self):
		self.y-=20

#敌机类
#属性：显示窗口、位置、图片、子弹列表、移动状态
#方法：显示、移动、开火
class Emeny():
	def __init__(self,screen):
		self.screen=screen  #将一个窗口对象作为了属性值，表示敌机对象显示的窗口
		self.x=0
		self.y=0
		self.img=pygame.image.load(r"feiji/enemy0.png") 
		self.bulletList=[]  #子弹列表
		self.moveState=1  #0左移  1右移

	def display(self):
		self.screen.blit(self.img,(self.x,self.y)) #显示到窗口

		#显示所有子弹
		for b in self.bulletList:#遍历每一个子弹对象，并显示
			b.display()
			b.move()
			#子弹移动到边缘时被清除
			if b.y>=600:
				self.bulletList.remove(b)

	def move(self):
		if self.moveState==1:
			self.x+=5 #向右移动5像素
		elif self.moveState==0:
			self.x-=5 #向左移动5像素

		if self.x<-20: #当敌机移动到边缘时改变方向
			self.moveState=1
		if self.x>280:
			self.moveState=0

	def fire(self): #在子弹列表中增加一个子弹对象
		b=EmenyBullet(self.screen,self.x,self.y) 
		self.bulletList.append(b)

#敌机子弹类
#属性：显示窗口、位置、图片
#方法：显示、移动
class EmenyBullet():
	def __init__(self,screen,x,y):
		self.screen=screen  #将一个窗口对象作为了属性值
		self.x=x+20 #子弹初始位置，需要跟随敌机
		self.y=y+30
		self.img=pygame.image.load(r"feiji/bullet2.png") 

	def display(self):
		self.screen.blit(self.img,(self.x,self.y)) #显示到窗口

	def move(self):
		self.y+=20


#捕捉用户操作
def key_control(player):
	for event in pygame.event.get():
		if event.type==QUIT:
			print("正在退出.....")
			sys.exit(0) #强制退出
		elif event.type==KEYDOWN: #键盘输入
			if event.key==K_LEFT:
				print("玩家向左！")
				player.moveLeftState=1
			if event.key==K_RIGHT:
				print("玩家向右！")
				player.moveRightState=1
			if event.key==K_SPACE: #捕捉空格键
				print("玩家开火！")
				player.fire()
		elif event.type==KEYUP: #键盘释放
			if event.key==K_LEFT: #释放左键
				print("停止向左...")
				player.moveLeftState=0
			if event.key==K_RIGHT: #释放右键
				print("停止向右...")
				player.moveRightState=0


#mian方法
class main():
	screen=pygame.display.set_mode((300,600)) #创建窗口对象

	#获取背景
	background=pygame.image.load(r"feiji/background.png")
	#创建玩家对象，并传入显示窗口
	player=Player(screen)
	#创建敌机对象，并传入显示窗口
	emeny=Emeny(screen)


	#在循环中显示所有对象并刷新
	while 1==1:
		screen.blit(background,(0,0)) #显示背景
		player.display() #显示玩家
		emeny.display() #显示敌机
		emeny.move() #敌机移动
		player.move() #玩家移动
		#敌机随机开火
		r=random.randint(1,10)
		if r==1:
			emeny.fire()
		key_control(player) #捕捉用户操作
		pygame.display.update() #刷新窗口
		time.sleep(0.05)

#---------------------------
if __name__ == '__main__':
	main()