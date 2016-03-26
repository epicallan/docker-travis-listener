# docker-travis-listener
- listens for docker automated builds on docker hub of a tracked image
- Triggers a new deploy of the container on a host server if build was successful
  on docker hub and tests passed on Travis.
