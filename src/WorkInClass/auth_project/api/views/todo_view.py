from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

import json

from ..models import TodoModel, UserModel
from ..tools.http_tools import *
from ..tools.jwt_tools import decode_jwt

class TodoView(View):
   
    def get(self, request):
        user_info = decode_jwt(request)
        
        user = UserModel.objects.get(id=int(user_info['user_id']))
        todos = TodoModel.objects.filter(user=user).all()
    
        data = []
        for todo in todos:
            data.append(todo.as_json())

        return data_status(data)

    def post(self, request):
        user_info = decode_jwt(request)
        user = UserModel.objects.get(id=int(user_info['user_id']))
        
        data = json.loads(request.body)
        
        todo = TodoModel.objects.create(
            user=user,
            text=data['text'],
            is_active=data['is_active'])
        
        todo.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        user_info = decode_jwt(request)
        try:
            user = UserModel.objects.get(id=int(user_info['user_id']))
        except:
            return  HttpResponse({"status": "user not found"})
        if user:
            if request.method == "GET":
                return TodoView.get_single(request, id)
            if request.method == "DELETE":
                return TodoView.delete(request, id)
            if request.method == "PATCH":
                return TodoView.edit(request, id)

    @staticmethod
    def delete(request, id):
        try:
            todo = TodoModel.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        todo.delete()
        
        return ok_status()

    @staticmethod
    def get_single(request, id):
        try:
            todo = TodoModel.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        return data_status(todo.as_json())

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            item = TodoModel.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "text" in data:
            item.text = data['text']
            item.save()
        elif "is_active" in data:
            item.is_active = data['is_active']
            item.save()
        
        return ok_status()    
        

