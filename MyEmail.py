# coding=utf-8
import smtplib
from email.mime.text import MIMEText


class MyEmail:
    '''
    使用指定qq邮箱发送邮件到制定邮箱
    '''
    def __init__(self):
        msg_from = ""
        passwd = ""
        msg_to = ""
        subject = ""
        content = ""

    def setUser(self,msg_from,msg_to,passwd):
        '''

        :param msg_from:
        :param msg_to:
        :param passwd:这里的密码指的是授权密码
        :return:
        '''
        self.msg_from = msg_from
        self.passwd = passwd
        self.msg_to = msg_to


    def setContent(self,subject,content):
        self.subject = subject
        self.content = content


    def send(self):
        msg = MIMEText(self.content)
        msg['Subject'] = self.subject
        msg['From'] = self.msg_from
        msg['To'] = self.msg_to
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
            s.login(self.msg_from, self.passwd)
            s.sendmail(self.msg_from, self.msg_to, msg.as_string())
            print("发送成功")
        except:
            print("发送失败")
        finally:
            s.quit()