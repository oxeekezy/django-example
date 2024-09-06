from django.urls import path
from merch import views

app_name = "merch"

urlpatterns = [
    path("<slug:slug>/", views.catalog, name="catalog"),
    path("product/<slug:slug>/", views.product, name="product"),
]
