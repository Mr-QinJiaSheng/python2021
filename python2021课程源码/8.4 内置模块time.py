#内置模块time
import time

# #获取一个时间戳：当前时间距离1970年元旦0时的秒数
# s1=time.time() 
# for x in range(1,10001):
# 	print(x)
# s2=time.time() 
# print(s2-s1)

#获取当前本地的日期和时间
t=time.localtime()

#将日期和时间转换成指定格式的字符串
strtime=time.strftime("%Y年-%m月-%d日----%H:%M:%S",t)
# print(strtime)


# #程序休眠
# time.sleep(5*60*60)
# print("hello")


#倒计时
i=10
while i>=0:
	print("倒计时：",i)
	time.sleep(1)
	i-=1




