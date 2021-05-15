#!/bin/bash
# 容器名称
CONTAINER="chameleon"
IMAGE="$CONTAINER":latest
# 创建新镜像
docker build -t $IMAGE . && \
# delete running images
RUN_NAME="$CONTAINER""service"
docker rm -f `docker ps -a | grep -w RUN_NAME | awk '{print $1}'`
# run new images
docker run --name RUN_NAME -d "$CONTAINER"
echo "Run successfully"
