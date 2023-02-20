from django.views.generic import View

from ..models import Item, ItemCategory, Store
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

class ItemView(View):

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
        items = Item.objects.all()
        data = []
        for item in items:
            data.append(item.as_json())

        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        item = Item.objects.create(
            store=Store.objects.get(id=data['store_id']),
            name=data['name'],
            category=ItemCategory.objects.get(id=data['category_id']),
            price=data['price'],
            quantity=data['quantity'],
            info=data['info'])
        item.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemView.get_single(request, id)
        if request.method == "DELETE":
            return ItemView.delete(request, id)
        if request.method == "PATCH":
            return ItemView.edit(request, id)

    @staticmethod
    def delete(request, id):
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        item.delete()
        return ItemView.ok_status()

    @staticmethod
    def get_single(request, id):
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return ItemView.data_status(item.as_json())

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            item.name = data['name']
            item.save()
        elif "category_id" in data:
            item.category = ItemCategory.objects.get(id=data['category_id'])
        elif 'store_id' in data:
            item.store = Store.objects.get(id=data['store_id'])
        elif 'price' in data:
            item.price = data['price']
        elif 'quantity' in data:
            item.quantity = data['quantity']
        elif 'info' in data:
            item.info = data['info']
        return ItemView.ok_status()    
            

