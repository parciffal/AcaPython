#
from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives


#
import environ


env = environ.Env()
environ.Env.read_env()


#

def my_send_email(data):
    send_mail(
        data['subject'],
        data['message'],
        env('GMAIL_USERNAME'),
        data['to'],
        fail_silently=False,
        )

"""
def _send_email_html(data):
    msg = EmailMultiAlternatives(data['subject'], data['message'], data['from'], data['to'])
    msg.attach_alternative(data['html'], "text/html")
    msg.send()
 
#
def send_confirmation_email(user, html):
    
    data = {
        "from": env("GMAIL_USERNAME"),
        "to": [user.email],
        "subject": "Email Verification",
        "html": html,
    }
    _send_email(data)
    

#
def send_card_creation_email(user, html):
    data = {
        "from": env("GMAIL_USERNAME"),
        "to": [user.email],
        "subject": "New card created",
        "html": html
    }
    _send_email(data)
    

#
def send_service_add_email(user, html):
    
    data = {
        "from": env("GMAIL_USERNAME"),
        "to": [user.email],
        "subject": "New service added",
        "html": html
    }
    _send_email(data)
""" 
