from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context = {
        "title": "Main page test",
        "content": "Main page content. Check this",
        "list": ["one", "two", "one-two"],
        "show": True,
    }

    return render(request, "main.index.html", context)


def about(request) -> HttpResponse:
    return HttpResponse("About this page")
