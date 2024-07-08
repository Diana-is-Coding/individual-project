from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1 style= 'color: teal;'>This is the Index Page! Well Done!!</h1>")

def staff(request):
    return HttpResponse('This is the Staff Page! Doing Good!!')