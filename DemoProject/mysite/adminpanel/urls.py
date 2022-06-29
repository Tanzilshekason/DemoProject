from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="adminpanel"),
    # path('login/',views.login_view,name='login_view'),
    # path('register/',views.register,name='register'),
    path('adminpage/', views.admin, name='admin'),
    path('customer', views.customer, name='customer'),
    path('order', views.customer, name='order'),
    # path('home/',views.index1, name='home'),
    # path('add',views.add,name='add'),
    # path('edit',views.edit,name='edit'),
    # path('update/<str:id>',views.update,name='update'),
    # path('delete/<str:id>',views.delete,name='delete'),

]
