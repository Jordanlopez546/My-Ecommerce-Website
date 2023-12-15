from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
from .models import *
# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def product(request):
    products = Product.objects.all()
    return render(request, 'blog.html', {'products':products})




@login_required(login_url='login')
def cart(request):
    user_profile = Profile.objects.get(user=request.user)
    carts = AddToCart.objects.filter(buyer=user_profile)
    return render(request, 'cart.html', {'carts':carts})




@login_required(login_url='login')
def add_to_cart(request):
    
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        user_profile = Profile.objects.get(user=request.user)
        
        if AddToCart.objects.filter(buyer=user_profile, product_id=product_id).exists():
            messages.info(request, "Added to Cart already.")
            return redirect('cart')
        
        else:
            product = Product.objects.get(pk=product_id)
            product_amount = product.price
            product_total = product_amount + 100
            product.no_of_carts +=1 
            product_count = product.no_of_carts
            product.save()

            new_cart = AddToCart.objects.create(buyer=user_profile, product=product, cart_count=product_count, total_amount=product_total)
            new_cart.save()
            messages.info(request, "Added to Cart.")

        return redirect('cart')
    



@login_required(login_url='login')
def remove_from_cart(request):

    if request.method == "POST":
        product_id  = request.POST.get('product_id')
        user_profile = Profile.objects.get(user=request.user)
        product = Product.objects.get(pk=product_id)

        if AddToCart.objects.filter(product_id=product_id, buyer=user_profile).exists():
            delete_cart = AddToCart.objects.get(product_id=product_id, buyer=user_profile)
            delete_cart.delete()

            product.no_of_carts -= 1
            product.save()

            messages.info(request, "Removed From Cart.")

        else:
            messages.info(request, "Product is not in cart.")

        return redirect('cart')




@login_required(login_url='login')
def order(request):
    user_profile = Profile.objects.get(user=request.user)
    orders = Order.objects.filter(buyer=user_profile)
    return render(request, 'order.html', {'orders':orders})




@login_required(login_url='login')
def place_order(request):

    if request.method == "POST":
        product_id = request.POST.get('product_id')
        user_profile = Profile.objects.get(user=request.user)

        product = Product.objects.get(pk=product_id)
        addtocart_item = AddToCart.objects.get(product=product, buyer=user_profile)
        order_item = Order.objects.create(product=addtocart_item, buyer=user_profile)
        order_item.save()
        messages.info(request, "Order Placed.")

    return redirect('order')




@login_required(login_url='login')
def contact(request):
    
    try:
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']


            new_contact = Contact(
                    name=username,
                    email=email,
                    subject=subject,
                    message=message,
                )

            new_contact.save()

            messages.success(request, f'Message delivered, {username}.')
            return redirect('index')
        else:
            return render(request, 'index.html')
    except:
        Http404




def register(request):
    
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken. Please Try another.')
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Name already taken. Please Try another.')
                return redirect('register')
            
            else:
                new_user = User.objects.create_user(email=email,username=username,password=password)
                new_user.save()
                
                login_user = auth.authenticate(username=username,password=password)
                auth.login(request, login_user)

                user_model = User.objects.get(username=username)
                new_user_profile = Profile.objects.create(
                    user=user_model,
                    id_user=user_model.id
                )
                new_user_profile.save()
                messages.info(request, f'Welcome {username}.')
                return redirect('setting')
            
        else:
            messages.info(request, 'Password not the same.')
            return redirect('register')
    else:
        return render(request, 'register.html')




def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, f'Welcome {username}.')
            return redirect('index')

        else:
            messages.info(request, 'Invalid Credentials. Please Try another.')
            return redirect('login')
    else:
        return render(request, 'login.html')




@login_required(login_url='login')
def setting(request):
    
    user_profile = Profile.objects.get(user=request.user)

    if request.method == "POST":

        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        
        messages.info(request, f'{user_profile.user.username}, your Profile is updated.')
        return redirect('index')
    
    else:
        return render(request, 'setting.html',{'user_profile':user_profile})
    




@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

