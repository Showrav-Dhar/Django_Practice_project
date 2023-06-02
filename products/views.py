from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product

# Create your views here.

def index (request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products':products})#third argument is a dictionary


def new_fun(request):
    return HttpResponse("it is working !!")


