from django.urls import path
from videocourses import views

app_name = "videocourses"

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>/", views.video, name="video"),
]
