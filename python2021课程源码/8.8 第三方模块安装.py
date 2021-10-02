from PIL import Image  #PIL(pillow) 图片处理模块

img = Image.open(r"C:\Users\mango\Desktop\python代码\file\aaa\cat.jpg")   # 读取图片
img = img.convert("L")   # 转化为黑白图片
img.save(r"C:\Users\mango\Desktop\python代码\file\aaa\cat2.jpg")   # 存储图片



#ModuleNotFoundError 缺少模块

pillow          图片处理
requests        爬虫
pyemail         邮件处理
baidu-aip       百度人工智能接口
pymysql         mysql数据库连接
tushare         财经数据接口
pyecharts       数据可视化







