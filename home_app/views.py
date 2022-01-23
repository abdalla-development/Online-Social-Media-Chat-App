from django.shortcuts import render
from django.http import HttpResponse
from inbox_app.models import Messages

# Create your views here.


def home(request):
    my_inbox = Messages.objects.filter(send_to= request.user)
    my_sent = Messages.objects.filter(send_from= request.user)
    inbox_count = len(my_inbox)
    sent_count = len(my_sent)
    total_messages = inbox_count + sent_count
    context ={
        "inbox_count": inbox_count, 
        "sent_count": sent_count, 
        "total_messages": total_messages,
    }
    if request.method == "GET":
        return render(request, 'index.html', context) 