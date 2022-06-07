from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="app"),
    path('login/',views.login_view,name='login_view'),
    path('register',views.register,name='register'),
    path('home', views.home, name='home')
]
