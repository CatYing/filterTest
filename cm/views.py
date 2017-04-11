from django.shortcuts import render
from model_filter import *
# Create your views here.


def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'test.html', {'filter': f})
