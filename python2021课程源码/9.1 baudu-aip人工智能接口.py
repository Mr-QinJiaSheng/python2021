# baudu-aip 人工智能接口
from aip import AipOcr


""" 你的 APPID AK SK """
APP_ID = '23987163'
API_KEY = 'G1zMsGAGOyAKF3VDiYRmQwqy'
SECRET_KEY = 'bToYVIkK4cO1VxpnGjjWyRjThyweuH8v'

#ocr客户端对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

#读取图片
with open(r"C:\Users\mango\Desktop\python代码\file\ss.png","rb") as f:
	img=f.read()

#识别文字
data=client.basicGeneral(img)

for d in data["words_result"]:
	print(d["words"])








