from django.urls import path
from connectercise import views

app_name = 'connectercise'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('explore/', views.explore, name='explore'),
    path('sports/', views.sports, name='sports'),
    path('sport/<slug:sport_name_slug>/', views.show_sport, name='show_sport'),
    path('sport/<slug:sport_name_slug>/<slug:request_name_slug>', views.show_request, name='show_request'),
    path('sport/<slug:sport_name_slug>/<slug:request_name_slug>/accept', views.accept_request, name='accept_request'),
    path('sport/<slug:sport_name_slug>/<slug:request_name_slug>/delete', views.delete_request, name='delete_request'),
    path('add_sport/', views.add_sport, name='add_sport'),
    path('sport/<slug:sport_name_slug>/add_request/', views.add_sport_request, name='add_sport_request'),
    path('user/<slug:user_profile_slug>/', views.show_user, name='show_user'),
    path('user/<slug:user_profile_slug>/settings/', views.user_settings, name='user_settings'),
    path('add_request/', views.add_request, name='add_request'),
    path('search/', views.search, name='search'),
    path('sport/<slug:sport_name_slug>/<slug:request_name_slug>/accept_request', views.accept_request, name='accept_request'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
]