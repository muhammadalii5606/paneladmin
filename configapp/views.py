# from importlib.resources import contents
# from django.shortcuts import render, redirect
# from .models import *
# from django.http import HttpResponse
# from .forms import *
# from decimal import Decimal, InvalidOperation
# from django.shortcuts import render, get_object_or_404, redirect
# from .forms import ProductForm
# from .models import Product
# from django.shortcuts import get_object_or_404
#
#
# def index(request):
#     cat = Category.objects.all()
#     pro = Product.objects.all()
#     content = {
#         "cat":cat,
#         "pro":pro,
#     }
#
#     return render(request,'index.html',content)
# def category(request, pk):
#     pro = Product.objects.filter(category=pk)
#     category = Category.objects.all()
#     content = {
#         "pro":pro,
#         "category":category
#     }
#
#     return render(request,'category.html',content)
#
# def add_category(request):
#     if request.method == 'POST':
#         # print("=========", request.POST)
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             # print("======",form.cleaned_data)
#             category = Category.objects.create(**form.cleaned_data)
#             return redirect('home')
#
#
#     else:
#         form = CategoryForm()
#
#     return render(request,'add_category.html',{'form':form})
# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = Product.objects.create(**form.cleaned_data)
#             return redirect('home')
#     else:
#         form = ProductForm()
#
#     return render(request,"add_product.html",{"form":form})
# def add_suppliers(request):
#     if request.method == 'POST':
#         form = SuppliersForm(request.POST)
#         if form.is_valid():
#             suppliers = Suppliers.objects.create(**form.cleaned_data)
#             return redirect('home')
#
#     else:
#         form = SuppliersForm()
#
#     return render(request,"add_suppliers.html",{"form":form})
# def add_order_details(request):
#     if request.method =='POST':
#         form = Order_detailsForm(request.POST)
#         if form.is_valid():
#             order_details = Order_details.objects.create(**form.cleaned_data)
#             return redirect('home')
#
#     else:
#         form = Order_detailsForm()
#
#     return render(request,"add_order_details.html", {"form":form})
# def add_orders(request):
#     if request.method == 'POST':
#         form = OrdersForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#
#             Orders.objects.create(
#                 order_date=data['order_date'],
#                 required_date=data['required_date'],
#                 order_dtls=data['order_dtls']
#             )
#
#             return redirect('home')
#
#     else:
#         form = OrdersForm()
#
#     return render(request, "add_orders.html", {"form": form})
#
# def delete_category(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     category.delete()
#     return redirect('home')
# def delete_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     product.delete()
#     return redirect('home')
# def delete_suppliers(request, pk):
#     supplier = get_object_or_404(Suppliers, pk=pk)
#     supplier.delete()
#     return redirect('home')
# def delete_order_details(request, pk):
#     order_detail = get_object_or_404(Order_details, pk=pk)
#     order_detail.delete()
#     return redirect('home')
# def delete_orders(request, pk):
#     order = get_object_or_404(Orders, pk=pk)
#     order.delete()
#     return redirect('home')
#
# def update_category(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             category.category_name = form.cleaned_data['category_name']
#             category.description = form.cleaned_data['description']
#             category.save()
#             return redirect('home')
#     else:
#         form = CategoryForm(initial={
#             'category_name': category.category_name,
#             'description': category.description,
#         })
#     return render(request, 'update_category.html', {'form': form})
# def update_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 # unit_price ni tozalaymiz
#                 price = form.cleaned_data['unit_price']
#                 if isinstance(price, str):
#                     price = price.replace(',', '').strip()  # "1,200" => "1200"
#
#                 product.product_name = form.cleaned_data['product_name']
#                 product.unit_price = Decimal(price)
#                 product.category = form.cleaned_data['category']
#                 product.suppliers = form.cleaned_data['suppliers']
#
#                 if form.cleaned_data.get('photo'):
#                     product.photo = form.cleaned_data['photo']
#
#                 product.save()
#                 return redirect('home')
#
#             except InvalidOperation:
#                 form.add_error('unit_price', 'Narxni to‘g‘ri raqamda kiriting (masalan: 1200.50)')
#     else:
#         form = ProductForm(initial={
#             'product_name': product.product_name,
#             'unit_price': product.unit_price,
#             'category': product.category,
#             'suppliers': product.suppliers,
#         })
#
#     return render(request, 'update_product.html', {'form': form})
# def update_suppliers(request, pk):
#     supplier = get_object_or_404(Suppliers, pk=pk)
#     if request.method == 'POST':
#         form = SuppliersForm(request.POST)
#         if form.is_valid():
#             supplier.company_name = form.cleaned_data['company_name']
#             supplier.contact_name = form.cleaned_data['contact_name']
#             supplier.contact_title = form.cleaned_data['contact_title']
#             supplier.address = form.cleaned_data['address']
#             supplier.city = form.cleaned_data['city']
#             supplier.region = form.cleaned_data['region']
#             supplier.country = form.cleaned_data['country']
#             supplier.phone = form.cleaned_data['phone']
#             supplier.save()
#             return redirect('home')
#     else:
#         form = SuppliersForm(initial={
#             'company_name': supplier.company_name,
#             'contact_name': supplier.contact_name,
#             'contact_title': supplier.contact_title,
#             'address': supplier.address,
#             'city': supplier.city,
#             'region': supplier.region,
#             'country': supplier.country,
#             'phone': supplier.phone,
#         })
#     return render(request, 'update_suppliers.html', {'form': form})
# def update_order_details(request, pk):
#     order_detail = get_object_or_404(Order_details, pk=pk)
#     if request.method == 'POST':
#         form = Order_detailsForm(request.POST)
#         if form.is_valid():
#             order_detail.product = form.cleaned_data['product']
#             order_detail.unit_price = form.cleaned_data['unit_price']
#             order_detail.quantity = form.cleaned_data['quantity']
#             order_detail.save()
#             return redirect('home')
#     else:
#         form = Order_detailsForm(initial={
#             'product': order_detail.product,
#             'unit_price': order_detail.unit_price,
#             'quantity': order_detail.quantity,
#         })
#     return render(request, 'update_order_details.html', {'form': form})
# def update_orders(request, pk):
#     order = get_object_or_404(Orders, pk=pk)
#     if request.method == 'POST':
#         form = OrdersForm(request.POST)
#         if form.is_valid():
#             order.order_date = form.cleaned_data['order_date']
#             order.required_date = form.cleaned_data['required_date']
#             order.order_dtls = form.cleaned_data['order_dtls']
#             order.save()
#             return redirect('home')
#     else:
#         form = OrdersForm(initial={
#             'order_date': order.order_date,
#             'required_date': order.required_date,
#             'order_dtls': order.order_dtls,
#         })
#     return render(request, 'update_orders.html', {'form': form})



