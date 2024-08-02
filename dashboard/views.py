from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Food, Medicine

# Create your views here.

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def users(request):
    return render (request, 'dashboard/users.html')

@login_required    
def food(request):
    return render (request, 'dashboard/food.html')

@login_required   
def medicine(request):
    return render (request, 'dashboard/medicine.html')

@login_required
def list(request):
    return render (request, 'dashboard/list.html')