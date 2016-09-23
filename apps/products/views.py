from django.shortcuts import render, redirect
from . import models
from django.core.urlresolvers import reverse
from django.contrib import messages

# Create your views here.
def index(request):
	allProducts = models.Products.objects.all()
	context = {'products': allProducts}
	return render(request, 'products/index.html', context)

# Renders product view of specific product selected
def show(request, productID):
	product = models.Products.objects.get(id=productID)
	context = {'product': product}
	return render(request, 'products/product.html', context)

# Renders form for updating specific product
def edit(request, productID):
	product = models.Products.objects.get(id=productID)
	context = {'submitType': 'Update', 'product': product}
	return render(request, 'products/createupdate.html', context)

# Updates database with form input from 'edit'
def update(request, productID):
	updatedProd=models.Products.objects.updater(id=productID, name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
	if updatedProd[0]:
		messages.success(request, updatedProd[1])
		return redirect(reverse('products:index'))
	else:
		messages.error(request, updatedProd[1])
		return redirect(reverse('products:edit', kwargs={'productID':productID}))

# Renders form for creating a new product
def new(request):
	context = {'submitType': 'Create'}
	return render(request, 'products/createupdate.html', context)

# Adds new product into database with from input from 'new'
def create(request):
	newProd = models.Products.objects.creator(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
	if newProd[0]:
		messages.success(request, newProd[1])
		return redirect(reverse('products:index'))
	else:
		messages.error(request, newProd[1])
		return redirect(reverse('products:new'))

# Removes the selected product
def destroy(request, productID):
	models.Products.objects.destroy(id=productID)
	messages.success(request, "Product has been successfully removed!")
	return redirect(reverse('products:index'))