from django.db import models
import datetime
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class Product(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100000)
    user = models.CharField(max_length=100000, default='Jordan')
    price = models.FloatField()
    no_of_carts = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=20000)
    email = models.CharField(max_length=2000, null=True)
    subject = models.CharField(max_length=20000)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to="users_profile_photos", default='blank-profile-picture.png')
    location = models.CharField(max_length=1002002, blank=True)

    def __str__(self):
        return self.user.username
    
class AddToCart(models.Model):
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_count = models.IntegerField(default=0)
    total_amount = models.FloatField(default=0)
    
    def __str__(self):
        return f"{self.buyer} - {self.product}"
    

class Order(models.Model):
    product = models.ForeignKey(AddToCart, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.buyer.user.username} - {self.product.product.name}"
    


