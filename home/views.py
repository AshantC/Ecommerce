from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from home.models import Category, Ad, Brand, Item, Slider
from cart.models import Cart, Item



# Create your views here.

class BaseView(View):
    views = {}
    views["category"] = Category.objects.filter(status = "active")
    views["new"] = Item.objects.filter(status="active", label="news")
    views["hots"] = Item.objects.filter(status="active", label="hot")

    # def get(self, request):
    #     username = request.user.username
    #     views["total_quantity"] = Item.objects.filter(username=username, checkout=False)


class HomeView(BaseView):
    def get(self, request):
        self.views["slider"] = Slider.objects.filter(status="active")
        self.views["ads"] = Ad.objects.all()
        self.views["brand"] = Brand.objects.filter(status="active")
        
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
            self.views['search_item'] = Item.objects.filter(name__icontains=search)
            return render(request, "search.html", self.views)
        return render(request, "category.html", self.views)
    
class ItemDetailView(BaseView):
    def get(self, request, slug):
        self.views['item_details'] = Item.objects.filter(slug=slug)
        return render(request, "product-detail.html", self.views)
    
    
def signup(request):
    if request.method =="POST":
        f_name = request.POST["first_name"]
        l_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        c_password = request.POST["cpassword"]
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "This username is already taken.")
                return redirect("home:signup")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "This email is already taken.")
                return redirect("home:singup")
            else: 
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password,
                    first_name = f_name,
                    last_name = l_name
                )
                user.save()
                messages.success(request, "You are successfully registered.")
                return redirect("home:signup")
        else:
            messages.error(request, "Password Not Matched.")
            return redirect("home:signup")
    return render(request, "signup.html")


# Default Login
# def login(request):
#     return render(request, "registration/login.html")

# Custom Login and it use normal login.html template
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            messages.error(request, "Wrong username or password")
            return redirect("home:login")

    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return render(request, "index.html")



