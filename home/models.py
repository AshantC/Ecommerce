from django.db import models
from django.urls import reverse

STATUS = (("active", "Active"), ("inactive", "Inactive"))
LABEL = (("new", "New"), ("hot", "Hot"), ("", "Default"))

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS, max_length=100)
    
    class Meta:
        verbose_name_plural = "Category"
        
    def __str__(self):
        return self.name
    
    
class Slider(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media")
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=100)
    
    class Meta:
        verbose_name_plural = "Slider"

    
class Ad(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media")
    description = models.TextField()
    rank = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=100)
    
    class Meta:
        verbose_name_plural = "Ad"
        
class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media")
    status = models.CharField(choices=STATUS, max_length=100)
    
    class Meta:
        verbose_name_plural = "Brand"
        
    def __str__(self):
        return self.name
        
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="media")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    label = models.CharField(choices=LABEL, max_length=100)
    description = models.TextField(blank=True)
    specificatoin = models.TextField(blank=True)
    status = models.CharField(choices=STATUS, max_length=100)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Item"

    def add_to_cart(self):
        return reverse('cart:add-to-cart', kwargs={'slug':self.slug})


# class Cart(models.Model):
#     username = models.CharField(max_length=100)
#     items = models.ForeignKey(Item, on_delete=models.CASCADE)
#     slug = models.CharField(max_length=300)
#     quantity = models.IntegerField(default=1)
#     checkout = models.BooleanField(default=False)
#
#     class Meta:
#         verbose_name_plural = "Cart"

