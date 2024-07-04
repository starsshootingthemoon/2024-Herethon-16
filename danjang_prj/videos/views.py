from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from portfolios.models import *
from django.db.models import Q

def video_list(request):
    videos = Video.objects.all()
    
    return render(request, "videos/video_list.html", {'videos' : videos})

def video_detail(request, id):
    video = get_object_or_404(Video, id = id)

    views = Video.objects.get(pk=id)
    views.increase_views()

    return render(request, "videos/video_detail.html",{'video' : video, 'views' : views})

def like(request, id):
    video = get_object_or_404(Video, id = id)
    if video.like.filter(id = request.user.id).exists():
        video.like.remove(request.user)
    else:
        video.like.add(request.user)
    return redirect('videos:video_detail', id)

# def search(request):
#     entered_text = request.GET['data']
#     videos = Video.objects.filter(Q(title__contains = entered_text) | Q(content__contains = entered_text))

#     return render(request, "videos/search.html", {'videos': videos, 'entered_text': entered_text})