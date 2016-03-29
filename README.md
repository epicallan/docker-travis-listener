# docker-travis-listener
- listens for docker automated builds on docker hub for a tracked image
- Triggers a new deploy of the container on a host server if build was successful
  on docker hub and tests passed on Travis.
- if you have gunicorn installed cd into app folder and run ``gunicorn -w 2 app:app``

# TODO
- Travis webhook is currently not working and needs to be fixed
