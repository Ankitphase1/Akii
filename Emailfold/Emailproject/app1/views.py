import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Emailproject.settings')
from django.core.mail import send_mail
from django.conf import settings



def my_mail(msg):
    subject = "Greetings from CPC"
    body = msg
    to = ["blacktomrider100@gmail.com", "umareankit08@gmail.com"]
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, to)
    print('mail send')
my_mail("HELLO SHUBHAM you are selected for infosis company")