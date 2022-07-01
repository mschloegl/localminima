#!/bin/bash

SCRIPT=$1
IMAGE=localminima
CONTAINER=${IMAGE}_container

docker container rm $CONTAINER -f

docker run -d --name $CONTAINER $IMAGE $SCRIPT

sleep 3 

docker cp $CONTAINER:/app/artifacts/performance.log ./artifacts
docker cp $CONTAINER:/app/artifacts/plot.png ./artifacts

docker container rm $CONTAINER -f 


