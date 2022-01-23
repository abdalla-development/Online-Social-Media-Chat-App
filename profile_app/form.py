from django import forms
from django.db.models.base import Model
from django.forms import fields
from register_app.models import UserInfo


class UpdateInfoForm(forms.ModelForm):
    class Meta:
        Model = UserInfo
        fields = ["about_me", "image", "address", "phone_number", "postal_code", "city", "country"]

