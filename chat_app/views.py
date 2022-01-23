from django.shortcuts import render
from django.http import HttpResponse
from inbox_app.models import Messages

# Create your views here.

# private_chat
def private_texted_chat(request):
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
    return render(request, 'private_chat.html', context)

def private_video_chat(request):
    my_inbox = Messages.objects.filter(send_to= request.user)
    my_sent = Messages.objects.filter(send_from= request.user)
    inbox_count = len(my_inbox)
    sent_count = len(my_sent)
    total_messages = inbox_count + sent_count
    context = {
        "inbox_count": inbox_count, 
        "sent_count": sent_count, 
        "total_messages": total_messages,
    }
    return render(request, 'private_chat.html', context)

def group_texted_chat(request):
    my_inbox = Messages.objects.filter(send_to= request.user)
    my_sent = Messages.objects.filter(send_from= request.user)
    inbox_count = len(my_inbox)
    sent_count = len(my_sent)
    total_messages = inbox_count + sent_count
    context = {
        "inbox_count": inbox_count, "sent_count": sent_count, "total_messages": total_messages,
    }
    return render(request, 'group_chat.html', context)


def group_video_chat(request):
    my_inbox = Messages.objects.filter(send_to= request.user)
    my_sent = Messages.objects.filter(send_from= request.user)
    inbox_count = len(my_inbox)
    sent_count = len(my_sent)
    total_messages = inbox_count + sent_count
    context = {
        "inbox_count": inbox_count, 
        "sent_count": sent_count, 
        "total_messages": total_messages,
    }
    return render(request, 'group_chat.html', context) 