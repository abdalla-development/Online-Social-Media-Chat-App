from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('profile/', include('profile_app.urls')),
    path('register/', include('register_app.urls')),
    path('login/', include('login_app.urls')),
    path('Mail-Box/', include('inbox_app.urls')),
    path('chat/', include('chat_app.urls')),
    path('Users/', include('my_users_app.urls')),
]
