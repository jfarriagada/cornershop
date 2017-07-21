# Cornershop's Backend Test by Farriagada

## virtualenv
```shell
$ pip install virtualenv
$ virtualenv venv_cornershop
$ cd venv_cornershop
$ source bin/activate
```

## project
```shell
$ git clone https://github.com/jfarriagada/cornershop.git
$ cd cornershop/
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

## setup load initial data (Order matters)
```shell
$ python manage.py loaddata menu/fixtures/users.json
$ python manage.py loaddata menu/fixtures/trader_profile.json
$ python manage.py loaddata menu/fixtures/employees.json
$ python manage.py loaddata menu/fixtures/menu.json
$ python manage.py loaddata menu/fixtures/option.json
$ python manage.py loaddata menu/fixtures/order.json
```

## Terminal 1 run django
```shell
$ python manage.py runserver
```

## Terminal 2 run redis
```shell
redis-4.0.0$ src/redis-server
```

## Terminal 3 run celery
```shell
celery worker -A cornershop.celery_app --loglevel=DEBUG
```

## init
ADMIN cornershop:cornershop
USER nora:lavendedora

## menú
http://localhost:8000/menu/886313e1-3b8a-5372-9b90-0c9aee199e5d

## test
$ python manage.py test menu