from django.contrib import admin
from home.models import Category, Ad, Brand, Item, Slider

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', )
    list_filter = ("name", "status")
    
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand','label', 'status',  'price', 'discounted_price',)
    
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')