from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ...tools.http_tools import ok_status, data_status
from ...tools.email_tools import my_send_email
from ...tools.verify_tools import generate_verify_code

from ...tasks.message_task import *



class TaskView(View):

    @staticmethod
    def mail(request):
        data = {}
        data['activate_code'] = generate_verify_code()
        data['to'] = "edgarchik99@gmail.com"
        mail_task.delay(data)
        return ok_status()

