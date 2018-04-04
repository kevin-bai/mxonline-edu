# _*_ coding:utf-8 _*_
# 邮箱验证码
__author__ = 'kevin'
__date__ = '2018/4/4 9:36'
from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from mxonline.settings import EMAIL_FROM


# 保存向用户发送的验证邮件
def send_register_mail(email, send_type='register'):
    email_code = EmailVerifyRecord()
    email_code.email = email
    code = random_str(8)
    email_code.code = code
    email_code.send_type = send_type
    email_code.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "慕学在线注册邮件"
        email_body = "请点击下面的注册激活链接激活你的账号： http://127.0.0.1/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def random_str(code_length=8):
    _str = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    char_len = len(chars) - 1
    random = Random()
    for i in range(code_length):
        _str += chars[random.randint(0, char_len)]
    return _str
