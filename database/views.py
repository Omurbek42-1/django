from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.template import loader

def text_response_view(request):
    return HttpResponse("Это текстовый ответ")

def object_response_view(request):
    products = Product.objects.all()
    return HttpResponse(products)

def html_template_view(request):
    products = Product.objects.all()
    template = loader.get_template('app/product_list.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))
