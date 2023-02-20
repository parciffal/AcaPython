from django.views.generic import View


from ..models import MyBug, Customer, Item
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

class MyBugView(View):

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
        my_bugs = MyBug.objects.all()
        data = []
        for bug in my_bugs:
            data.append(bug.as_json())

        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        
        my_bug = MyBug.objects.create(
            customer = Customer.objects.get(id=data['customer_id']),
            total_price = data['total_price'],
            items = (Item.objects.get(id=i) for i in data['items'])
        )
        my_bug.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return MyBugView.get_single(request, id)
        if request.method == "DELETE":
            return MyBugView.delete(request, id)
        if request.method == "PATCH":
            return MyBugView.edit(request, id)

    @staticmethod
    def delete(request, id):
        try:
            my_bug = MyBug.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        my_bug.delete()
        return MyBugView.ok_status()

    @staticmethod
    def get_single(request, id):
        try:
            my_bug = MyBug.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return MyBugView.data_status(my_bug.as_json())

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            my_bug = MyBug.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "custumer" in data:
            my_bug.custumer = data['custumer']
            my_bug.save()
        elif "total_price" in data:
            my_bug.total_price = data['total_price']
        elif "items" in data:
            if data['items']['status'] == 'delete':
                for i in data['items']['ids']:
                    item = Item.objects.get(id=i['item'])
                    my_bug.items.remove(item)
            elif data['items']['status'] == 'add':
                for i in data['items']['ids']:
                    item = Item.objects.get(id=i['item'])
                    my_bug.items.add(item)
            elif data['items']['status'] == 'clear':
                my_bug.items.clear()
        return MyBugView.ok_status()    