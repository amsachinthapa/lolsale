from django.urls import path
from .views import *


app_name= "lolapp"
urlpatterns = [
	path('', HomeView.as_view(), name="home"),
	path('about-us/', AboutView.as_view(), name="about"),
	path('contact/', ContactView.as_view(), name="contact"),
	path('store/', Store.as_view(), name="store"),
	path('local_product/', Local_product.as_view(), name="local_product"),
	path('livestokes/', Livestokes.as_view(), name="livestokes"),
	path('all-products/', AllProductsView.as_view(), name="allproducts"),
	path('product/<slug:slug>/', ProductDetailView.as_view(), name="productdetail"),
	path('add-to-cart-<int:pro_id>/', AddToCartView.as_view(), name="addtocart"),
] 