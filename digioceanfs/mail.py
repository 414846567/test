#coding=UTF-8
import smtplib
from time import sleep
from email.mime.text import MIMEText
from email.header import Header

sender='caoyi@estor.com.cn'
receiver='caoyi@estor.com.cn'
subject ="hello world"
smtpserver='smtp.estor.com.cn'
username='caoyi@estor.com.cn'
password='xifunizainaer96'


msg=MIMEText('你好!','text','utf-8')
msg['Subject'] = Header(subject, 'utf-8')


smtp = smtplib.SMTP()
smtp.connect=(smtpserver,25)
smtp.login(username,password)
smtp.sendmail(sender,reciver,msg.as_string())
#smtp.quit()
