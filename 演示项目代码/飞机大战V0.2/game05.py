import time
import pygame
from pygame.locals import *   #检测事件，如监控键盘按键
import sys
import random


#玩家类
class Player():
	def __init__(self,screen):
		self.screen = screen #显示的窗口
		self.x = 150 #显示的位置
		self.y = 500
		self.image=pygame.image.load(r"feiji/hero1.png") #设置玩家飞机图片
		self.bullet_list=[]  #玩家子弹列表
		self.moveleftstate=0 # 记录玩家飞机左右移动状态 0代表不移动 1代表移动
		self.moverightstate=0

	def display(self,emeny): #将敌机对象传递进来方便比对位置
		self.screen.blit(self.image,(self.x,self.y)) #在窗口中添加玩家飞机  （图片，（位置））
		#显示子弹
		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()
			#敌机坠毁过程
			if emeny.x-20<bullet.x<emeny.x+20 and bullet.y==emeny.y:
				print("击中敌机！！！！！！！！！！")
				emeny.count+=1
				if emeny.count==1:
					emeny.image=pygame.image.load(r"feiji/enemy0_down1.png")
				elif emeny.count==2:
					emeny.image=pygame.image.load(r"feiji/enemy0_down2.png")
				elif emeny.count==3:
					emeny.x=0
					emeny.y=0
					emeny.image=pygame.image.load(r"feiji/enemy0.png")
					emeny.count=0			
	def move(self):
		if self.moveleftstate==1 and self.x>=-50:
			self.x=self.x-5
		if self.moverightstate==1 and self.x<=430:
			self.x=self.x+5

	def fire(self):
		bullet=PlayerBullet(self.screen,self.x,self.y)
		self.bullet_list.append(bullet)

#玩家子弹类
class PlayerBullet():
	def __init__(self,screen,x,y):
		self.screen = screen #显示的窗口
		self.x = x+40 #显示的位置
		self.y = y-20
		self.image=pygame.image.load(r"feiji/bullet.png") #设置子弹图片
 
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

	def move(self):
		self.y=self.y-20
#敌机类
class Emeny():
	def __init__(self,screen):
		self.screen = screen #显示的窗口
		self.x = 0 #显示的位置
		self.y = 0
		self.image=pygame.image.load(r"feiji/enemy0.png") 
		self.bullet_list=[]  #子弹列表
		self.movestate=2 # 记录飞机左右移动状态 0代表不移动 1代左移动  2代表右移动
		self.count=0  #记录敌机被击中的次数

	def display(self):
		self.screen.blit(self.image,(self.x,self.y)) #在窗口中添加飞机  （图片，（位置））
		#显示子弹
		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()

	def move(self):
		if self.movestate==1:
			self.x=self.x-5
		elif self.movestate==2:
			self.x=self.x+5

		if self.x<0: #移动至边缘改变方向
			self.movestate=2
		elif self.x>300:
			self.movestate=1
	
	def fire(self):
		bullet=EmenyBullet(self.screen,self.x,self.y)
		self.bullet_list.append(bullet)
#敌机子弹类
class EmenyBullet():
	def __init__(self,screen,x,y):
		self.screen = screen #显示的窗口
		self.x = x+23 #显示的位置
		self.y = y+32
		self.image=pygame.image.load(r"feiji/bullet1.png") #设置子弹图片
 
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

	def move(self):
		self.y=self.y+20
#键盘控制
def key_control(player):
	for event in pygame.event.get():
		if event.type==QUIT: #捕捉用户退出窗口
			print("退出游戏....")
			sys.exit(0) #强制退出游戏
		elif event.type==KEYDOWN:#捕捉用户键盘输入
			if event.key==K_a or event.key==K_LEFT:
				print("玩家向左！")
				player.moveleftstate=1
			if event.key==K_d or event.key==K_RIGHT:
					print("玩家向右！")
					player.moverightstate=1
			if event.key==K_SPACE:
				print("玩家开火！")
				player.fire()
		elif event.type==KEYUP: #捕捉键盘释放
			if event.key==K_a or event.key==K_LEFT:
				player.moveleftstate=0
			if event.key==K_d or event.key==K_RIGHT:
				player.moverightstate=0

#mian方法
def main():
	screen=pygame.display.set_mode((300,600))#创建窗口  参数：窗口像素大小
	background=pygame.image.load(r"feiji/background.png")#创建背景对象
	player=Player(screen) #创建玩家对象
	emeny=Emeny(screen) #创建敌机对象
	while 1==1:
		screen.blit(background,(0,0)) #在窗口中添加背景  (背景图片显示的位置)
		player.display(emeny) #显示玩家
		emeny.display()  #显示敌机
		player.move()    #玩家移动
		emeny.move()    #敌机移动
		r=random.randint(1,10)
		if r<=2:
			emeny.fire() #敌机随机开火
		pygame.display.update() #刷新窗口，显示窗口中所有对象
		key_control(player) #键盘控制
		time.sleep(0.05)

####
if __name__ == '__main__':
	main()

