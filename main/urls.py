from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/', views.userpage, name='user'),
    path('bookmarks/', views.userBookmarks, name='bookmarks'),
    path('explore/', views.explore, name='explore'),
]