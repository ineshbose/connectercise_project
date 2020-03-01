from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'message': 'Hello Andrea.'}
    return render(request, 'main/index.html', context=context_dict)

def about(request):
    context_dict = {'message': 'Hello Marc.'}
    return render(request, 'main/about.html', context=context_dict)

def userpage(request):
    context_dict = {'message': 'Hello Inesh.'}
    return render(request, 'main/user.html', context=context_dict)

def userBookmarks(request):
    context_dict = {'message': 'Hello (again) Inesh.'}
    return render(request, 'main/bookmarks.html', context=context_dict)

def explore(request):
    context_dict = {'message': 'Hello Toby.'}
    return render(request, 'main/index.html', context=context_dict)