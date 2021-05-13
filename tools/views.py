# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #
    return render(request, 'tool.html')


def save_map(request):
    # Save map from diagrams.net
    return HttpResponse('OK')