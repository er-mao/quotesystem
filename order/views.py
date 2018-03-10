from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def order(request):
    return render(request, 'order/order.html')

def order_number(request, order_number):
    return render(request, 'order/order_number.html', {'order_number': order_number})

def my_order(request):
    return render(request, 'order/my_order.html')