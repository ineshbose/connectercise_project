from django.shortcuts import render
from django.http import HttpResponse
from connectercise.models import Sport, SportRequest

# Create your views here.
def index(request):
    sport_list = Sport.objects.order_by('-likes')[:5]
    request_list = SportRequest.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'lorem ipsum?'
    context_dict['sports'] = sport_list
    context_dict['requests'] = request_list
    return render(request, 'connectercise/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Team Connectercise!'}
    return render(request, 'connectercise/about.html', context=context_dict)

def show_sport(request, sport_name_slug):
    context_dict = {}
    try:
        sport = Sport.objects.get(slug=sport_name_slug)
        requests = SportRequest.objects.filter(sport=sport)
        context_dict['requests'] = requests
        context_dict['sport'] = sport
    except Sport.DoesNotExist:
        context_dict['sport'] = None
        context_dict['requests'] = None
    return render(request, 'connectercise/sport.html', context=context_dict)