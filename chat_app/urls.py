from django.urls import path
from chat_app import views

urlpatterns = [
    path('private-texted', views.private_texted_chat, name='private_texted_chat'),
    path('group-texted', views.group_texted_chat, name='group_texted_chat'),
]
# path('private/video', views.private_video_chat, name='private_video_chat'),
# path('group/video', views.group_video_chat, name='group_video_chat'),