from django.shortcuts import render
from . import models

def landing(request):
    return render(request, 'homechef/landing.html')

def Buy(request):
	return render(request,'homechef/buy.html')

def about(request):
	return render(request,'homechef/abt.html')

def Vendor(request):
	data=models.Vendor.objects.all()
	return render(request,'homechef/vendor.html',{'data':data})

def search(request):
	if request.method=='POST':
		name_search=request.POST.get('q')
		search_list=models.Vendor.objects.filter(name=name_search)
		return render(request,'homechef/search.html',{'data':search_list})
	else:
		data=models.Vendor.objects.all()
		return render(request,'homechef/vendor.html',{'data':data})

def display(request,vendor_id):
	data=None
	m=int(vendor_id)
	for vendor in models.Vendor.objects.all():
		n=int(vendor.id)
		if n==m:
			data=vendor
	print(data.food_items)
	return render(request,'homechef/display.html',{'data':data})

def product(request,vendor_id,food_id):
	data1=None
	m=int(vendor_id)
	for vendor in models.Vendor.objects.all():
		n=int(vendor.id)
		if n==m:
			data1=vendor
	print(data1.food_list())
	data=None
	m=int(food_id)
	for food in models.FoodItem.objects.all():
		n=int(food.id)
		if n==m:
			data=food
			print(food.ingredients)
			print("Yes")
	return render(request,'homechef/product.html',{'vendor':data1,'food':data})
	
def food(request):
	data=models.FoodItem.objects.all()
	return render(request,'homechef/food.html',{'data':data})

def vendorlist(request,food_id):
	data=None
	for sample in models.FoodItem.objects.all():
		if int(sample.id)==int(food_id):
			data=sample
	print(data.vendor_list())
	return render(request,'homechef/vendorlist.html',{'data':data})  