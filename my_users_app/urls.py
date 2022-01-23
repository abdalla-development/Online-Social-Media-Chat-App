from django.urls import path
from my_users_app import views


urlpatterns = [
    path('', views.users, name='users'),
]