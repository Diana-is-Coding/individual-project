from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),        
    path('users/', views.users, name='dashboard-users'),
    path('pantry/', views.pantry, name='dashboard-pantry'),
    path('chilled/', views.chilled, name='dashboard-chilled'),
    path('frozen/', views.frozen, name='dashboard-frozen'),
    path('order/', views.order, name='dashboard-order'),
]