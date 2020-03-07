from django.urls import path
from connect import views
from django.contrib.auth import views as auth_views

app_name = 'connect'

urlpatterns = [
    #path('signup/', views.signup, name='signup'),
    #path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    #path('logout/', auth_views.logout, {'template_name': 'home.html'} ,name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/', views.selfProfile, name='profile'),
    path('rate/', views.rate, name='rate'),
    path('rate/<ratedUserID>/', views.rate, name='rate'),
    path('matches/', views.matches, name='matches'),
    path('mailbox/', views.mailbox, name='mailbox'),
    #path('message/<username>/', views.message, name='message'),
    path('menu/', views.menu, name='menu'),
    path('', views.index, name='index'),
]