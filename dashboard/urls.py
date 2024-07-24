from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),        
    path('users/', views.users, name='dashboard-users'),
    path('kitchen/', views.kitchen, name='dashboard-kitchen'),
    path('medicine/', views.medicine, name='dashboard-medicine'),
    path('list/', views.list, name='dashboard-list'),
]