# pyEmail邮件处理

# 客户端1----微信服务器----客户端2
# 客户端1(网易)----网易邮箱服务器-----QQ邮箱服务器------客户端2（QQ）

# 邮箱协议：smtp协议  imap协议  pop协议

import smtplib   #smtp协议包
from email.mime.text import MIMEText #用于构建邮箱内容

msg_from="test666@126.com" #发件人
password="QBVECGFSSZOJARVS" #客户端授权码
msg_to="2268902957@qq.com"   #收件人 


#构造邮件内容
subject="0414测试邮件"
content="你中奖了！5毛钱！"
msg=MIMEText(content)  #msg邮件内容对象
msg["Subject"]=subject
msg["From"]=msg_from
msg["To"]=msg_to


#发送邮件
smtpObj=smtplib.SMTP_SSL("smtp.126.com",465)  #smtpObj smtp对象
smtpObj.login(msg_from,password) #登录
smtpObj.sendmail(msg_from,msg_to,str(msg)) #发送邮件
print("发送成功！")
smtpObj.quit()







