from django.db import models
import datetime

# Create your models here.
#categories of foodstuffs
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    #kuhepa django plural automation of category
    class Meta:
        verbose_name_plural = 'Categories'

class Customer(models.Model):
    first_name_as_per_MPESA = models.CharField(max_length=50)
    last_name_as_per_MPESA = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name_as_per_MPESA} {self.last_name_as_per_MPESA}'

#customer product
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="1")
    description = models.CharField(max_length=200,default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')
    def __str__(self):
        return self.name



#customer order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    location_address=models.CharField(max_length=100, default='', blank=True, null=True)
    phone = models.CharField(max_length=10, default='', blank=True, null=True)
    date_ordered = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.product.name} {self.quantity} {self.date_ordered}'



