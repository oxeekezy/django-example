from django.shortcuts import render
from merch.models import Products


def catalog(request, slug):
    if slug == "all":
        merch = Products.objects.all()
    else:
        merch = Products.objects.filter(category__slug=slug)

    context = {
        "title": "Чеглок Мерч",
        "name": "Cheglock Sokol Creation",
        "merch": merch,
    }

    return render(request, "merch/catalog.html", context)


def product(request, slug):
    product = Products.objects.get(slug=slug)

    if product.large_description is None:
        product.large_description = product.description

    context = {"product": product}

    return render(request, "merch/product.html", context)
