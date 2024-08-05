from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('goods/', views.goods, name='dashboard-goods'),
    path('goods/delete/<int:pk>/', views.goods_delete, name='dashboard-goods-delete'),
    path('goods/update/<int:pk>/', views.goods_update, name='dashboard-goods-update'),
    path('users/', views.users, name='dashboard-users'),
    path('users/detail/<int:pk>/', views.user_detail, name='dashboard-user-detail'),
    path('list/', views.list, name='dashboard-list'),
]