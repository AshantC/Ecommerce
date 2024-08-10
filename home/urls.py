from django.urls import path
from home.views import HomeView, CategoryItemView, ItemSearchVeiw, ItemDetailView, signup, login, logout

app_name = "home"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("category/<slug>", CategoryItemView.as_view(), name="category"),
    path("item_detail/<slug>", ItemDetailView.as_view(), name="item_detail"),
    path("search", ItemSearchVeiw.as_view(), name="search"),
    path("signup", signup, name="signup"),
    path("login", login, name="login"),
    path("logout", logout, name="logout")

]