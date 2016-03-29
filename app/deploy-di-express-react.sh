#!/bin/bash
echo updating testApp
docker pull epicallan/node-docker
docker stop testApp
docker rm testApp
docker run  -t -i -p 8000:8000 --name di-express-react --link redis:redis -d epicallan/di-express-react
