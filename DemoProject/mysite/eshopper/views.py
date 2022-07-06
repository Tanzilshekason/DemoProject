from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from adminpanel.models import Categorys, Products, Brands, Contactus,Filterprices,Images,Subcategory
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
# from wishlist import Wishlist
from django.http import JsonResponse
from django.views.generic import View
# from django.contrib import messages

User = get_user_model()

# Create your views here.
def index(request):
    category = Categorys.objects.all()
    brand = Brands.objects.all()
    filter_price = Filterprices.objects.all()
    brandId = request.GET.get('brand')
    categoryID = request.GET.get('category')
    PRICE_FILTER_ID = request.GET.get('filter_price')
    if categoryID:
        product = Products.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandId:
        product = Products.objects.filter(brand=brandId).order_by('-id')
    elif PRICE_FILTER_ID:
        product = Products.objects.filter(filter_price=PRICE_FILTER_ID)
    else:
        product = Products.objects.all()

    context = {
        'category':category,
        'product':product,
        'brand':brand,
        'filter_price':filter_price
    }
    return render(request,'eshopper/index.html',context)


def index1(request):
    category = Categorys.objects.all()
    product = Products.objects.all()

    context = {
        'category': category,
        'product': product,
    }
    return render(request,'eshopper/index1.html',context)

def base(request):
    return render(request, 'eshopper/base.html')


def contact(request):
    if request.method == "POST":
        contact = Contactus(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            # contact_no=request.POST.get('contact_no'),
            message=request.POST.get('message'),
            # note_adm=request.POST.get('note_adm'),
            # created_by=request.POST.get('created_by'),
            # created_date=request.POST.get('created_date'),
            # modify_by=request.POST.get('modify_by'),
            # modify_date=request.POST.get('modify_date'),
        )
        contact.save()
    return render(request,'eshopper/contactus.html')

def Login(request):
    return render(request, 'eshopper/register.html')

def cart(request):
    return render(request,'eshopper/cart.html')

def blog(request):
    return render(request,'eshopper/blog.html')


def blog_single(request):
    return render(request,'eshopper/blog_single.html')


def checkout(request):
    return render(request,'eshopper/checkout.html')


def product_details(request,id):
    category = Categorys.objects.all()
    brand = Brands.objects.all()
    product = Products.objects.filter(id=id).first()
    # product = products.objects.filter(id=id).first()
    image_list = Images.objects.filter(product=product)

    context = {
        'category': category,
        'brand':brand,
        'product':product,
        'image_list': image_list,
    }
    return render(request,'eshopper/product_details.html',context)


def wishlist(request):
    return render(request,'wishlist.html')


@login_required(login_url="/login/")
def wishlist_add(request, id):
    wishlist = Wishlist(request)
    product = Products.objects.get(id=id)
    wishlist.add(product=product)
    return redirect('wishlist')


# Register and login page views
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
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect('eshopper')


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
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

# class ProductListView(View):
#     def get(request):
#         # text = request.GET.get('button_text')
#         #
#         # if request.is_ajax():
#         #     t = time()
#         #     return JsonResponse({'seconds': t}, status=200)
#
#         category = request.GET.get('category')
#         brand = request.GET.get('brand')
#         startprice = request.GET.get('filter_price')
#         endprice = request.GET.get('filter_price')
#
#
#         return render(request,'eshopper/index.html')


class ProductListView(View):
    def get(self,request):
        category = request.GET.get('category')
        brand = request.GET.get('brand')
        startprice = request.GET.get('price_filter')
        endprice = request.GET.get('price_filter')

        product_queryset = Products.objects.all()
        if category:
            sub_category = Subcategory.objects.filter(name=category).first()
            product_queryset = product_queryset.filter(sub_category=sub_category)
        if brand:
            brand = Brands.objects.filter(name=brand).first()
            product_queryset = product_queryset.filter(brand=brand)
        if startprice:
            product_queryset = product_queryset.filter(price__gte=int(startprice))
        if endprice:
            product_queryset = product_queryset.filter(price__lte=int(endprice))

        product_list = list(product_queryset.values())
        print(product_list)
        context = {
            'products': product_list
        }
        return JsonResponse(context,safe=False)




