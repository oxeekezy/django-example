from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    return HttpResponse("Home Page")


def about(request) -> HttpResponse:
    return HttpResponse("About this page")
