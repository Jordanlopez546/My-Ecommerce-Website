from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('product', views.product, name='product'),
    path('register', views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('setting', views.setting, name='setting'),
    path('logout', views.logout,name='logout'),
    path('login', views.login,name='login'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    path('order/', views.order, name='order'),
    path('place-order/', views.place_order, name='place_order')
]