import base64
import os
from io import BytesIO

import qrcode
from django.http import HttpResponse
from django.shortcuts import render

from chameleon.settings import MAP_DIR
from .models import Map
import qrcode
from chameleon import settings


def index(request):
    return render(request, 'community.html')

def download(request):
    return render(request, 'download.html')

def makeqrcode(request,data):

    url = os.path.join(settings.URL, "community/download")
    print(url)
    print(request)
    # url = os.path.join(settings.BASE_DIR, "static/img/portfolio/card3.jpg")
    img = qrcode.make(url)      #传入网址计算出二维码图片字节数据
    buf = BytesIO()                                 #创建一个BytesIO临时保存生成图片数据
    img.save(buf)                                   #将图片字节数据放到BytesIO临时保存
    image_stream = buf.getvalue()                   #在BytesIO临时保存拿出数据
#    imagepath = os.path.join(settings.BASE_DIR, "static/img/{}".format("qrcode"))  # 图片路径
#    with open(imagepath, 'rb') as f:
#        image_data = f.read()
    response = HttpResponse(image_stream, content_type="image/jpg")  #将二维码数据返回到页面
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
