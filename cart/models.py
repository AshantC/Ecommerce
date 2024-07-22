from django.db import models
from home.models import Item

# Create your models here.

class Cart(models.Model):
    username = models.CharField(max_length=100)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    slug = models.CharField(max_length=300)
    quantity = models.IntegerField(default=1)
    checkout = models.BooleanField(default=False)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Cart"