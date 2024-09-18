from django.shortcuts import render

from videocourses.models import Video


def index(request):
    video_list = Video.objects.all()
    context = {"video_list": video_list}

    return render(request, "videocourses/index.html", context)


def video(request, slug):
    video = Video.objects.get(slug=slug)
    context = {"video": video}

    return render(request, "videocourses/video.html", context)
