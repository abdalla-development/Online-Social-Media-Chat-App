from django.shortcuts import render, redirect
from inbox_app.models import Messages

# Create your views here.   message = Messages.objects.get()


def mailbox(request):
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
        return render(request, 'mailbox.html', context)


def inbox(request):
    my_inbox = Messages.objects.filter(send_to= request.user)
    my_sent = Messages.objects.filter(send_from= request.user)
    inbox_count = len(my_inbox)
    sent_count = len(my_sent)
    total_messages = inbox_count + sent_count
    inbox_message = Messages.objects.filter(send_to= request.user) 
    context = {
        "inbox_message": inbox_message, 
        "inbox_count": inbox_count, 
        "sent_count": sent_count, 
        "total_messages": total_messages,
    }
    if request.method == "GET":
        
        return render(request, 'inbox.html', context)


def sent(request):
    my_inbox = Messages.objects.filter(send_to= request.user)
    my_sent = Messages.objects.filter(send_from= request.user)
    inbox_count = len(my_inbox)
    sent_count = len(my_sent)
    total_messages = inbox_count + sent_count
    sent_message = Messages.objects.filter(send_from= request.user)
    context = {
        "sent_message": sent_message, 
        "inbox_count": inbox_count, 
        "sent_count": sent_count, 
        "total_messages": total_messages,
    }
    if request.method == "GET":
        
        return render(request, 'sent.html', context)

        

def new_message(request, to_user):
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
        return render(request, 'new_message.html', context)
    else:
        sent_to = to_user
        sent_from = request.user
        subject = request.POST['subject']
        message = request.POST['message']
        Messages.objects.create(send_to=sent_to, send_from= sent_from, subject= subject, message= message)
        return redirect('mailbox')



def read_email(request, mail):
    my_inbox = Messages.objects.filter(send_to= request.user)
    my_sent = Messages.objects.filter(send_from= request.user)
    inbox_count = len(my_inbox)
    sent_count = len(my_sent)
    total_messages = inbox_count + sent_count
    read_message = Messages.objects.get(pk=mail)
    context = {
        "read_message": read_message, 
        "inbox_count": inbox_count, 
        "sent_count": sent_count, 
        "total_messages": total_messages,
    }
    if request.method == "GET":
        return render(request, 'read_email.html', context)



def show_email(request, mail):
    my_inbox = Messages.objects.filter(send_to= request.user)
    my_sent = Messages.objects.filter(send_from= request.user)
    inbox_count = len(my_inbox)
    sent_count = len(my_sent)
    total_messages = inbox_count + sent_count
    show_message = Messages.objects.get(pk=mail)
    context ={
        "show_message": show_message, 
        "inbox_count": inbox_count, 
        "sent_count": sent_count, 
        "total_messages": total_messages,
    }
    if request.method == "GET":
        return render(request, 'show_email.html', context)



def delete_email(request, mail):
    if request.method == "GET":
        message = Messages.objects.get(pk=mail)
        message.delete()
        return redirect('mailbox') 