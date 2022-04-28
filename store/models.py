from django.db import models
from django.contrib.auth.models import User
import pymysql

# Create your models here.
class Contact(models.Model):
    name =  models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)  
    message = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name

    class Meta:
       verbose_name_plural = "6. Contact" 

 

class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=122, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name  
    class Meta:
       verbose_name_plural = "2. Category"  

class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    code = models.CharField(max_length=122, null=True, blank=True)
    short_description = models.TextField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    details = models.TextField(max_length=500, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
       verbose_name_plural = "1. Product" 

class OrderItem(models.Model):

    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "7. OrderItem" 


class Setting(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    location_details = models.CharField(max_length=200, null=True, blank=True)
    fb = models.URLField(max_length=200, null=True, blank=True)
    insta = models.URLField(max_length=200, null=True, blank=True)
    yt = models.URLField(max_length=200, null=True, blank=True)
    tw = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
       verbose_name_plural = "5. Setting" 

class BannerImage(models.Model):
    image = models.ImageField(null=True, blank=True)

    class Meta:
       verbose_name_plural = "3. Banner Image" 

class Brochure(models.Model):
    image = models.FileField(null=True, blank=True)

    class Meta:
       verbose_name_plural = "4. Brochure" 


