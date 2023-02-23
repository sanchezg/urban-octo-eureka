# urban-octo-eureka
Backend for an "OnlyFans" like app.

Eureka is the codename for a web app where users (publishers) can offer different contents (video, documents or images) by subscription (access to all their content), by selling them individually, or free. And then other users (consumers) can access the different purchased or free content.

# About the name
The name is just the suggested one by GitHub repos. It's really difficult naming things and I won't spend time with it.
If you clone this, give it a better name ;)

## Setting up using Docker

1. Run `docker-compose -f docker/docker-compose.yml build eureka` to build images
2. Run `docker-compose -f docker/docker-compose.yml run -p8000:8000 eureka /bin/bash` to run container.
3. Inside container bash shell, run `python3 manage.py runserver 0.0.0.0:8000` to run development server.
4. Go to `localhost:8000` in your preferred browser.
