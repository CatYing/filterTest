from django.shortcuts import render
from cm import models
# Create your views here.


def product_list(request):
    subs = models.__dict__
    results = subs["Product"].objects.all()
    return render(request, 'test.html', {"results": results})
