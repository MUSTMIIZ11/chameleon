from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

# Create your forms here.

# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
#
#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user


# Create your models here.
class User(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    create_time = models.DateField()

    def __str__(self):
        return self.username

