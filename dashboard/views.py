from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Goods, List
from .forms import GoodsForm
from django.contrib.auth.models import User
from user.models import Profile

# Create your views here.

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
# @allowed_users(allowed_roles=['Admin'])
def users(request):
    customers = User.objects.all()
    context={
        'customers':customers
    }
    return render (request, 'dashboard/users.html', context)

@login_required
# @allowed_users(allowed_roles=['Admin'])
def user_detail(request, pk):
    customers = User.objects.get(id=pk)
    context={
        'customers':customers
    }
    return render(request, 'dashboard/user_detail.html', context)


@login_required    
def goods(request):
    items = Goods.objects.all()
    
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-goods')
    else:
        form = GoodsForm()

    context = {
        'items':items,
        'form':form,
    }
    return render (request, 'dashboard/goods.html', context)

@login_required
def goods_delete(request, pk):
    item = Goods.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-goods-delete')
    return render(request, 'dashboard/goods_delete.html')

@login_required
def goods_update(request, pk):
    item = Goods.objects.get(id=pk)
    
    if request.method == 'POST':
        form = GoodsForm(request.POST, instance= item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-goods-update')
    else:
        form = GoodsForm()

    context = {
        'form':form,
    }
    return render(request, 'dashboard/goods_update.html')

@login_required
def list(request):
    groceries = List.objects.all()

    context={
        'groceries':groceries,
    }
    return render (request, 'dashboard/list.html', context)