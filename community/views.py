import base64
import os
from io import BytesIO

import qrcode
from django.http import HttpResponse
from django.shortcuts import render

from chameleon.settings import MAP_DIR
from .models import Map
from signup.models import User
import qrcode
from chameleon import settings


def index(request):
    # sort the map data based on the 'like' attribute.
    # Select 9 map which have most likes.
    ordered_map = Map.objects.order_by('-like').all()[:9]
    # display_map_list = dict()
    # for i in range(9):
    #     display_map_list['map' + str(i)] = ordered_map[i].map_url
    #     # display_map_list['map' + str(i) + 'user'] = User.objects.get(id=ordered_map[i].user_id).username
    display_map_dict = dict()
    display_map_dict['map_user_all'] = list()
    print(display_map_dict)
    for i in range(9):
        temp = dict()
        temp['map'] = ordered_map[i].map_url
        temp['map_user'] = User.objects.get(id=ordered_map[i].user_id).username
        display_map_dict['map_user_all'].append(temp)
    print(display_map_dict)
    return render(request, 'community.html', display_map_dict)


from django.utils.http import  urlencode

def download(request):
    count = 0
    if request.method == "GET":
        img_url = request.GET.get('url')
        count += 1
        print("count:", count)
        print('img_url:', img_url)
    return render(request, 'download.html', {"img_url": img_url})


# def update_img_url(request):
#     if request.method == "GET":
#         img_url = request.GET.get('url')
#         print("img_url:", img_url)
#         return HttpResponse(request, {"img_url": img_url})

def makeqrcode(request, data):
    url = settings.URL+'/'+ "community/download?url=" + data
    # url = os.path.join(settings.BASE_DIR, "static/img/portfolio/card3.jpg")
    img = qrcode.make(url)  # 传入网址计算出二维码图片字节数据
    buf = BytesIO()  # 创建一个BytesIO临时保存生成图片数据
    img.save(buf)  # 将图片字节数据放到BytesIO临时保存
    image_stream = buf.getvalue()  # 在BytesIO临时保存拿出数据
    #    imagepath = os.path.join(settings.BASE_DIR, "static/img/{}".format("qrcode"))  # 图片路径
    #    with open(imagepath, 'rb') as f:
    #        image_data = f.read()
    response = HttpResponse(image_stream, content_type="image/jpg")  # 将二维码数据返回到页面
    return response


def get_all_maps(limit=None):
    dir = MAP_DIR
    maps = []
    for map_filename in os.path.dirname(dir):
        with open(map_filename, 'wb') as f:
            map_data = f.read()
            map_data = base64.b64decode(map_data)
        maps.append(bytes('data:image/svg+xml;base64,') + map_data)
    return maps
