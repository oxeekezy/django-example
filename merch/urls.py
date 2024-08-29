from django.urls import path
from merch import views

app_name = "merch"

urlpatterns = [
    path("", views.catalog, name="catalog"),
    path("product/", views.product, name="product"),
]
