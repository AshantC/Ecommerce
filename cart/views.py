from django.shortcuts import render, redirect
from home.models import Item
from cart.models import Cart
from home.views import *

app_name = 'cart'

# Create your views here.

def add_to_cart(request, slug):
    username = request.user.username
    price = Item.objects.get(slug=slug).price
    discounted_price = Item.objects.get(slug=slug).discounted_price
    # quantity = Item.objects.get(slug=slug).quantity

    if discounted_price > 0:
        original_price = discounted_price
    else:
        original_price = price
    if Cart.objects.filter(username = username, slug = slug, checkout = False).exists():
        quantity = Cart.objects.get(username = username, slug=slug, checkout=False).quantity
        quantity = quantity + 1
        total = original_price * quantity
        Cart.objects.filter(username=username, slug=slug, checkout=False).update(quantity=quantity, total=total)
        return render(request, "cart.html")
    else:
        quantity = 1
    total = original_price * quantity

    data = Cart.objects.create(
        username = username,
        items = Item.objects.filter(slug=slug)[0],
        slug = slug,
        quantity = quantity,
        total = total
    )
    data.save()
    return render(request, "cart.html")

class CartView(BaseView):
    def get(self, request):
        username = request.user.username
        self.views['my_cart'] = Cart.objects.filter(username=username, checkout=False)
        return render(request, "cart.html", self.views)
