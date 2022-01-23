from django.shortcuts import render, redirect
from register_app.form import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from register_app.models import UserInfo
from datetime import datetime

# Create your views here.
user_name = ""


def register(request):
    global user_name
    if request.method == "GET":
        return render(request, 'register.html', {})
    else:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'New User added.') 
            user_name = request.POST['username']
            return redirect('user_info')  
        else:
            for msg in form.error_messages:
                messages.error(request, 'User Not added.') 
            return redirect('register')


def user_info(request):
    if request.method == "GET":
        return render(request, 'user_info.html', {})
    else:
        # Request form Data
        birth_day = request.POST["birthday"]
        gender = request.POST["gender"]
        phone_number = request.POST["phone_number"]
        address = request.POST["address"]
        city = request.POST["city"]
        country = request.POST["country"]
        postal_code = request.POST["postal_code"]
        about_me = request.POST["about_me"]
        user_id = request.user
        profile_picture = request.FILES["image"]

        # Calculate the Ag3
        date = int(datetime.now().year)
        birth = int(birth_day.split("/")[2])
        age = date - birth

        # check the username
        if request.user.is_authenticated:
            user_id = request.user

        new_user = UserInfo.objects.create(birth_day=birth_day, gender=gender, phone_number=phone_number, address=address, city=city, country=country, 
        postal_code=postal_code, about_me=about_me, profile_picture=profile_picture, age=age, friends=0, user_id=user_name)
        if new_user:
            return redirect('profile')
        else:
            return render(request, 'user_info.html', {})