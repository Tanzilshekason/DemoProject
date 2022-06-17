from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='eshopper'),
    path('base/',views.BASE,name='base'),
    path('contactus/',views.CONTACT,name='contact'),
    path('shop/',views.SHOP,name='shop'),
    path('login/',views.LOGIN,name='login'),
    # path('',views.HOME,name='home'),
]

