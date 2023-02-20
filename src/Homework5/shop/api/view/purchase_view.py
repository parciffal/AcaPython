from django.views.generic import View


from ..models import Purchase, Customer, Item
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

class PurchaseView(View):

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
        purchases = Purchase.objects.all()
        data = []
        for purchase in purchases:
            data.append(purchase.as_json())

        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        
        purchase = Purchase.objects.create(
            customer = Customer.objects.get(id=data['customer_id']),
            total_price = data['total_price'],
            items = (Item.objects.get(id=i) for i in data['items'])
        )
        purchase.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return PurchaseView.get_single(request, id)
        if request.method == "DELETE":
            return PurchaseView.delete(request, id)
        if request.method == "PATCH":
            return PurchaseView.edit(request, id)

    @staticmethod
    def delete(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        purchase.delete()
        return PurchaseView.ok_status()

    @staticmethod
    def get_single(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return PurchaseView.data_status(purchase.as_json())

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "custumer" in data:
            purchase.custumer = data['custumer']
            purchase.save()
        elif "total_price" in data:
            purchase.total_price = data['total_price']
        elif "buy_time" in data:
            purchase.buy_time = data['buy_time']
        elif "items" in data:
            if data['items']['status'] == 'delete':
                for i in data['items']['ids']:
                    item = Item.objects.get(id=i['item'])
                    purchase.items.remove(item)
            elif data['items']['status'] == 'add':
                for i in data['items']['ids']:
                    item = Item.objects.get(id=i['item'])
                    purchase.items.add(item)
            elif data['items']['status'] == 'clear':
                purchase.items.clear()
        return PurchaseView.ok_status()    