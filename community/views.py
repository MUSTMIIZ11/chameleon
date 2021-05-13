from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import qrcode
from io import BytesIO
import os
from chameleon import settings


def index(request):
    return render(request, 'community.html')


def makeqrcode(request, data):
    url = "http://www.test.com"
    img = qrcode.make(url)      #传入网址计算出二维码图片字节数据
    buf = BytesIO()                                 #创建一个BytesIO临时保存生成图片数据
    img.save(buf)                                   #将图片字节数据放到BytesIO临时保存
    image_stream = buf.getvalue()                   #在BytesIO临时保存拿出数据
#    imagepath = os.path.join(settings.BASE_DIR, "static/img/{}".format("qrcode"))  # 图片路径
#    with open(imagepath, 'rb') as f:
#        image_data = f.read()
    response = HttpResponse(image_stream, content_type="image/jpg")  #将二维码数据返回到页面
    return response


