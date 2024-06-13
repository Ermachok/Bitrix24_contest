from django.urls import path
from app_ticket.views import create_video_with_caption

urlpatterns = [
    path('create_video/', create_video_with_caption, name='create_video'),
]
