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

from decimal import Decimal, InvalidOperation
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Product

def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category.category_name = form.cleaned_data['category_name']
            category.description = form.cleaned_data['description']
            category.save()
            return redirect('home')
    else:
        form = CategoryForm(initial={
            'category_name': category.category_name,
            'description': category.description,
        })
    return render(request, 'update_category.html', {'form': form})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # unit_price ni tozalaymiz
                price = form.cleaned_data['unit_price']
                if isinstance(price, str):
                    price = price.replace(',', '').strip()  # "1,200" => "1200"

                product.product_name = form.cleaned_data['product_name']
                product.unit_price = Decimal(price)
                product.category = form.cleaned_data['category']
                product.suppliers = form.cleaned_data['suppliers']

                if form.cleaned_data.get('photo'):
                    product.photo = form.cleaned_data['photo']

                product.save()
                return redirect('home')

            except InvalidOperation:
                form.add_error('unit_price', 'Narxni to‘g‘ri raqamda kiriting (masalan: 1200.50)')
    else:
        form = ProductForm(initial={
            'product_name': product.product_name,
            'unit_price': product.unit_price,
            'category': product.category,
            'suppliers': product.suppliers,
        })

    return render(request, 'update_product.html', {'form': form})



def update_suppliers(request, pk):
    supplier = get_object_or_404(Suppliers, pk=pk)
    if request.method == 'POST':
        form = SuppliersForm(request.POST)
        if form.is_valid():
            supplier.company_name = form.cleaned_data['company_name']
            supplier.contact_name = form.cleaned_data['contact_name']
            supplier.contact_title = form.cleaned_data['contact_title']
            supplier.address = form.cleaned_data['address']
            supplier.city = form.cleaned_data['city']
            supplier.region = form.cleaned_data['region']
            supplier.country = form.cleaned_data['country']
            supplier.phone = form.cleaned_data['phone']
            supplier.save()
            return redirect('home')
    else:
        form = SuppliersForm(initial={
            'company_name': supplier.company_name,
            'contact_name': supplier.contact_name,
            'contact_title': supplier.contact_title,
            'address': supplier.address,
            'city': supplier.city,
            'region': supplier.region,
            'country': supplier.country,
            'phone': supplier.phone,
        })
    return render(request, 'update_suppliers.html', {'form': form})

def update_order_details(request, pk):
    order_detail = get_object_or_404(Order_details, pk=pk)
    if request.method == 'POST':
        form = Order_detailsForm(request.POST)
        if form.is_valid():
            order_detail.product = form.cleaned_data['product']
            order_detail.unit_price = form.cleaned_data['unit_price']
            order_detail.quantity = form.cleaned_data['quantity']
            order_detail.save()
            return redirect('home')
    else:
        form = Order_detailsForm(initial={
            'product': order_detail.product,
            'unit_price': order_detail.unit_price,
            'quantity': order_detail.quantity,
        })
    return render(request, 'update_order_details.html', {'form': form})

def update_orders(request, pk):
    order = get_object_or_404(Orders, pk=pk)
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            order.order_date = form.cleaned_data['order_date']
            order.required_date = form.cleaned_data['required_date']
            order.order_dtls = form.cleaned_data['order_dtls']
            order.save()
            return redirect('home')
    else:
        form = OrdersForm(initial={
            'order_date': order.order_date,
            'required_date': order.required_date,
            'order_dtls': order.order_dtls,
        })
    return render(request, 'update_orders.html', {'form': form})
