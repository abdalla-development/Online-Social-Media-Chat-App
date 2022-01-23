from django.urls import path
from profile_app import views

urlpatterns = [
    path('<username>', views.profile, name='profile'),
    path('edit-user-profile/<username>', views.edit_user_profile, name='edit_user_profile'),
]
