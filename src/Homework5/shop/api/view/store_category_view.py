from django.views.generic import View

from ..models import StoreCategory
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

class StoreCategoryView(View):

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
        store_categorys = StoreCategory.objects.all()
        data = []
        for store_category in store_categorys:
            data.append(store_category.as_json())

        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        
        store_category = StoreCategory.objects.create(
            name = data['name']        
        )
        store_category.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return StoreCategoryView.delete(request, id)
        if request.method == "PATCH":
            return StoreCategoryView.edit(request, id)

    @staticmethod
    def delete(request, id):
        print(id)
        try:
            store_category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        store_category.delete()
        return StoreCategoryView.ok_status()

    @staticmethod
    def get_single(request, id):
        try:
            store_category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return StoreCategoryView.data_status(store_category.as_json())

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            store_category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            store_category.name = data['name']
            store_category.save()
        return StoreCategoryView.ok_status()    
            