from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from decimal import Decimal, InvalidOperation

from .models import Category, Product, Suppliers, Order_details, Orders
from .forms import (
    CategoryForm, ProductForm, SuppliersForm,
    Order_detailsForm, OrdersForm
)

# ==================== HOME PAGE ====================
class HomeView(View):
    def get(self, request):
        cat = Category.objects.all()
        pro = Product.objects.all()
        return render(request, "index.html", {"cat": cat, "pro": pro})


# ==================== CATEGORY PAGES ====================
class CategoryProductsView(View):
    def get(self, request, pk):
        pro = Product.objects.filter(category=pk)
        category = Category.objects.all()
        return render(request, 'category.html', {"pro": pro, "category": category})


class AddCategoryView(View):
    def get(self, request):
        return render(request, "add_category.html", {"form": CategoryForm()})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(
                category_name=form.cleaned_data['category_name'],
                description=form.cleaned_data.get('description', '')
            )
            return redirect("home")
        return render(request, "add_category.html", {"form": form})


class UpdateCategoryView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(initial={
            "category_name": category.category_name,
            "description": category.description
        })
        return render(request, "update_category.html", {"form": form})

    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(request.POST)
        if form.is_valid():
            category.category_name = form.cleaned_data["category_name"]
            category.description = form.cleaned_data["description"]
            category.save()
            return redirect("home")
        return render(request, "update_category.html", {"form": form})


class DeleteCategoryView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect("home")


# ==================== PRODUCT VIEWS ====================
class AddProductView(View):
    def get(self, request):
        return render(request, "add_product.html", {"form": ProductForm()})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                price = Decimal(form.cleaned_data['unit_price'])
            except InvalidOperation:
                form.add_error("unit_price", "Narxni to‘g‘ri kiriting!")
                return render(request, "add_product.html", {"form": form})

            Product.objects.create(
                product_name=form.cleaned_data["product_name"],
                unit_price=price,
                category=form.cleaned_data["category"],
                suppliers=form.cleaned_data["suppliers"],
                photo=form.cleaned_data["photo"]
            )
            return redirect("home")

        return render(request, "add_product.html", {"form": form})


class UpdateProductView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(initial={
            "product_name": product.product_name,
            "unit_price": product.unit_price,
            "category": product.category,
            "suppliers": product.suppliers,
        })
        return render(request, "update_product.html", {"form": form})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                price = Decimal(form.cleaned_data['unit_price'])
            except InvalidOperation:
                form.add_error("unit_price", "Raqam kiriting!")
                return render(request, "update_product.html", {"form": form})

            product.product_name = form.cleaned_data["product_name"]
            product.unit_price = price
            product.category = form.cleaned_data["category"]
            product.suppliers = form.cleaned_data["suppliers"]

            if request.FILES.get("photo"):
                product.photo = form.cleaned_data["photo"]

            product.save()
            return redirect("home")

        return render(request, "update_product.html", {"form": form})


class DeleteProductView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect("home")

