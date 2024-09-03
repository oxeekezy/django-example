from django.shortcuts import render
from merch.models import Products


def catalog(request):
    merch = Products.objects.all()

    context = {
        "title": "Чеглок Мерч",
        "name": "Cheglock Sokol Creation",
        "merch": merch,
    }

    return render(request, "merch/catalog.html", context)


def product(request):
    return render(request, "merch/product.html")
