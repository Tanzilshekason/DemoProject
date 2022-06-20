from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='eshopper'),
    path('index/',views.INDEX,name='index'),
    path('base/',views.BASE,name='base'),
    path('contactus/',views.CONTACT,name='contact'),
    path('shop/',views.SHOP,name='shop'),
    path('login/',views.LOGIN,name='login'),
    path('cart/',views.CART,name='cart'),
    path('four/',views.FOUR,name='four'),
    path('blog/',views.BLOG,name='blog'),
    path('blog_single/',views.BLOG_SINGLE,name='blog_single'),
    path('checkout/',views.CHECKOUT,name='checkout'),
    path('product_details',views.PRODUCT_DETAILS,name='product_details')
]

