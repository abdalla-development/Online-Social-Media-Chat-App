from django.urls import path
from register_app import views

urlpatterns = [
    path('', views.register, name='register'),
    path('user-info', views.user_info, name='user_info'),
]
