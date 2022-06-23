from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
# from django.contrib import messages
# from .forms import UserRegistrationForm
# Create your views here.

User = get_user_model()


def index(request):
    return render(request, 'index.html')


def INDEX(request):
    return render(request,'index1.html')

def BASE(request):
    return render(request, '/home/neosoft/PycharmProjects/DemoProject/mysite/eshopper/template/eshopper/base.html')


def CONTACT(request):
    return render(request,'/home/neosoft/PycharmProjects/DemoProject/mysite/eshopper/template/eshopper/contactus.html')


def SHOP(request):
    return render(request,'/home/neosoft/PycharmProjects/DemoProject/mysite/eshopper/template/eshopper/shop.html')


def LOGIN(request):
    return render(request, '/home/neosoft/PycharmProjects/DemoProject/mysite/eshopper/template/eshopper/register.html')

def CART(request):
    return render(request,'/home/neosoft/PycharmProjects/DemoProject/mysite/eshopper/template/eshopper/cart.html')


def FOUR(request):
    return render(request,'/home/neosoft/PycharmProjects/DemoProject/mysite/eshopper/template/eshopper/four.html')


def BLOG(request):
    return render(request,'blog.html')


def BLOG_SINGLE(request):
    return render(request,'blog_single.html')


def CHECKOUT(request):
    return render(request,'checkout.html')


def PRODUCT_DETAILS(request):
    return render(request,'product_details.html')


def HandleRegister(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        customer = User.objects.create_user(username,email,pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('register')

    return render(request,'register.html')


def HandleLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('register')

    return render(request,'register.html')


def HandleLogout(request):
    logout(request)

    return redirect('eshopper')