class AddSupplierView(View):
    def get(self, request):
        return render(request, "add_supplier.html", {"form": SuppliersForm()})

    def post(self, request):
        form = SuppliersForm(request.POST)
        if form.is_valid():
            Suppliers.objects.create(
                supplier_name=form.cleaned_data["supplier_name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                address=form.cleaned_data.get("address", "")
            )
            return redirect("home")
        return render(request, "add_supplier.html", {"form": form})


class UpdateSupplierView(View):
    def get(self, request, pk):
        supplier = get_object_or_404(Suppliers, pk=pk)
        form = SuppliersForm(initial={
            "supplier_name": supplier.supplier_name,
            "email": supplier.email,
            "phone": supplier.phone,
            "address": supplier.address
        })
        return render(request, "update_supplier.html", {"form": form})

    def post(self, request, pk):
        supplier = get_object_or_404(Suppliers, pk=pk)
        form = SuppliersForm(request.POST)
        if form.is_valid():
            supplier.supplier_name = form.cleaned_data["supplier_name"]
            supplier.email = form.cleaned_data["email"]
            supplier.phone = form.cleaned_data["phone"]
            supplier.address = form.cleaned_data.get("address", "")
            supplier.save()
            return redirect("home")
        return render(request, "update_supplier.html", {"form": form})


class DeleteSupplierView(View):
    def get(self, request, pk):
        supplier = get_object_or_404(Suppliers, pk=pk)
        supplier.delete()
        return redirect("home")

class AddOrderView(View):
    def get(self, request):
        return render(request, "add_order.html", {"form": OrdersForm()})

    def post(self, request):
        form = OrdersForm(request.POST)
        if form.is_valid():
            Orders.objects.create(
                customer_name=form.cleaned_data["customer_name"],
                order_date=form.cleaned_data["order_date"],
                status=form.cleaned_data["status"]
            )
            return redirect("home")
        return render(request, "add_order.html", {"form": form})


class UpdateOrderView(View):
    def get(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        form = OrdersForm(initial={
            "customer_name": order.customer_name,
            "order_date": order.order_date,
            "status": order.status
        })
        return render(request, "update_order.html", {"form": form})

    def post(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        form = OrdersForm(request.POST)
        if form.is_valid():
            order.customer_name = form.cleaned_data["customer_name"]
            order.order_date = form.cleaned_data["order_date"]
            order.status = form.cleaned_data["status"]
            order.save()
            return redirect("home")
        return render(request, "update_order.html", {"form": form})


class DeleteOrderView(View):
    def get(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        order.delete()
        return redirect("home")

class AddOrderDetailsView(View):
    def get(self, request):
        return render(request, "add_order_details.html", {"form": Order_detailsForm()})

    def post(self, request):
        form = Order_detailsForm(request.POST)
        if form.is_valid():
            try:
                qty = int(form.cleaned_data["quantity"])
            except ValueError:
                form.add_error("quantity", "Faqat son kiriting!")
                return render(request, "add_order_details.html", {"form": form})

            Order_details.objects.create(
                order=form.cleaned_data["order"],
                product=form.cleaned_data["product"],
                quantity=qty
            )
            return redirect("home")

        return render(request, "add_order_details.html", {"form": form})


class UpdateOrderDetailsView(View):
    def get(self, request, pk):
        order_detail = get_object_or_404(Order_details, pk=pk)
        form = Order_detailsForm(initial={
            "order": order_detail.order,
            "product": order_detail.product,
            "quantity": order_detail.quantity
        })
        return render(request, "update_order_details.html", {"form": form})

    def post(self, request, pk):
        order_detail = get_object_or_404(Order_details, pk=pk)
        form = Order_detailsForm(request.POST)

        if form.is_valid():
            try:
                qty = int(form.cleaned_data["quantity"])
            except ValueError:
                form.add_error("quantity", "Raqam kiriting!")
                return render(request, "update_order_details.html", {"form": form})

            order_detail.order = form.cleaned_data["order"]
            order_detail.product = form.cleaned_data["product"]
            order_detail.quantity = qty
            order_detail.save()
            return redirect("home")

        return render(request, "update_order_details.html", {"form": form})


class DeleteOrderDetailsView(View):
    def get(self, request, pk):
        order_detail = get_object_or_404(Order_details, pk=pk)
        order_detail.delete()
        return redirect("home")

    from django.views import View
    from django.shortcuts import render, redirect
    from .forms import SuppliersForm
    from .models import Suppliers

    class AddSuppliersView(View):
        template_name = 'add_suppliers.html'

        def get(self, request):
            form = SuppliersForm()
            return render(request, self.template_name, {'form': form})

        def post(self, request):
            form = SuppliersForm(request.POST)
            if form.is_valid():
                Suppliers.objects.create(**form.cleaned_data)
                return redirect('suppliers_list')  # agar list page bo‘lsa
            return render(request, self.template_name, {'form': form})


