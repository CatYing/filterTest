from django.shortcuts import render
from django.apps import apps
# Create your views here.


def product_list(request):
    my_app_config = apps.get_app_config('cm')
    product_list = my_app_config.get_model("Product").objects.all()
    return render(request, 'test.html', {'product_list': product_list})
