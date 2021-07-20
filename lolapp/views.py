from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from django.views.generic import TemplateView
from .models import *


class HomeView(TemplateView):
	template_name = "home.html" 

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['product_list']=Product.objects.all().order_by("-id")

		return context


class AllProductsView(TemplateView):
	template_name="allproducts.html"

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['allcategories']=Category.objects.all()
		return context

class ProductDetailView(TemplateView):
	template_name="productdetail.html"

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		url_slug=self.kwargs['slug']
		product=Product.objects.get(slug=url_slug)
		product.view_count +=1
		product.save()
		context['product']=product
		return context


class AddToCartView(TemplateView):
	template_name="addtocart.html"

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
	#get product id from reqst ur
		product_id= self.kwargs['pro_id']
	#get product
		product_obj=Product.objects.get(id=product_id)
	#check if cart exist
		cart_id=self.request.session.get("cart_id", None)
		if cart_id:
			cart_obj= Cart.objects.get(id=cart_id)
			this_products_in_cart= cart_obj.cartproduct_set.filter(
			product=product_obj)

			if this_product_in_cart.exist():
				cartproduct= this_product_in_cart.last()
				cartproduct.quantity +=1
				cartproduct.subtotal +=product_obj.selling_price
				cartproduct.save()
				cart_obj.total += product_obj.selling_price
				cart_obj.save()

			else:
				cartproduct=CartProduct.objects.create(
				cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, subtotal=product_obj.selling_price)
				cart_obj.total+=product_obj.selling_price
				cart_obj.save()

		else:
			cart_obj= Cart.objects.create(total=0)
			self.request.session['cart_id']=cart_obj.id
			cartproduct=CartProduct.objects.create(
				cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, subtotal=product_obj.selling_price)
			cart_obj.total+=product_obj.selling_price
			cart_obj.save()
	#check if product already exist in cart 
 
		return context


class AboutView(TemplateView):
	template_name= "about.html" 


class ContactView(TemplateView):
	template_name= "contact.html  "


class Store(TemplateView):
	template_name= "store/store.html"

class Local_product(TemplateView):
	template_name= "store/lolproduct.html"

class Livestokes(TemplateView):
	template_name= "store/livestoke.html"


