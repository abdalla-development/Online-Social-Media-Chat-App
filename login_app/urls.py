from django.urls import path
from login_app import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
