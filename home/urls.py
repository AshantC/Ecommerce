from django.urls import path
from home.views import HomeView, CategoryItemView, ItemSearchVeiw

app_name = "home"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("category/<slug>", CategoryItemView.as_view(), name="category"),
    path("search", ItemSearchVeiw.as_view(), name="search")
    
]