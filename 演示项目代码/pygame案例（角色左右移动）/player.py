# ***下载：
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pygame
import pygame
import time
import sys
from pygame.locals import *   #检测事件，如监控键盘按键


####2
while 1==1:
	a=10 #x轴位置 10-300之间左右移动
	b=100 #y轴位置
	for x in range(60):
		# 1.创建窗口   窗口尺寸
		screen=pygame.display.set_mode((400,300)) 
		# 2.读取本地图片
		img1=pygame.image.load("background.jpg") 
		img2=pygame.image.load("player.png") 
		# 3.在窗口中加入对象   (0,0)显示的位置
		screen.blit(img1,(0,0)) 
		screen.blit(img2,(a,b)) 
		# 4.刷新窗口，显示窗口中所有对象
		pygame.display.update()
		time.sleep(0.1)

		#来回改变x值
		if x<=30:
			a+=10
		else:
			a-=10

		#监控键盘输入退出
		for event in pygame.event.get(): #遍历所有用户输入事件
			if event.type==QUIT: #捕捉退出按钮
				print("正在退出....")
				sys.exit(0)

