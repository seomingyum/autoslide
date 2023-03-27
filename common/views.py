from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import signupForm

def main(request):
    return render(request, 'common/main.html')


def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            auth_login(request, user)  # 로그인
            return redirect('common:main')
    else:
        form = signupForm()
    return render(request, 'common/signup.html', {'form': form})

