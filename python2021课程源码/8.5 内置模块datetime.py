#内置模块datetime
import datetime

#获取当前的日期时间
now=datetime.datetime.now()
print(type(now))

#获取一个指定时间
d1=datetime.datetime(2018,2,13,5,23,45)
print(d1)

#日期转字符串
s1=d1.strftime("%Y年-%m月-%d日  %H:%M:%S")
print(s1)

#字符串转日期(格式一定要一致)
s2="2018/02/13 05:23:45"
d2=datetime.datetime.strptime(s2,"%Y/%m/%d %H:%M:%S")
print(d2,type(d2))











