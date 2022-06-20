from django.shortcuts import render

# Create your views here.
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
    return render(request,'/home/neosoft/PycharmProjects/DemoProject/mysite/eshopper/template/eshopper/login.html')


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

