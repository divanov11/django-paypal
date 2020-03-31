from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Product, Order

# Create your views here.

def simpleCheckout(request):
	return render(request, 'base/simple_checkout.html')


def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'base/store.html', context)

def checkout(request, pk):
	product = Product.objects.get(id=pk)
	context = {'product':product}
	return render(request, 'base/checkout.html', context)

def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Product.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
		)

	return JsonResponse('Payment completed!', safe=False)