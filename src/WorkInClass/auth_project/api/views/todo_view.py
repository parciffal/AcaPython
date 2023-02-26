from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

import json
import jwt

from ..models import TodoModel, UserModel


class TodoView(View):
    
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type="application/json"
        )

    @staticmethod
    def ok_status():
        return HttpResponse(
            json.dumps({"status": "ok"}),
            status = 200,
            content_type="application/json"
        )
    

    def get(self, request):
        token = request.META.get("HTTP_AUTHORIZATION").split()[1]
        user_info = jwt.decode(token, "SECRET_KEY", algorithms=['HS256'])
        user = UserModel.objects.get(id=int(user_info['user_id']))
        todos = TodoModel.objects.filter(user=user).all()
        data = []
        for todo in todos:
            data.append(todo.as_json())

        return self.data_status(data)

    def post(self, request):
        token = request.META.get("HTTP_AUTHORIZATION").split()[1]
        user_info = jwt.decode(token, "SECRET_KEY", algorithms=['HS256'])
        user = UserModel.objects.get(id=int(user_info['user_id']))
        data = json.loads(request.body)
        todo = TodoModel.objects.create(
            user=user,
            text=data['text'],
            is_active=data['is_active'])
        todo.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        token = request.META.get("HTTP_AUTHORIZATION").split()[1]
        user_info = jwt.decode(token, "SECRET_KEY", algorithms=['HS256'])
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
        return TodoView.ok_status()

    @staticmethod
    def get_single(request, id):
        try:
            todo = TodoModel.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return TodoView.data_status(todo.as_json())

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
        
        return TodoView.ok_status()    
        

