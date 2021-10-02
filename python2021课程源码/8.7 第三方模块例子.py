from PIL import Image  #PIL(pillow) 图片处理模块

img = Image.open(r"C:\Users\mango\Desktop\python代码\file\aaa\cat.jpg")   # 读取图片
img = img.convert("L")   # 转化为黑白图片
img.save(r"C:\Users\mango\Desktop\python代码\file\aaa\cat2.jpg")   # 存储图片












