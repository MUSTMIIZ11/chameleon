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
#                 return render(request, "tool.html")
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
            request.session['user_id'] = usr.id
            request.session['user_name'] = usr.username
            return render(request, 'tool.html')
        else:
            return render(request, 'login.html', {"msg": "Invalid user or password!"})
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', "")
        pass_word1 = request.POST.get('password1', "")
        pass_word2 = request.POST.get('password2', "")
        try:
            usr = User.objects.get(username=user_name)
        except Exception as e:
            usr = None

        if usr is not None:
            return render(request, 'register.html', {"msg": "The user name already exist!"})
        else:
            if pass_word1 == pass_word2:
                # create new users
                print("create new user")
                new_user = User.objects.create(username=user_name, password=pass_word1)
                new_user.save()
                return render(request, 'index.html')
            else:
                return render(request, 'register.html', {"msg": "Two password not the same, Please try again."})
    return render(request, 'register.html')
