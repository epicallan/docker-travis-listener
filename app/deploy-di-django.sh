#!/bin/bash
echo updating di-django App
docker pull epicallan/di-django
docker stop di-django
docker rm di-django
docker run  -t -i -p 8080:8080 --name di-django -d epicallan/di-django
