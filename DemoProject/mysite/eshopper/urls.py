from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ProductListView

urlpatterns = [
    path('',views.index,name='eshopper'),
    path('index/',views.index1,name='index'),

    # urls for eshopper website
    path('base/',views.base,name='base'),
    path('contactus/',views.contact,name='contact'),
    path('login/',views.Login,name='login'),
    path('cart/',views.cart,name='cart'),
    path('blog/',views.blog,name='blog'),
    path('blog_single/',views.blog_single,name='blog_single'),
    path('checkout/',views.checkout,name='checkout'),
    path('checkout/placeorder/',views.place_order,name='place_order'),
    path('success',views.success,name='success'),

    path('product_detail/<int:id>/',views.product_details,name='product_details'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('wishlist/add/<int:id>/', views.wishlist_add, name='wishlist_add'),

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
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-details/', views.cart_details, name='cart_details'),

    # add to cart updated urls
    path('update/',views.update,name='update'),
    path('cart/cart_add/<int:id>/', views.addtocart, name='cart_add'),
    path('cart/delete_cart_item/', views.delete_cart_item, name='delete_cart_item'),
    path('cart/update_quantity/',views.update_quantity,name='update_quantity'),
    path('cart/cart_count/', views.cart_count, name='cart_count'),


    path('product_list',ProductListView.as_view(),name='product_list'),
]

