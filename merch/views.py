from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Чеглок Мерч",
        "name": "Cheglock Sokol Creation",
    }

    return render(request, "merch/catalog.html", context)


def product(request):
    return render(request, "merch/product.html")
