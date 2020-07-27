from django.shortcuts import render, get_object_or_404, redirect

from .forms import CreationForm
from .forms import CreationForm_Room
from .models import Meeting
from .models import Room

# Create your views here.


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'Blog/room/room_list.html', {
        'rooms': rooms
    })

def post_list(request):
    return render(request, "post_list.html", {"posts": Meeting.objects.all()})


def post_details(request, post_title):
    post = get_object_or_404(Meeting, title=post_title)
    return render(request, "post_details.html", {"post": post})


def post_creation(request):
    if request.method == "POST":
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"/post_details/{form.cleaned_data['title']}")

    else:
        form = CreationForm()
    return render(request, "creation.html", {"form": form})

def room_creation(request):
    if request.method == "POST":
        form = CreationForm_Room(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"/post_details/{form.cleaned_data['title']}")

    else:
        form = CreationForm_Room()
    return render(request, "room/room_list.html", {"form": form})