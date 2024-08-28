from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context = {
        "title": "Welcome to Cheglock",
        "name": "Cheglock Sokol Creation",
        "motto": "Сообщество креативных людей",
    }

    return render(request, "main/index.html", context)


def about(request) -> HttpResponse:
    return HttpResponse("About this page")
