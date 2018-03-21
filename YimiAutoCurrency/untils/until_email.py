import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
import datetime


def meil_send(receivers='jinghao.xu@1mifudao.com', url='D:\\yimi_work\\yimi_auto_test_001\\untils\\1.html'):
    # 第三方 SMTP 服务
    mail_host = "smtp.exmail.qq.com"  # 设置服务器
    mail_user = "jinghao.xu@1mifudao.com"  # 用户名
    mail_pass = "SSSabc123"  # 口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格

    # 发送者
    sender = 'jinghao.xu@1mifudao.com'

    # 接收方，抄送的人都放在这里面
    receivers = ['jinghao.xu@1mifudao.com', 'weihong.shen@1mifudao.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEMultipart()

    # 以下都是邮件的显示文字
    message.attach(MIMEText('测试报告 - ' + str(datetime.datetime.now()) + '\n详情见附件', 'plain', 'utf-8'))
    message['From'] = Header("徐敬浩<jinghao.xu@1mifudao.com>", 'utf-8')
    message['To'] = Header("徐敬浩<jinghao.xu@1mifudao.com>", 'utf-8')
    message['Cc'] = Header("申卫红<weihong.shen@1mifudao.com>", 'utf-8')

    subject = '测试报告'
    message['Subject'] = Header(subject, 'utf-8')

    # 附件
    art = MIMEApplication(open(url, 'rb').read())
    art.add_header('content-disposition', 'attachment', filename='1.html')
    message.attach(art)

    smtp_obj = smtplib.SMTP_SSL(mail_host, 465)
    smtp_obj.login(mail_user, mail_pass)
    smtp_obj.sendmail(sender, receivers, message.as_string())
    smtp_obj.quit()


if __name__ == '__main__':
    meil_send()
# print(open('1.html', 'rb').read())
