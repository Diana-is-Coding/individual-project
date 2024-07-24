from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('food/', views.food, name='dashboard-food'),        
    path('users/', views.users, name='dashboard-users'),
    path('medicine/', views.medicine, name='dashboard-medicine'),
    path('list/', views.list, name='dashboard-list'),
]