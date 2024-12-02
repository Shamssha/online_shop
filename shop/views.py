from django.shortcuts import render
from shop_settings import models


def header(request):
    obj = models.Ttings.objects.last()
    context = {
        'obj':obj
    }
    return render(request, 'base/header.html', context)
def footer(request):
    obj = models.Ttings.objects.last()
    context ={
        'obj':obj
    }
    return render(request, 'base/footer.html', context)