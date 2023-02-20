from django.views.generic import View
from ..models import Store, StoreCategory, StoreOwner
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

class StoreView(View):

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
        stores = Store.objects.all()
        data = []
        for store in stores:
            data.append(store.as_json())

        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        store = Store.objects.create(
            name = data['name'],
            owner = StoreOwner.objects.get(id=data['owner_id']),
            store_category = StoreCategory.objects.get(id=data['store_category_id'])
        )
        store.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreView.get_single(request, id)
        if request.method == "DELETE":
            return StoreView.delete(request, id)
        if request.method == "PATCH":
            return StoreView.edit(request, id)

    @staticmethod
    def delete(request, id):
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        store.delete()
        return StoreView.ok_status()

    @staticmethod
    def get_single(request, id):
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return StoreView.data_status(store.as_json())

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            store.name = data['name']
            store.save()
        elif "owner" in data:
            store.owner = StoreOwner.objects.get(id=data['owner'])
            store.save()
        elif "store_category" in data:
            store.store_category = StoreCategory.objects.get(id=data['store_category'])
            store.save()
        return StoreView.ok_status()    
            

