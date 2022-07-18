from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from adminpanel.models import Categorys, Products, Brands, Contactus,FilterPrices,Images,Subcategory,Configuration,Order
from adminpanel.models import OrderItem, CouponCode
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from requests import session
from wishlist import Wishlist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
import datetime
from adminpanel.models import *
# from django.contrib import messages
import razorpay
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))


User = get_user_model()
session_key = 'cart'

# Create your views here.
def index(request):
    category = Categorys.objects.all()
    brand = Brands.objects.all()
    filter_price = FilterPrices.objects.all()
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
    payment = client.order.create({
        "amount":500,
        "currency":"INR",
        "payment_capture":"1"
        })

    order_id = payment['id']

    coupon = None
    valid_coupon = None
    invalid_coupon = None

    if request.method == "GET":
        coupon_code = request.GET.get('coupon_code')
        if coupon_code:
            try:
                coupon = CouponCode.objects.get(code=coupon_code)
                valid_coupon = "Are Applicable on Current Order !"
            except:
                invalid_coupon = "Invalid Coupon Code !"

    context = {
        'order_id': order_id,
        'payment': payment,
        'coupon':coupon,
        'valid_coupon':valid_coupon,
        'invalid_coupon':invalid_coupon,
    }

    return render(request,'checkout.html',context)


def place_order(request):
    if request.method == "POST":
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id=uid)
        cart = request.session.get('cart')
        print(cart)
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country = request.POST.get('country')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        amount = request.POST.get('amount')

        order_id = request.POST.get('order_id')
        payment = request.POST.get('payment')

        context = {
            'order_id':order_id,
            'payment':payment,
        }

        order = Order(
            user=user,
            firstname=firstname,
            lastname=lastname,
            country=country,
            city=city,
            address=address,
            state=state,
            postcode=postcode,
            phone=phone,
            email=email,
            payment_id=order_id,
            amount=amount,
        )
        order.save()


        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b

            item = OrderItem(
                order=order,
                product=cart[i]['name'],
                image=cart[i]['image'],
                quantity=cart[i]['quantity'],
                price=cart[i]['price'],
                total=total
            )
            item.save()

    return render(request,'placeorder.html',context)

@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'paypal_order_id':
                order_id = val
                break

        user = Order.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
        request.session['cart'] = {}

    return render(request,"thank.html")



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
    return render(request, "eshopper/cart_detail.html")



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









def create_session(request):
    try:
        dic = request.session[session_key]
    except:
        dic = {}
    return dic

def update(dic, id):
    for index, object in dic.items():
        for key, value in object.items():
            if index == id:
                if key == 'quantity':
                    object[key] = object[key] + 1
        dic[index] = object
    return dic

def addtocart(request, id):
    dic = create_session(request)
    request.session[session_key] = dic

    product = Products.objects.get(id=id)
    name = product.name
    price = product.price
    image = product.image.url
    if product.special_price and product.special_price_to > datetime.datetime.now().date() > product.special_price_from:
        price = product.special_price

    if id not in dic.keys():
        quantity = 1
        dic[id] = {'id':id,'quantity':quantity,'price':price,'name':name,'image':image}
        request.session[session_key] = dic
    else:
        if dic[id]['quantity'] < product.quantity:
            myDic = update(dic,id)
            request.session[session_key] = myDic
        else:
            obj_json = json.dumps({'status': 'Out of Range'})
            return HttpResponse(obj_json, content_type='application/json')

    obj_json = json.dumps({'status': 'Done','cart_count': len(request.session[session_key])})
    return HttpResponse(obj_json, content_type='application/json')


class Cartview(View):
    template_name = 'templates/eshopper/cart_detail.html'

    def get(self, request):
        """

        :param request:
        :return:
        """
        count = 0
        product_dic = {}
        try:
            dic = request.session[session_key]
            for id in dic:
                prod = Products.objects.get(id=id)
                image = prod.image.all()
                product_dic[id] = {'product': prod, 'image': image[0]}

            object = Configuration.objects.get(conf_key='Tax')
            return render(request, self.template_name,
                          {'dic': dic, 'dic2': product_dic, 'configuration': object})
        except:
            dic = {}
            return render(request, self.template_name, {'dic': dic})


def delete_cart_item(request, mykey):
    """

    :param mykey:
    :param request:
    :return:
    """
    dic = request.session[session_key]
    del (dic[mykey])
    request.session[session_key] = dic
    if dic == {}:
        obj_json = json.dumps({'status': 'none'})
        return HttpResponse(obj_json, content_type='application/json')
    obj_json = json.dumps({'status': 'Done'})
    return HttpResponse(obj_json, content_type='application/json')


def update_quantity(request, mykey):
    """

    :param mykey:
    :param request:
    :return:
    """
    dic = request.session[session_key]
    obj = Products.objects.get(id=int(mykey))
    if obj.quantity > dic[mykey]['quantity']:
        dic_updated = update(dic, mykey)
        request.session[session_key] = dic_updated
        obj_json = json.dumps(dic_updated[mykey])
        return HttpResponse(obj_json, content_type='application/json')
    else:
        return HttpResponse('Out of Range')


def downgrade_quantity(request, mykey):
    """

    :param request:
    :param mykey:
    :return:
    """
    dic = request.session[session_key]

    for index, object in dic.items():
        for key, value in object.items():
            if index == mykey:
                if key == 'quantity':
                    object[key] = object[key] - 1
        dic[index] = object
    request.session[session_key] = dic
    obj_json = json.dumps(dic[mykey])
    return HttpResponse(obj_json, content_type='application/json')


def cart_count(request):
    cart_dic = session(request)
    obj_json = json.dumps({'status': len(cart_dic)})
    return HttpResponse(obj_json, content_type='application/json')


