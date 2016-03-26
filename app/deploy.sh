#!/bin/bash
echo updating testApp
docker pull epicallan/node-docker
docker stop testApp
docker rm testApp
docker run  -t -i -p 3000:3000 --name testApp --link redis:redis -d epicallan/node-docker
