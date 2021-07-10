# HWSubs
Homework submission sample project implemented in Django Rest framework.

### Requirements
- Docker
- Docker-Compose

### Assumptions
- django `is_staff` user field is used to distinguish teachers v. students.
- django Group object is used as "classes" where students belong.
- Refer to API docs for more details.
 

### Instructions
- run `docker-compose up` in base directory.
- attach to web docker image (do `docker ps` to get container id) and run tests.
- log on to http://0.0.0.0:8000/ on a browser
- attach to web docker image (do `docker ps` to get container id) and create a superuser and student users.
- play with the frontend DRF API interface.

### TODO
- use UUIDS.
- a lot more tests.
- more documentation.
- more robust filtering.
- tailor API to frontend requirements.
- have restrictions (students should submit 1 submission/assignment). 

