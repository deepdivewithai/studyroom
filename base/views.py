from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id': 1 , 'name': 'Lets Learn Python'},
#     {'id': 2 , 'name': 'Design With Me'},
#     {'id': 3 , 'name': 'Front End Developers'},
# ]
rooms = Room.objects.all()

def home(request):
    rooms = Room.objects.all()

    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'base/room.html', context)