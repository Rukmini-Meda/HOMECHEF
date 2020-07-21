from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VendorSerializer
from .serializers import FoodItemSerializer
from .serializers import IngredientsSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.utils import timezone
from django.views.generic import DetailView, View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CheckoutForm
from profiles.forms import VolunteerForm, VolunteerUpdateForm
from profiles.models import VolunteerModel
from django.core.paginator import Paginator
from django.db.models import Q
from payment.views import payment_process
from profiles.forms import VolunteerForm, VolunteerUpdateForm
from profiles.models import VolunteerModel

def landing(request):
    return render(request, 'homechef/landing.html')

def Buy(request):
	return render(request,'homechef/buy.html')

def about(request):
	return render(request,'homechef/abt.html')

def Vendor(request):
	data=models.Vendor.objects.all()
	return render(request,'homechef/vendor.html',{'data':data})

def Selling1(request):
	return render(request,'homechef/selling1.html')

def Bevolunteer(request):
	return render(request,'homechef/bevolunteer.html')

def Volunteerform(request):
	return render(request,'homechef/index.html')

def addsucc(request):
	return render(request,'homechef/addsucc.html')

def deletedsucc(request):
	return render(request,'homechef/deletedsucc.html')

@login_required
def myvolunteerinfo(request):
	if request.method == 'POST':
	   v_form = VolunteerUpdateForm(request.POST, instance=request.user.profile)
	   if v_form.is_valid():
		   v_form.save()
		   messages.success(request, f'Your account has been updated!')
		   return redirect('myvolunteerinfo')
	else:
		v_form = VolunteerUpdateForm(instance=request.user.profile)

	context = {
		'v_form':v_form
	}
	return render(request,'homechef/myvolunteerinfo.html', context)


def purchaseinfo(request):
	return render(request,'homechef/purchaseinfo.html')

def registeredsucc(request):
	return render(request,'homechef/registeredsucc.html')

def searchfood(request):
	return render(request,'homechef/searchfood.html')

def sell(request):
	return render(request,'homechef/sell.html')

def sellerprofile(request):
	return render(request,'homechef/sellerprofile.html')

def temporary(request):
	return render(request,'homechef/temporary.html')

def hire(request):
	return render(request,'homechef/hire.html')

def hireweb(request):
	return render(request, 'homechef/hireweb.html')


def search(request):
	#data2=None
	fulldata=[]
	query=request.GET.get('q')
	data1=models.Vendor.objects.all()
	fulldata=[f.name for f in data1]
	
	for i in range(len(fulldata)):
		if(fulldata[i].upper()==query.upper()):
			data=models.Vendor.objects.filter(name=fulldata[i])
		else:
			data=models.Vendor.objects.filter(name=query.capitalize())
	
	#data=models.Vendor.objects.filter(name=query)

	
	return render(request,'homechef/search.html',{'data':data})
	
def searchfood(request):
	query=request.GET.get('q')
	data=models.FoodItem.objects.filter(itemname=query.capitalize())
	return render(request,'homechef/searchfood.html',{'data':data})

def searchaddress(request):
	# query=request.GET.get('q')
	# data=models.Vendor.objects.filter(address=query.capitalize())
	# return render(request,'homechef/search.html',{'data':data})
	# 
	query=request.GET.get('q')
	data=models.Vendor.objects.filter(Q(address__icontains=query.capitalize()))
	return render(request,'homechef/search.html',{'data':data})	

def searchrating1(request):
	data=models.Vendor.objects.filter(rating=1)
	return render(request,'homechef/search.html',{'data':data})	

def searchrating2(request):
	data=models.Vendor.objects.filter(rating=2)
	return render(request,'homechef/search.html',{'data':data})	

def searchrating3(request):
	data=models.Vendor.objects.filter(rating=3)
	return render(request,'homechef/search.html',{'data':data})	

def searchrating4(request):
	data=models.Vendor.objects.filter(rating=4)
	return render(request,'homechef/search.html',{'data':data})	

def searchrating5(request):
	data=models.Vendor.objects.filter(rating=5)
	return render(request,'homechef/search.html',{'data':data})	

def foodrating1(request):
	data=models.FoodItem.objects.filter(rating=1)
	return render(request,'homechef/searchfood.html',{'data':data})	

def foodrating2(request):
	data=models.FoodItem.objects.filter(rating=2)
	return render(request,'homechef/searchfood.html',{'data':data})	

def foodrating3(request):
	data=models.FoodItem.objects.filter(rating=3)
	return render(request,'homechef/searchfood.html',{'data':data})	

def foodrating4(request):
	data=models.FoodItem.objects.filter(rating=4)
	return render(request,'homechef/searchfood.html',{'data':data})	

def foodrating5(request):
	data=models.FoodItem.objects.filter(rating=5)
	return render(request,'homechef/searchfood.html',{'data':data})	

def searchprice1(request):
	data=models.FoodItem.objects.filter(Q(price__gte=100) | Q(price__lt = 250))
	return render(request,'homechef/searchfood.html',{'data':data})	

def searchprice2(request):
	data=models.FoodItem.objects.filter(Q(price__gte= 250) | Q(price__lt = 500))
	return render(request,'homechef/searchfood.html',{'data':data})	

def searchprice3(request):
	data=models.FoodItem.objects.filter(Q(price__gte=500))
	return render(request,'homechef/searchfood.html',{'data':data})

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


class VendorList(viewsets.ModelViewSet):
	
	queryset=models.Vendor.objects.all()
	serializer_class=VendorSerializer
		
class FoodItemList(viewsets.ModelViewSet):
	queryset=models.FoodItem.objects.all()
	serializer_class=FoodItemSerializer

class IngredientsList(viewsets.ModelViewSet):
	queryset=models.Ingredients.objects.all()
	serializer_class=IngredientsSerializer


