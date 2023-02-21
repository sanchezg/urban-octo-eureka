# urban-octo-eureka
Backend for an "OnlyFans" like app

## Setting up using Docker

1. Run `docker-compose -f docker/docker-compose.yml build eureka` to build images
2. Run `docker-compose -f docker/docker-compose.yml run -p8000:8000 eureka /bin/bash` to run container.
3. Inside container bash shell, run `python3 manage.py runserver 0.0.0.0:8000` to run development server.
4. Go to `localhost:8000` in your preferred browser.
