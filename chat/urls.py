from django.urls import path
from chat import views

app_name = 'chat'

urlpatterns = [
    path('', views.all_chats, name='all_chats'),
]