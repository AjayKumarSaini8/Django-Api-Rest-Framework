from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from products.models import Product


def api_home(request, *args, **kwargs):
    mode_data = Product.objects.all().order_by("?").first()
    data = {}
    if mode_data:
        data = model_to_dict(mode_data, fields=["id", "title", "price"])
    return HttpResponse(data, headers={"content-type": "application/json"})
