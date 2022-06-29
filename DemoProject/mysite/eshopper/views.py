from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from adminpanel.models import categorys, products, brands
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
# from django.contrib import messages

User = get_user_model()

# Create your views here.
def index(request):
    category = categorys.objects.all()
    brand = brands.objects.all()
    brandId = request.GET.get('brand')
    categoryID = request.GET.get('category')
    if categoryID:
        product = products.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandId:
        product = products.objects.filter(brand=brandId).order_by('-id')
    else:
        product = products.objects.all()

    context = {
        'category':category,
        'product':product,
        'brand':brand,
    }
    return render(request,'eshopper/index.html',context)


def index1(request):
    category = categorys.objects.all()
    product = products.objects.all()

    context = {
        'category': category,
        'product': product,
    }
    return render(request,'eshopper/index1.html',context)

def base(request):
    return render(request, 'eshopper/base.html')


def contact(request):
    return render(request,'eshopper/contactus.html')


def shop(request):
    category = categorys.objects.all()
    brand = brands.objects.all()
    brandId = request.GET.get('brand')
    categoryID = request.GET.get('category')
    if categoryID:
        product = products.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandId:
        product = products.objects.filter(brand=brandId).order_by('-id')
    else:
        product = products.objects.all()

    context = {
        'category': category,
        'product': product,
        'brand': brand,
    }
    return render(request,'eshopper/shop.html',context)


def Login(request):
    return render(request, 'eshopper/register.html')

def cart(request):
    return render(request,'eshopper/cart.html')


def four(request):
    return render(request,'eshopper/four.html')


def blog(request):
    return render(request,'eshopper/blog.html')


def blog_single(request):
    return render(request,'eshopper/blog_single.html')


def checkout(request):
    return render(request,'eshopper/checkout.html')


def product_details(request):
    # product = products.objects.filter(id=id).first()
    # context = {
    #     'product':product
    # }
    return render(request,'eshopper/product_details.html')



# Register and lohgin page views
def handle_register(request):
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

    return render(request,'eshopper/register.html')


def handle_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('register')

    return render(request,'eshopper/register.html')


def handle_logout(request):
    logout(request)

    return redirect('eshopper')



# views for My Account of user

def account(request):
    return render(request,'eshopper/account.html')

def edit_account(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        return redirect('account')

    return render(request,'eshopper/edit_account.html')



# add to cart code

@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = products.objects.get(id=id)
    cart.add(product=product)
    return redirect('eshopper')


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'eshopper/cart_detail.html')

