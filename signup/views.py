from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello world, you are at poll index")

# def index(request):
#     context = dict()
#     context['hello'] = 'Hello World! You are now in the welcome app!'
#     return render(request, 'navigation.html', context)


def index(request):
    return render(request, 'login.html')