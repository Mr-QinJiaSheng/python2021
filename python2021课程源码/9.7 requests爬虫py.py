#requests爬虫
import requests

#抓包获取音乐的链接
url="https://m801.music.126.net/20210415105529/957f299b2a0aaba6fa28\
e2a8f643edfb/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/8304332344/f1c4/df0e/\
4fd8/8625bca4605b72e8cfeb8fda3cc6365a.m4a"

#get()向服务器发送get请求  .content获取二进制数据（.text 获取文本数据）
data=requests.get(url).content

#写入到本地
with open(r"C:\Users\mango\Desktop\python代码\file\音乐0415.m4a","wb") as f:
	f.write(data)