from django.urls import path
from connectercise import views

app_name = 'connectercise'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('sport/<slug:sport_name_slug>/', views.show_sport, name='show_sport'),
]