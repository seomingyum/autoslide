from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import User
from django import forms

class signupForm(UserCreationForm):
    class Meta: #메타 안에 있는 모델과 필드들을 커스텀 유저에 맞게 수정 작업하는 것
        model=User
        fields= ['username', 'password1', 'password2', 'nickname', 'phone', 'email']


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'nickname']