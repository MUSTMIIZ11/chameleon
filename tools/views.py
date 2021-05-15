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
def check(request):
    user_id = request.POST['user_id']
    print(f"the user id {user_id}")
    # if user_id == -1:
    #     return
    return JsonResponse({
        "user_id": user_id
    })
    # if user_id != -1:
    #     print("testtttt")
    #     return render(request, 'login.html')
    # else:
    #     print("toollllllll")
    #     # Not login
    #     return render(request, 'tool.html')


import cairosvg


@csrf_exempt
def save_map(request):
    # Save map from diagrams.net
    # map格式  mapId-userId-mapName
    imgstring = request.POST['map_data']
    map_name = request.POST['map_name']
    user_id = request.POST['user_id']
    try:
        user_id = int(user_id)
    except:
        user_id = -1
    imgdata = base64.b64decode(imgstring)
    # filename = str(user_id) + '-' + map_name
    # filename 1. 创建数据库里map_url('map_img/xxx.jpg') 2. 图片存储路径，跟前面路径一样，存jpg。
    filename = 'map_img/' + map_name + '.svg'
    map = Map.objects.create(map_name=map_name, user_id=user_id, map_url=filename)
    # map_dir = os.path.join(BASE_DIR, 'image_map')
    map_dir = os.path.join(BASE_DIR, 'static/')
    # if not os.path.exists(map_dir):
    #     os.makedirs(map_dir)
    # with open(os.path.join(map_dir, str(map.id)+"-"+filename) + '.svg', 'wb') as f:
    with open(os.path.join(map_dir, filename), 'wb') as f:
        f.write(imgdata)
    cairosvg.svg2png(url=os.path.join(map_dir, filename),
                     write_to=os.path.join(map_dir, 'map_img/' + map_name + '.jpg'))
    return JsonResponse({
        'status': 'ok',
        'map_id': map.id,
        'map_name': map.map_name,
        'map_url': map.map_url,
        'user_id': map.user_id
    })
