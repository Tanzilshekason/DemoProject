from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def BASE(request):
    return render(request, '/home/neosoft/PycharmProjects/DemoProject/mysite/eshopper/template/eshopper/base.html')

#
# def HOME(request):
#     return render(request,'index1.html')

def CONTACT(request):
    return render(request,'/home/neosoft/PycharmProjects/DemoProject/mysite/eshopper/template/eshopper/contactus.html')


def SHOP(request):
    return render(request,'/home/neosoft/PycharmProjects/DemoProject/mysite/eshopper/template/eshopper/shop.html')


def LOGIN(request):
    return render(request,'/home/neosoft/PycharmProjects/DemoProject/mysite/eshopper/template/eshopper/login.html')


