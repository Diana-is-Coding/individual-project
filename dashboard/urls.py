from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('food/', views.food, name='dashboard-food'),
    path('food/delete/<int:pk>/', views.food_delete, name='dashboard-food-delete'),
    path('food/update/<int:pk>/', views.food_update, name='dashboard-food-update'),
    path('users/', views.users, name='dashboard-users'),
    path('medicine/', views.medicine, name='dashboard-medicine'),
    path('medicine/delete/<int:pk>/', views.medicine_delete, name='dashboard-med-delete'),
    path('medicine/update/<int:pk>/', views.medicine_update, name='dashboard-med-update'),
    path('list/', views.list, name='dashboard-list'),
]