from django.contrib import admin
from .models import *
# Register your models here.

class ProductPanel(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['price']
    search_fields = ['name', 'price']

class ContactPanel(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'date_sent']
    list_filter = ['date_sent']
    search_fields = ['name']

class ProfilePanel(admin.ModelAdmin):
    list_display = ['user', 'location']
    search_fields = ['name', 'location']

class AddToCartPanel(admin.ModelAdmin):
    list_display = ['buyer', 'product', 'cart_count', 'total_amount']
    search_fields = ['buyer', 'product']


admin.site.register(Product, ProductPanel)
admin.site.register(Contact, ContactPanel)
admin.site.register(Profile, ProfilePanel)
admin.site.register(AddToCart, AddToCartPanel)
admin.site.register(Order)