@login_required
def add_to_cart(request, vendor_id, food_id):
	item = get_object_or_404(models.FoodItem,id=food_id)
	vendorobj = get_object_or_404(models.Vendor,id=vendor_id)
	# print(item)
	# print(vendorobj)
	order_item = models.OrderItem.objects.get_or_create(item=item,vendorobj=vendorobj,user=request.user,ordered=False)
	# print(order_item)
	order_qs = models.Order.objects.filter(user = request.user,ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		if order.items.filter(item__id=item.id,vendorobj__id=vendorobj.id).exists():
			order_item[0].quantity += 1
			order_item[0].save()
			messages.info(request,"This item's quantity has been updated in the cart")
		else:
			order.items.add(order_item[0])
			messages.info(request,"This item has been added to the cart")
	else:
		ordered_date = timezone.now()
		order = models.Order.objects.create(user=request.user,ordered_date=ordered_date)
		order.items.add(order_item[0])
		messages.info(request,"This item's quantity has been updated in the cart")
	return redirect("order-summary")

class OrderSummaryView(LoginRequiredMixin,View):
	def get(self,*args,**kwargs):
		try:
			order = models.Order.objects.get(user=self.request.user,ordered=False)
			context = {
				'object': order
			}
			return render(self.request,'homechef/order_summary.html',context)
		except ObjectDoesNotExist:
			messages.error(self.request,"You do not have an active order")
			return redirect("/")
	template_name = "order_summary.html"

@login_required
def remove_from_cart(request,vendor_id,food_id):
	item = get_object_or_404(models.FoodItem,id=food_id)
	vendorobj = get_object_or_404(models.Vendor,id=vendor_id)
	order_qs = models.Order.objects.filter(user = request.user,ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		if order.items.filter(item__id=item.id,vendorobj__id=vendorobj.id).exists():
			order_item = models.OrderItem.objects.filter(
				item = item,
				vendorobj = vendorobj,
				user = request.user,
				ordered = False
			)[0]
			# print(order_item)
			order.items.filter(item__id=item.id,vendorobj__id=vendorobj.id).delete()
			messages.info(request,"This item has been removed from cart")
			return redirect("order-summary")
		else:
			messages.info(request,"This item was not in your cart")
			return redirect("order-summary")
	else:
		messages.info(request,"You do not have an active order")
		return redirect("order-summary")

@login_required
def remove_single_item_from_cart(request,vendor_id,food_id):
	item = get_object_or_404(models.FoodItem,id=food_id)
	vendorobj = get_object_or_404(models.Vendor,id=vendor_id)
	order_qs = models.Order.objects.filter(user = request.user,ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		if order.items.filter(item__id=item.id,vendorobj__id=vendorobj.id).exists():
			order_item = models.OrderItem.objects.filter(
				item = item,
				vendorobj = vendorobj,
				user = request.user,
				ordered = False
			)[0]
			# print(order_item)
			if order_item.quantity > 1:
				order_item.quantity -= 1
				order_item.save()
			else:
				order.items.filter(item__id=item.id,vendorobj__id=vendorobj.id).delete()
			print(order_item.quantity)
			messages.info(request,"This item's quantity has been updated")
			return redirect("order-summary")
		else:
			messages.info(request,"This item was not in your cart")
			return redirect("order-summary")
	else:
		messages.info(request,"You do not have an active order")
		return redirect("order-summary")

class CheckoutView(View):
	def get(self,*args,**kwargs):
		form = CheckoutForm()
		context = {
			'form': form
		}
		return render(self.request,"homechef/checkout.html",context)
	
	def post(self,*args,**kwargs):
		form = CheckoutForm(self.request.POST or None)
		try:
			order = models.Order.objects.get(user=self.request.user,ordered=False)
			# print(form.street_address)
			# print(form.apartment_address)
			# print(form.country)
			# print(form.zipfield)
			# print(form.payment_option)
			# if form.is_valid():
			# 	street_address = form.cleaned_data.get('street_address')
			# 	apartment_address = form.cleaned_data.get('apartment_address')
			# 	country = form.cleaned_data.get('country')
			# 	zipfield = form.cleaned_data.get('zipfield')
			# 	payment_option = form.cleaned_data.get('payment_option')
			# 	# billing_address = models.BillingAddress(
			# 	# 	user = self.request.user,
			# 	# 	street_address = street_address,
			# 	# 	apartment_address = apartment_address,
			# 	# 	country = country,
			# 	# 	zipfield = zipfield
			# 	# )
			# 	# billing_address.save()
			# 	# order.billing_address = billing_address
			# 	order.save()
			# 	return redirect('checkout')
			# messages.warning(self.request,"Failed checkout")
			return redirect('payment')
		except ObjectDoesNotExist:
			messages.error(self.request,"You do not have an active order")
			return redirect("order-summary")
		
			
def listing(request):
    vendor_list = Vendor.objects.all()
    paginator = Paginator(vendor_list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vendor.html', {'page_obj': page_obj})			

class VolunteerView(View):
	def get(self, *args, **kwargs):
		form = VolunteerForm()
		context = {
			'form': form
		}
		return render(self.request,'homechef/index.html',context)

	def post(self, *args, **kwargs):
		form = VolunteerForm(self.request.POST or None)
		if form.is_valid():
			address = form.cleaned_data.get('address')
			city = form.cleaned_data.get('city')
			state = form.cleaned_data.get('state')
			pincode = form.cleaned_data.get('pincode')
			volunteer_model = VolunteerModel(
				user = self.request.user,
				address = address,
				city = city,
				state = state,
				pincode = pincode,
			)
			volunteer_model.save()
			return render(self.request,'homechef/landing.html')
		return render(self.request,'homechef/landing.html')
