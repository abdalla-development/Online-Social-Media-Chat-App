from django.urls import path
from inbox_app import views

urlpatterns = [
    path('', views.mailbox, name='mailbox'),
    path('Inbox', views.inbox, name='inbox'),
    path('Sent', views.sent, name='sent'),
    path('new-message/<to_user>', views.new_message, name='new_message'),
    path('Inbox/read-email/<mail>', views.read_email, name='read_email'),
    path('Sent/show-email/<mail>', views.show_email, name='show_email'),
    path('delete-email/<mail>', views.delete_email, name='delete_email'),
]
