
from django.urls import path
from cart.views import add_to_cart, CartView

app_name = 'cart'

urlpatterns = [
    path("add-to-cart/<slug>", add_to_cart, name="add-to-cart"),
    path("", CartView.as_view(), name="cart"),
]