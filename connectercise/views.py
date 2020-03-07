from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'Wazzup?'}
    return render(request, 'connectercise/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Team Connectercise!'}
    return render(request, 'connectercise/about.html', context=context_dict)