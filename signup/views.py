from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import User

# def index(request):
#     return render(request, 'login.html')

from django.views.generic.base import View


# class CustomBackend(ModelBackend):
#     def authenticate(self, username=None, password=None, **kwargs):
#         print("<<< start authenticate >>>")
#         try:
#             user = User.objects.get(Q(username=username) | Q(email=username))
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None
#
#     def user_login(self, request):
#         print("get in user login")
#         if request.method == 'POST':
#             print("get user name and password")
#             user_name = request.POST.get('username', "")
#             pass_word = request.POST.get('password', "")
#             print(user_name)
#             print(pass_word)
#             user = authenticate(username=user_name, password=pass_word)
#             if user is not None:
#                 login(request, user)
#                 return render(request, "tools.html")
#             else:
#                 return render(request, 'login.html', {"msg": "用户名或密码错误!"})
#         elif request.method == 'GET':
#             return render(request, 'login.html', {})


def simple_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', "")
        pass_word = request.POST.get('password', "")
        usr = User.objects.get(username=user_name)
        if usr.password == pass_word:
            request.session['is_login'] = True
            request.session['user_id'] = usr.userid
            request.session['user_name'] = usr.username
            return render(request, 'tools.html')
        else:
            return render(request, 'login.html', {"msg": "Invalid user or password!"})
    return render(request, 'login.html')


def signup(request):
    return render(request, 'register.html')
