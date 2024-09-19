from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from video.models import Video


def video(request):
    videos=Video.objects.all()
    context={'videos':videos}
    return  render(request,'video/video.html', context)

def watch_video(request, pk):
    video=Video.objects.get(pk=pk)
    context={'video':video}
    return render(request, 'video/watch_video.html', context)

