from django.views.generic import View
from ..models import ItemCategory
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

class ItemCategoryView(View):

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
        categories = ItemCategory.objects.all()
        data = []
        for category in categories:
            data.append(category.as_json())

        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = ItemCategory.objects.create(
            name = data['name']
        )
        category.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return ItemCategoryView.delete(request, id)
        if request.method == "PATCH":
            return ItemCategoryView.edit(request, id)

    @staticmethod
    def delete(request, id):
        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        category.delete()
        return ItemCategoryView.ok_status()

    @staticmethod
    def get_single(request, id):
        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return ItemCategoryView.data_status(category.as_json())

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data['name']
            category.save()
        return ItemCategoryView.ok_status()    
            

