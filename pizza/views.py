from django.shortcuts import render, redirect
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages 
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from instamojo_wrapper import Instamojo
# api = Instamojo(api_key=API_KEY,
#                 auth_token=AUTH_TOKEN)

def home(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, "index.html", context)


def login_page(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_obj = User.objects.filter(username=username)

            if not user_obj.exists():
                messages.error(request, "user is not available")
                return redirect('/login/')
            
            user_obj = authenticate(username=username, password=password)

            if user_obj:
                login(request, user_obj)
                return redirect('/')
            
            messages.error(request, "Wrong Password")
            return redirect('/login/')
        
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/login/')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_obj = User.objects.filter(username=username)

            if user_obj.exists():
                messages.error(request, "username is already taken")
                return redirect('/register/')
            
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()

            messages.success(request, "User created successfully")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
    return render(request, "register.html")
    
        
@login_required()
def add_cart(request, p_uid):
    user = request.user
    pizza_obj = Pizza.objects.get(uid = p_uid)
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)

    cart_items = CartItems.objects.create(
        cart = cart,
        pizza = pizza_obj
    )
    return redirect('/')


@login_required()
def cart(request):
    cart = Cart.objects.get(is_paid=False, user=request.user)

    # response = api.payment_request_create(
    #     amount = cart.get_cart_total(),
    #     purpose = "Order",
    #     buyer_name = request.user.username,
    #     email = 'test@mail.com',
    #     redirect_url = 'http://127.0.0.1:8000/success'
    # )
    # cart.instamojo_id = response['payment_request']['id']
    # cart.save()

    context = {'carts': cart, 
            #    'payment_url' : response['payment_request']['long_url']
               }
    return render(request, "cart.html", context)

@login_required()
def remove_cart_item(request, cart_item_uid):
    try:
        CartItems.objects.get(uid = cart_item_uid).delete()
        return redirect('/cart')

    except Exception as e:
        print(e)

@login_required()
def orders(request):
    orders = Cart.objects.filter(is_paid=True, user = request.user)
    context = {'orders': orders}
    return render(request, "order.html", context)