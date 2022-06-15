from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from adminpanel.models import Manage_user
from adminpanel.models import Category

def index(request):
    return render(request, 'starter.html')

# For Register and Login page
def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'

    else:
        form = SignUpForm()
    return render(request,'register.html',{'form':form, 'msg':msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')

            elif user is not None and user.is_manager:
                login(request, user)
                return redirect('manager')


            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form':form, 'msg':msg})


# For admin,customer and order page.
def admin(request):
    return render(request, 'admin.html')

def customer(request):
    return render(request, 'customer.html')

def manager(request):
    return render(request, 'manager.html')


# For CRUD Operations
def INDEX(request):
    emp = Manage_user.objects.all()

    context = {
        'emp':emp,
    }
    return render(request, 'crud.html',context)

def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Manage_user(
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()
        return redirect('home')

    return render(request,'crud.html',)

def Edit(request):
    emp = Manage_user.objects.all()

    context = {
        'emp':emp,
    }

    return redirect(request,'crud.html',context)


def UPDATE(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Manage_user(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home')

    return redirect(request,'crud.html')

def Delete(request,id):
    emp = Manage_user.objects.filter(id=id)
    emp.delete()
    context = {
        'emp':emp,
    }

    return redirect('home')

def Index(request):
    category = Category.objects.all()

    context = {
        'category': category
    }
    return render(request,context)
