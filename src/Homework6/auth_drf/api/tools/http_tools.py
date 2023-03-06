from django.http import HttpResponse

import json


def data_status(data):
    return HttpResponse(
        json.dumps({"data": data, "status": "ok"}),
        content_type="application/json"
    )

def ok_status():
    return HttpResponse(
        json.dumps({"status": "ok"}),
        status = 200,
        content_type="application/json"
    )