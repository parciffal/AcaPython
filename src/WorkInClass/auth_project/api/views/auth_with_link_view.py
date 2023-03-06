from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

import json
import jwt

from ..models import UserModel
from ..tools.http_tools import ok_status, data_status
from ..tools.jwt_tools import generate_jwt
from ..tools.email_tools import my_send_email

class UserAuthView(View):

    """
    ToDo

    1)token refresh 
    2)password change
    3)email verification
     
    """

    @csrf_exempt
    @staticmethod
    def user_info(request):
        token = request.META.get("HTTP_AUTHORIZATION").split()[1]
        user_info = jwt.decode(token, "SECRET_KEY", algorithms=['HS256'])
        return data_status(user_info)
    
    @csrf_exempt
    @staticmethod
    def login(request):
        data = json.loads(request.body.decode("utf-8"))
        try:
            username = data['username']
            password = data['password']
        except KeyError:
            return  HttpResponse({"status": "Missing key error"})
        user = authenticate(username=username, password=password)
        if user:
            try:
                user_model = UserModel.objects.get(user=user)
            except KeyError:
                return  HttpResponse({"status": "Missing key error"})
            login(request, user)
            jwt_token = generate_jwt(user_model)
            refresh_jwt_token = generate_jwt(user_model, True)

            response = JsonResponse(
                {"access_token": jwt_token, "refresh_token": refresh_jwt_token}
            )

            response.set_cookie("refresh_token", refresh_jwt_token, httponly=True)
            return response
        else:
            try:
                user = User.objects.get(username=username)
            except KeyError:
                return  HttpResponse({"status": "not register"})
            return HttpResponse({"status": "wrong password"})
            


    @csrf_exempt
    @staticmethod
    def register(request):
        data = json.loads(request.body)
        try:
            username = data['username']
            password = data['password']
            email = data['email']
            name = data['name']
            surname = data['surname']
        except KeyError:
            return  HttpResponse({"status": "Missing key error"})
        
        if User.objects.filter(username=username).exists():
            return  HttpResponse({"status": "User exist's"})
        else:
            user = User.objects.create_user(
                        username= username, 
                        password= password,
                        email= email)

            user.first_name = name
            user.last_name = surname
            user.is_active = False
            user.save()

            user_model = UserModel.objects.create(user=user,)
            user_model.save()
            verify_data = {}
            verify_data['subject'] = 'Activate your account'
            verify_data['message'] = 'Click the link below to activate your account: http://localhost:8000{}'\
                                     .format(reverse("activate", args=[user.pk]))
            verify_data['to'] = [user.email]
            return UserAuthView._email_verification(verify_data)
        
    @staticmethod
    def _email_verification(data):
        my_send_email(data)
    
    @csrf_exempt
    @staticmethod
    def activate(request, user_pk):
        try:
            user = User.objects.get(pk=user_pk)
        except KeyError:
            return  HttpResponse({"status": "User does not exist"})
        else:
            user.is_active = True
            user.save()
            return ok_status()

    @csrf_exempt
    @staticmethod
    def logout(request):
        logout(request)
        return ok_status()
 
