from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import signupForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import User
from django.contrib import messages

def main(request):
    return render(request, 'common/main.html')

def main_pop(request):
    return render(request, 'common/main_pop.html')

def board(request):
    return render(request, 'pybo/pybo.html')

def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            auth_login(request, user)  # 로그인
            if user:    # authenticate함수가 사용자 인증 처리를 성공하면 user는 True값 반환
                return redirect('common:main_pop')    # main_pop 함수에서 랜더링하는 페이지가 팝업창 호출하는 기능 가지고 있음!
        else:
            return redirect('common:signup')
    else:
        form = signupForm()
    return render(request, 'common/signup.html', {'form': form})



def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('common:main')
        else:
            return redirect('common:profile')
    else:
        form = UserProfileForm(instance=request.user)
        return render(request, 'common/profile.html', {'form': form})


def profile_pw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('common:main')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'common/profile_pw.html', {'form': form})









