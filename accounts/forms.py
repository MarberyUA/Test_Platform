from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts import models


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = UserCreationForm.Meta.fields + ('email',)


class UserDetailUpdateForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_photo', 'birthday', 'personal_description']
