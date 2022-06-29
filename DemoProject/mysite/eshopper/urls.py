from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='eshopper'),
    path('index/',views.index1,name='index'),

    # urls for eshopper website
    path('base/',views.base,name='base'),
    path('contactus/',views.contact,name='contact'),
    path('shop/',views.shop,name='shop'),
    path('login/',views.Login,name='login'),
    path('cart/',views.cart,name='cart'),
    path('four/',views.four,name='four'),
    path('blog/',views.blog,name='blog'),
    path('blog_single/',views.blog_single,name='blog_single'),
    path('checkout/',views.checkout,name='checkout'),
    path('product_details/',views.product_details,name='product_details'),

    # urls for login and register
    path('register/',views.handle_register,name='register'),
    path('login1/',views.handle_login,name='login1'),
    path('logout/',views.handle_logout,name='logout'),
    path('account/',views.account,name='account'),
    path('edit_account/',views.edit_account,name='edit_account'),

    # urls for forgot password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    # add to  cart urls
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]

