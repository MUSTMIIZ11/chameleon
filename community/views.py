from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    context = dict()
    context['hello'] = 'You are now in the community app!'
    return render(request, 'navigation.html', context)
