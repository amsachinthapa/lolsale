from django.contrib import admin
from .models import *




admin.site.register([Admin,Customer,Category,Product,CartProduct,Cart,ProductImage,Order, Review])