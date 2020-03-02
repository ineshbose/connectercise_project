from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'message': 'Index'}
    return render(request, 'main/index.html', context=context_dict)

def about(request):
    context_dict = {'message': 'About'}
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