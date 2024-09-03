from django.http import HttpResponse
from django.shortcuts import render
from merch.models import Categories


def index(request) -> HttpResponse:

    categories = Categories.objects.all()

    context = {
        "title": "Welcome to Cheglock",
        "name": "Cheglock Sokol Creation",
        "motto": "Сообщество креативных людей",
        "categories": categories,
    }

    return render(request, "main/index.html", context)


def about(request) -> HttpResponse:
    return HttpResponse("About this page")
