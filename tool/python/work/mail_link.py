#-*- coding: UTF-8 用python发送带附件的邮件 -*-
import sys
import getopt
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from subprocess import *
from email.utils import COMMASPACE
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


def sendgmail(username, password, mailfrom, mailto, subject, content):
    gserver = 'smtp.gmail.com'
    gport = 587

    msg = MIMEText(unicode(content).encode('utf-8'))
    msg['from'] = mailfrom
    msg['to'] = mailto
    msg['Reply-To'] = mailfrom
    msg['Subject'] = subject

    smtp = smtplib.SMTP(gserver, gport)
    smtp.set_debuglevel(0)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(username,password)

    smtp.sendmail(mailfrom, mailto, msg.as_string())
    smtp.close()


def sendqqmail(username, password, mailfrom, mailto, subject, content):
    gserver = 'smtp.exmail.qq.com'
    gport = 465

    try:
        msg = MIMEMultipart()
        msg['from'] = mailfrom
        msg['to'] = COMMASPACE.join(mailto)
        msg['Reply-To'] = mailfrom
        msg['Subject'] = Header(subject,'utf-8')
        msg["Accept-Language"] = "zh-CN"
        msg["Accept-Charset"] = "utf-8"

        att1 = MIMEText(open('d:\\coohua\data.txt', 'rb').read(), 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="content.txt"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
        msg.attach(att1)

        msg.attach(MIMEText(content, 'plain', 'utf-8'))

        smtp = smtplib.SMTP_SSL(gserver, gport)
        smtp.set_debuglevel(0)
        smtp.ehlo()
        smtp.login(username, password)

        smtp.sendmail(mailfrom, mailto, msg.as_string())
        smtp.close()
    except Exception, err:
        print "Send mail failed. Error: %s" % err


def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    to = ['dushupeng@coohua.com']
    #to=['wenguozhu@coohua.com','wuxianhe@coohua.com','wangxin@coohua.com','zhoucheng@coohua.com','dev_data@coohua.com','wangshicheng@coohua.com','zhouwei@coohua.com']
    subject = sys.argv[2]
    content = sys.argv[3]
    sendqqmail('monitor@coohua.com', 'PGMaiX7BC9nr', 'monitor@coohua.com', to, subject, content)


if __name__ == "__main__":
    main()
