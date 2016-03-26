#!/bin/bash
echo test
docker pull account/app
docker stop myapp
docker rm myapp
docker run  -t -i -p 5000:5000 --name myapp --link redis:redis --link mongo:mongo  -d account/app
