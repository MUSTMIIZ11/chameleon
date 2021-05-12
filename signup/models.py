from django import forms
from django.contrib.auth.forms import UserCreationForm
<<<<<<< Updated upstream
from django.contrib.auth.models import User
=======
# from django.contrib.auth.models import User
from django.db import models
>>>>>>> Stashed changes


# Create your forms here.

<<<<<<< Updated upstream
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
=======
# Create your models here.
class User(models.Model):
    # userid = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    create_time = models.DateField(auto_now=True)
>>>>>>> Stashed changes

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
