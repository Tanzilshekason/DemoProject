from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')


# def BASE(request):
#     return render(request, '/home/neosoft/PycharmProjects/DemoProject/mysite/eshopper/template/eshopper/base.html')
#
#
# def HOME(request):
#     return render(request,'index1.html')

