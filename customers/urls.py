from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customer, name='customer'),
    path('../customers/logout', views.logout, name='logout'),
    path('../customers/signup', views.logout, name='signup'),
]
