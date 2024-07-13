from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def users(request):
    return render (request, 'dashboard/users.html')
    
def pantry(request):
    return render (request, 'dashboard/pantry.html')
    
def chilled(request):
    return render (request, 'dashboard/chilled.html')

def frozen(request):
    return render (request, 'dashboard/frozen.html')

def order(request):
    return render (request, 'dashboard/order.html')