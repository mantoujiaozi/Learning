# -*- coding: UTF-8 -*-
import sys
import getopt
import smtplib
from email.mime.text import MIMEText
# from email.MIMEMultipart import MIMEMultipart
from subprocess import *
from email.utils import COMMASPACE
from email.header import Header


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
    smtp.login(username, password)

    smtp.sendmail(mailfrom, mailto, msg.as_string())
    smtp.close()


def sendqqmail(username, password, mailfrom, mailto, subject, content):
    gserver = 'smtp.exmail.qq.com'
    gport = 465

    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['from'] = mailfrom
        msg['to'] = COMMASPACE.join(mailto)
        msg['Reply-To'] = mailfrom
        msg['Subject'] = Header(subject, 'utf-8')
        msg["Accept-Language"] = "zh-CN"
        msg["Accept-Charset"] = "utf-8"

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
    # to=['wenguozhu@coohua.com','wuxianhe@coohua.com','wangxin@coohua.com','zhoucheng@coohua.com',
    #     'dev_data@coohua.com','wangshicheng@coohua.com','zhouwei@coohua.com']
    subject = sys.argv[2]
    content = sys.argv[3]
    sendqqmail('monitor@coohua.com', 'PGMaiX7BC9nr', 'monitor@coohua.com', to, subject, content)


if __name__ == "__main__":
    main()
