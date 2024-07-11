from django.shortcuts import render
from django.views import View
from home.models import Category, Ad, Brand, Item, Slider


# Create your views here.

class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get(self, request):
        self.views["category"] = Category.objects.filter(status = "active")
        self.views["slider"] = Slider.objects.filter(status="active")
        self.views["ads"] = Ad.objects.all()
        self.views["brand"] = Brand.objects.filter(status="active")
        self.views["hots"] = Item.objects.filter(status="active", label="hot")
        self.views["new"] = Item.objects.filter(status="active", label="news ")
        
        return render(request, "index.html", self.views)