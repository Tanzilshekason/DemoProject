from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

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
    path('product_details/',views.PRODUCT_DETAILS,name='product_details'),
    path('register/',views.HandleRegister,name='register'),
    path('login1/',views.HandleLogin,name='login1'),
    path('logout/',views.HandleLogout,name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]

