from django.views.generic import View
from django.contrib.auth.models import User

from ..models import Store, StoreCategory, StoreOwner
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

class StoreOwnerView(View):

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
        store_owners = StoreOwner.objects.all()
        data = []
        for store_owner in store_owners:
            data.append(store_owner.as_json())

        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        
        store_owner = StoreOwner.objects.create(
            user = User.objects.get(id=data['user_id'])        
        )
        store_owner.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreOwnerView.get_single(request, id)
        if request.method == "DELETE":
            return StoreOwnerView.delete(request, id)
        if request.method == "PATCH":
            return StoreOwnerView.edit(request, id)

    @staticmethod
    def delete(request, id):
        try:
            store_owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        store_owner.delete()
        return StoreOwnerView.ok_status()

    @staticmethod
    def get_single(request, id):
        try:
            store_owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return StoreOwnerView.data_status(store_owner.as_json())

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            store_owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "user" in data:
            store_owner.user = data['user']
            store_owner.save()
        return StoreOwnerView.ok_status()    
            

