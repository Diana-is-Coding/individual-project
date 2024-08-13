from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Goods, List
from .forms import GoodsForm, ListForm
from django.contrib.auth.models import User
from user.models import Profile
from django.contrib import messages


# Create your views here.

@login_required
def index(request):
    
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            form.save()
            goods_name = form.cleaned_data.get('name')
            messages.success(request, f'{goods_name} has been added')
            return redirect('dashboard-index')
    else:
        form = GoodsForm()

    groceries = List.objects.all()

    context = {
        'form':form,
    }

    return render(request, 'dashboard/index.html', context)


@login_required
def users(request):
    customers = User.objects.all()
    user_count = customers.count()
    food_count= Goods.objects.all().count()
    list_count= List.objects.all().count()

    context={
        'customers':customers,
        'user_count':user_count,
        'food_count':food_count,
        'list_count':list_count,
    }
    return render (request, 'dashboard/users.html', context)

@login_required
def user_detail(request, pk):
    customers = User.objects.get(id=pk,)

    context={
        'customers':customers,
    }
    return render(request, 'dashboard/users_detail.html', context)


@login_required    
def goods(request):
    items = Goods.objects.all()
    food_count= items.count()
    user_count = User.objects.all().count()
    list_count= List.objects.all().count()
    
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            form.save()
            goods_name = form.cleaned_data.get('name')
            messages.success(request, f'{goods_name} has been added')
            return redirect('dashboard-index')
    else:
        form = GoodsForm()

    context = {
        'items':items,
        'form':form,
        'user_count': user_count,
        'food_count': food_count,
        'list_count': list_count,
    }
    return render (request, 'dashboard/goods.html', context)

@login_required    
def user_dash(request):
    items = Goods.objects.all()
    
    context = {
        'items':items,
    }
    return render (request, 'templates/dashboard/users_index.html', context)

@login_required
def goods_delete(request, pk):
    item = Goods.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-index')
    return render(request, 'dashboard/goods_delete.html')

@login_required
def goods_update(request, pk):
    item = Goods.objects.get(id=pk)
    
    if request.method == 'POST':
        form = GoodsForm(request.POST, instance= item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = GoodsForm()

    context = {
        'form':form,
    }
    return render(request, 'dashboard/goods_update.html')

@login_required
def list(request):
    groceries = List.objects.all()
    list_count= groceries.count()
    user_count = User.objects.all().count()
    food_count= Goods.objects.all().count()
    
    if 'groceries' not in request.session:
        request.session['groceries'] = []
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            groceries = request.session['groceries']
            groceries.append(item.name)
            request.session['groceries'] = groceries
            goods_name = form.cleaned_data.get('item')
            messages.success(request, f'{goods_name} has been added to your list')
            return redirect('dashboard-list')
        elif 'clear_list' in request.POST:
            request.session['groceries'] = []
            messages.success(request, 'The list has been cleared')
            return redirect('dashboard-list')
            
    else:
        form = ListForm()

    context={
        'form':form,
        'groceries':request.session['groceries'],
        'user_count':user_count,
        'food_count':food_count,
        'list_count':list_count,
    }
    return render (request,'dashboard/list.html', context)



