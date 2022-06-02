from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ('phone', 'address')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('phone', 'address')


class UpdateUserDataForm(forms.ModelForm):
    phone = forms.CharField(max_length=255, required=True,)
    address = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['phone', 'address']
