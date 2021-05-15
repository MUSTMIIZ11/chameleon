#!/bin/bash
# 容器名称
CONTAINER="chameleon"
IMAGE="$CONTAINER":latest
# 创建新镜像
docker build -t $IMAGE . && \
# delete running images

RUN_NAME="$CONTAINER""service"
if docker ps -a | grep -w $RUN_NAME
then
  docker rm -f $RUN_NAME
fi
# run new images
sudo docker run --name  "$RUN_NAME" -v /home/ubuntu/img/img:/code/chameleon/static/map_img  -p 9090:9090 -d"$CONTAINER"
echo "Run successfully"
