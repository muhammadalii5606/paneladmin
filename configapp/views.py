# from importlib.resources import contents

from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from .forms import *


def index(request):
    cat = Category.objects.all()
    pro = Product.objects.all()
    content = {
        "cat":cat,
        "pro":pro,
    }

    return render(request,'index.html',content)


def category(request, pk):
    pro = Product.objects.filter(category=pk)
    category = Category.objects.all()
    content = {
        "pro":pro,
        "category":category
    }

    return render(request,'category.html',content)



def add_category(request):
    if request.method == 'POST':
        # print("=========", request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            # print("======",form.cleaned_data)
            category = Category.objects.create(**form.cleaned_data)
            return redirect('home')


    else:
        form = CategoryForm()

    return render(request,'add_category.html',{'form':form})




def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = ProductForm()

    return render(request,"add_product.html",{"form":form})



def add_suppliers(request):
    if request.method == 'POST':
        form = SuppliersForm(request.POST)
        if form.is_valid():
            suppliers = Suppliers.objects.create(**form.cleaned_data)
            return redirect('home')

    else:
        form = SuppliersForm()

    return render(request,"add_suppliers.html",{"form":form})

def add_order_details(request):
    if request.method =='POST':
        form = Order_detailsForm(request.POST)
        if form.is_valid():
            order_details = Order_details.objects.create(**form.cleaned_data)
            return redirect('home')

    else:
        form = Order_detailsForm()

    return render(request,"add_order_details.html", {"form":form})


def add_orders(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            Orders.objects.create(
                order_date=data['order_date'],
                required_date=data['required_date'],
                order_dtls=data['order_dtls']
            )

            return redirect('home')

    else:
        form = OrdersForm()

    return render(request, "add_orders.html", {"form": form})

from django.shortcuts import get_object_or_404


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('home')


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('home')


def delete_suppliers(request, pk):
    supplier = get_object_or_404(Suppliers, pk=pk)
    supplier.delete()
    return redirect('home')


def delete_order_details(request, pk):
    order_detail = get_object_or_404(Order_details, pk=pk)
    order_detail.delete()
    return redirect('home')


def delete_orders(request, pk):
    order = get_object_or_404(Orders, pk=pk)
    order.delete()
    return redirect('home')
