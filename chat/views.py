from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from chat.models import Room, Message
from django.contrib.auth.models import User
from chat.forms import MessageForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def all_chats(request):
    context_dict = {}
    try:
        room_data = []
        for room in Room.objects.all():
            if request.user in room['participants']:
                room_data.append(room)
        context_dict['room'] = room_data
    except Room.DoesNotExist:
        context_dict['room'] = None
    return render(request, 'chat/all_chats.html', context=context_dict)

@login_required
def room(request, user_profile_slug):
    context_dict = {}
    try:
        participant_user = User.objects.get(username=user_profile_slug)
        room = None
        for r in Room.objects.all():
            if participant_user in r['participants']:
                room = r
    except User.DoesNotExist:
        return redirect('/')
    except Room.DoesNotExist:
        return redirect('/')
        
'''    
@login_required
def add_sport_request(request, sport_name_slug):
    try:
        sport = Sport.objects.get(slug=sport_name_slug)
    except Sport.DoesNotExist:
        sport = None
    
    if sport is None:
        return redirect('/')
    
    form = SportRequestForm()

    if request.method == 'POST':
        form = SportRequestForm(request.POST)
        if form.is_valid():
            if sport:
                s_request = form.save(commit=False)
                s_request.sport = sport
                s_request.views = 0
                s_request.creator = request.user
                s_request.completed = False
                s_request.save()
                return redirect(reverse('connectercise:show_request', kwargs={'sport_name_slug': sport_name_slug, 'request_name_slug': s_request.request_id}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'sport': sport}
    return render(request, 'connectercise/add_request.html', context=context_dict)
'''