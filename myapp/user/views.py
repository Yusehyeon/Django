from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .models import  User
from .forms import RegisterForm, LoginForm

# Create your views here.
# user 관련 기능
# 회원가입
# log-in
# log0out

### Registration
class Registration(View):
    def get(self, request):
        # 회원가입 페이지
        # write userinformation for form
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'user/user_register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 로그인한 다음 이동
        return redirect('blog:list')


class Login(View):
    def get(self, request):
        form = LoginForm(request.POST)
        context = {
            'form': form
        }
        return render(request, 'user/user_login.html', context)
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)

            if user:
                login(request, user)
                return redirect('blog:list')
            
            form.add_error(None, 'was not find a ID')
    
        context = {
        'form': form
        }

        return render(request, 'user.user_login.html', context)


### LogOut
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:list')