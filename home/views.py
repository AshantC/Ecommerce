from django.shortcuts import redirect, render
from django.views import View
from home.models import Category, Ad, Brand, Item, Slider


# Create your views here.

class BaseView(View):
    views = {}
    views["category"] = Category.objects.filter(status = "active")
    views["new"] = Item.objects.filter(status="active", label="news ")
    views["hots"] = Item.objects.filter(status="active", label="hot")

class HomeView(BaseView):
    def get(self, request):
        self.views["slider"] = Slider.objects.filter(status="active")
        self.views["ads"] = Ad.objects.all()
        self.views["brand"] = Brand.objects.filter(status="active")
        self.views["new"] = Item.objects.filter(status="active", label="news ")
        
        return render(request, "index.html", self.views)
    
class CategoryItemView(BaseView):
    def get(self, request, slug):
        category_id = Category.objects.get(slug=slug).id
        self.views["cat_items"] = Item.objects.filter(category = category_id)
        
        return render(request, "category.html", self.views)
    

class ItemSearchVeiw(BaseView):
    def get(self, request):
        search = request.GET.get('search', None)
        if search is None:
            return redirect("/")
        else:
            return render(request, "category.html", self.views)
        return render(request, "category.html", self.views)