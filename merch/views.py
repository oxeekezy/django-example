from django.shortcuts import render
from merch.models import Products

BASE_CONTEXT = {"title": "Чеглок Мерч", "name": "Cheglock Sokol Creation"}


def catalog(request, slug):
    discount = request.GET.get("discount", False)
    order_by = request.GET.get("order_by", None)

    merch = Products.objects.filter(category__slug=slug)

    if discount:
        merch = merch.filter(discount__gt=0)

    if order_by:
        merch = merch.order_by(order_by)

    context = BASE_CONTEXT | {"merch": merch}

    return render(request, "merch/catalog.html", context)


def get_all_catalog(request):
    merch = Products.objects.all()

    context = BASE_CONTEXT | {"merch": merch}

    return render(request, "merch/catalog.html", context)


def product(request, slug):
    product = Products.objects.get(slug=slug)

    if product.large_description is None:
        product.large_description = product.description

    context = BASE_CONTEXT | {"product": product}

    return render(request, "merch/product.html", context)
