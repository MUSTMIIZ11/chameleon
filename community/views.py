from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Map


def index(request):
    ordered_map = Map.objects.order_by('-like').all()[:9]
    display_map_list = dict()
    for i in range(9):
        display_map_list['map' + str(i)] = ordered_map[i].map_url
    print(display_map_list)
    return render(request, 'community.html', display_map_list)
