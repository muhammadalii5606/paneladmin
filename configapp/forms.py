from traceback import format_exc

from django import forms
from configapp.models import Category, Suppliers, Order_details, Product
from django.core.exceptions import  ValidationError



class CategoryForm(forms.Form):
    category_name = forms.CharField(max_length=100,label='Category',
                                    widget=forms.TextInput(attrs={"class":"form-control"}))

    description = forms.CharField(label='text_description',required=False,
                                  widget=forms.Textarea(attrs={"class":"form-control","rows":5}))


    # category = forms.ModelChoiceField(empty_label='Category',label="Category",queryset=Category.objects.all(),
    #                                   widget=forms.Select(attrs={"class":"form-control"}))


class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=100, label='Product_name', widget=forms.TextInput(attrs={"class":"form-control"}))
    unit_price = forms.DecimalField(label='Product_price', widget=forms.NumberInput(attrs={"class":"form-control"}))
    category = forms.ModelChoiceField(empty_label='Category', label='Category',queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={"class":"form-control"}))
    suppliers = forms.ModelChoiceField(empty_label='Suppliers', label='Suppliers',queryset=Suppliers.objects.all(),
                                       widget=forms.Select(attrs={"class":"form-control"}))
    photo = forms.ImageField()


class SuppliersForm(forms.Form):
    company_name = forms.CharField(max_length=100, label='company_name', widget=forms.TextInput(attrs={"class":"form-control"}))
    contact_name = forms.CharField(max_length=100, label='contact_name', widget=forms.TextInput(attrs={"class":"form-control"}))
    contact_title = forms.CharField(max_length=100, label='contact_title', widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(max_length=250, label='address', widget=forms.Textarea(attrs={"class":"form-control"}))
    city = forms.CharField(max_length=180, label='city', widget=forms.TextInput(attrs={"class":"form-control"}))
    region = forms.CharField(max_length=100, label='region', widget=forms.TextInput(attrs={"class":"form-control"}))
    country = forms.CharField(max_length=100, label='country',widget=forms.TextInput(attrs={"class":"form-control"}))
    phone = forms.CharField(max_length=14, label='phone', widget=forms.TextInput(attrs={"class":"form-control"}))


class Order_detailsForm(forms.Form):
    product = forms.ModelChoiceField(empty_label='Product', label='Product', queryset=Product.objects.all(),
                                     widget=forms.Select(attrs={"class":"form-control"}))

    unit_price = forms.DecimalField(label='unit_price', widget=forms.NumberInput(attrs={"class":"form-control"}))
    quantity  = forms.CharField(label='quantity', widget=forms.TextInput(attrs={"class":"control"}))

class OrdersForm(forms.Form):
    order_date = forms.DateTimeField(label='Order_date',widget=forms.DateTimeInput(attrs={"class":"form-control"}))
    required_date = forms.DateTimeField(label='Required_date', widget=forms.DateTimeInput(attrs={"class":"form-control"}))

    order_dtls = forms.ModelChoiceField(empty_label='order_dtls', label='order_dtls', queryset=Order_details.objects.all(),
                                        widget=forms.Select(attrs={"class":"form-control"}))