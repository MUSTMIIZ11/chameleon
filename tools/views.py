# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import base64

from django.views.decorators.csrf import csrf_exempt

from community.models import Map
from chameleon.settings import BASE_DIR
import os
def index(request):
    return render(request, 'tool.html')

@csrf_exempt
def save_map(request):
    # Save map from diagrams.net
    # map格式  mapId-userId-mapName
    imgstring = request.POST['map_data']
    map_name = request.POST['map_name']
    user_id =  request.POST['user_id']
    try:
        user_id = int(user_id)
    except:
        user_id = -1
    imgdata = base64.b64decode(imgstring)
    filename = str(user_id) +'-' + map_name
    map = Map.objects.create(map_name=map_name,user_id=user_id,map_url='/'+filename)
    map_dir = os.path.join(BASE_DIR,'image_map')
    if not os.path.exists(map_dir):
        os.makedirs(map_dir)
    with open(os.path.join(map_dir,str(map.id)+"-"+filename), 'wb') as f:
        f.write(imgdata)
    return JsonResponse({
        'status':'ok',
        'map_id': map.id,
        'map_name':map.map_name,
        'map_url':map.map_url,
        'user_id':map.user_id
    })