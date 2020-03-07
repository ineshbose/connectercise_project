from django.urls import path
from connectercise import views

app_name = 'connectercise'

urlpatterns = [
    path('', views.index, name='index'),
]