from django.shortcuts import render


def login(request):

    context = {"title": "Вход"}

    return render(request, "users/login.html", context)


def register(request):
    context = {}

    return render(request, "users/login.html", context)


def logout(request):
    context = {}

    return render(request, "users/login.html", context)


def profile(request):
    context = {}

    return render(request, "users/login.html", context)
