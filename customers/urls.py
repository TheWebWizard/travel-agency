from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customer, name='customer'),
    path('../accounts/logout', views.logout, name='logout'),
]
