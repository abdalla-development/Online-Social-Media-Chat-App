from django.shortcuts import render, redirect
from register_app.models import UserInfo
from django.contrib.auth.decorators import login_required
from inbox_app.models import Messages

# Create your views here.

# @login_required
def profile(request, username):
    my_inbox = Messages.objects.filter(send_to= request.user)
    my_sent = Messages.objects.filter(send_from= request.user)
    inbox_count = len(my_inbox)
    sent_count = len(my_sent)
    total_messages = inbox_count + sent_count
    user_data = UserInfo.objects.get(user_id= username)
    context = {
        "user_data": user_data, 
        "inbox_count": inbox_count, 
        "sent_count": sent_count, 
        "total_messages": total_messages,
    }
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'profile.html', context) 

        else:
            return redirect ("login")
    
        


def edit_user_profile(request, username):
    my_inbox = Messages.objects.filter(send_to= request.user)
    my_sent = Messages.objects.filter(send_from= request.user)
    inbox_count = len(my_inbox)
    sent_count = len(my_sent)
    total_messages = inbox_count + sent_count
    user_data = UserInfo.objects.get(user_id= username)
    context = {
        "user_data": user_data, 
        "inbox_count": inbox_count, 
        "sent_count": sent_count, 
        "total_messages": total_messages,
    }
    if request.method == "GET":
        return render(request, 'edit_user_profile.html', context)

    else:
        user_data = UserInfo.objects.get(user_id= username)
        user_data.about_me = request.POST["about_me"]
        user_data.address = request.POST["address"]
        user_data.phone_number = request.POST["phone_number"]
        user_data.postal_code = request.POST["postal_code"]
        user_data.country = request.POST["country"]
        user_data.city = request.POST["city"]
        if len(user_data.about_me) != 0:
            user_data.about_me = request.POST["about_me"]
        user_data.save()
        return redirect("profile")