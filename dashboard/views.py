from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Food, Medicine
from .forms import FoodForm, MedicineForm

# Create your views here.

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def users(request):
    return render (request, 'dashboard/users.html')

@login_required    
def food(request):
    food_items = Food.objects.all()
    
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-food')
    else:
        food_form = FoodForm()

    context = {
        'food_items':food_items,
        'food_form':food_form,
    }
    return render (request, 'dashboard/food.html', context)

@login_required
def food_delete(request, pk):
    food_item = Food.objects.get(id=pk)
    if request.method == 'POST':
        food_item.delete()
        return redirect('dashboard-food')
    return render(request, 'dashboard/food_delete.html')

@login_required
def medicine_delete(request, pk):
    med_item = Medicine.objects.get(id=pk)
    if request.method == 'POST':
        med_item.delete()
        return redirect('dashboard-medicine')
    return render(request, 'dashboard/medicine_delete.html')

@login_required
def food_update(request, pk):
    food_item = Food.objects.get(id=pk)
    
    if request.method == 'POST':
        form = FoodForm(request.POST, instance= food_item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-food')
    else:
        food_form = FoodForm()

    context = {
        'food_form':food_form,
    }
    return render(request, 'dashboard/food_update.html')

@login_required
def medicine_update(request, pk):
    med_item = Medicine.objects.get(id=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance= med_item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-medicine')
    else:
        med_form = MedicineForm(instance= med_item)

    context={
        'med_form':med_form,
    }
    return render(request, 'dashboard/medicine_update.html')

@login_required   
def medicine(request):
    med_items = Medicine.objects.all()
    
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-medicine')
    else:
        med_form = MedicineForm()
        
    context = {
        'med_items':med_items,
        'med_form':med_form
    }
    return render (request, 'dashboard/medicine.html', context)

@login_required
def list(request):
    return render (request, 'dashboard/list.html')