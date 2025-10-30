from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    product_name = models.CharField(max_length=100)
    suppliers  = models.ForeignKey('Suppliers', on_delete=models.CASCADE,default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.product_name


class Suppliers(models.Model):
    company_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)



    def __str__(self):
        return self.company_name


class Order_details(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.CharField(max_length=100)
    def __str__(self):
        return self.quantity


class Orders(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    required_date = models.DateTimeField()
    order_dtls = models.ForeignKey(Order_details,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"Order #{self.id}"

