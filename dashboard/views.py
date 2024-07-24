from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def users(request):
    return render (request, 'dashboard/users.html')
    
def food(request):
    return render (request, 'dashboard/food.html')
    
def medicine(request):
    return render (request, 'dashboard/medicine.html')

def list(request):
    return render (request, 'dashboard/list.html')