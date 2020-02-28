from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Andrea.")

def about(request):
    return HttpResponse("Hello Marc.")

def userpage(request):
    return HttpResponse("Hello Inesh.")

def userBookmarks(request):
    return HttpResponse("Hello (again) Inesh.")

def explore(request):
    return HttpResponse("Hello Toby.")