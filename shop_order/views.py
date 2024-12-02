from django.shortcuts import render
from shahar.models import Product
# Create your views here.
def add_to_cart(request):
    cart_product = {}
    cart_product[str(request.GET['id'])]={
        'qty': request.GET['qty'],
        'pr_size': request.GET['pr_size'],
    }
    
    if 'cart_data_obj' in request.sessions:
        if str(request.GET[id]) in request.sessions['cart_data_obj']:
            cart_data = request.sessions['cart_data_obj']