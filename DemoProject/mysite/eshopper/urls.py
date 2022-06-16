from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='eshopper'),
    # path('base/',views.BASE,name='base'),
    # path('',views.HOME,name='home')
]

