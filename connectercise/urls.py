from django.urls import path
from connectercise import views

app_name = 'connectercise'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('activity/', views.activity, name='activity'),
    path('sports/', views.sports, name='sports'),
    path('sport/<slug:sport_name_slug>/', views.show_sport, name='show_sport'),
    path('sport/<slug:sport_name_slug>/<slug:request_name_slug>', views.show_request, name='show_request'),
    path('add_sport/', views.add_sport, name='add_sport'),
    path('sport/<slug:sport_name_slug>/add_request/', views.add_request, name='add_request'),
    path('user/<slug:user_profile_slug>/', views.show_user, name='show_user'),
    path('restricted/', views.restricted, name='restricted'),
    path('sport/<slug:sport_name_slug>/<slug:request_name_slug>/accept_request', views.accept_request, name='accept_request'),
]