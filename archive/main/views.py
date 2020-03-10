from django.shortcuts import render
from django.http import HttpResponse
from main.models import UserProfile, SportingRequest

def index(request):
    request_list = SportingRequest.objects.all()
    context_dict = {'message': 'Index', 'requests':request_list}
    return render(request, 'main/index.html', context=context_dict)

def about(request):
    request_list = SportingRequest.objects.all()
    context_dict = {'message': 'About', 'requests':request_list}
    return render(request, 'main/about.html', context=context_dict)

def userpage(request):
    context_dict = {'message': 'User Page'}
    return render(request, 'main/user.html', context=context_dict)

def userBookmarks(request):
    context_dict = {'message': 'Bookmarks'}
    return render(request, 'main/bookmarks.html', context=context_dict)

def explore(request):
    context_dict = {'message': 'Explore'}
    return render(request, 'main/explore.html', context=context_dict)