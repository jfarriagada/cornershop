# Cornershop's Backend Test by Farriagada

## Virtualenv
```shell
$ pip install virtualenv
$ virtualenv venv_cornershop
$ source venv_cornershop/bin/activate
```
## Add file secret.py
```python
# -*- coding: utf-8 -*-

EMAIL_HOST_USER = 'your_email'
EMAIL_HOST_PASSWORD = 'your_email_password'
DEFAULT_FROM_EMAIL = 'jfarriagada91@gmail.com'
TOKEN_SLACK = 'your_token_slack'
```

## Project
```shell
$ git clone https://github.com/jfarriagada/cornershop.git
$ cd cornershop/
$ pip install -r requirements.txt
$ python manage.py migrate
```

## Setup load initial data (Order matters) or "one click"
```shell
$ python manage.py loaddata menu/fixtures/users.json
$ python manage.py loaddata menu/fixtures/trader_profile.json
$ python manage.py loaddata menu/fixtures/employees.json
$ python manage.py loaddata menu/fixtures/menu.json
$ python manage.py loaddata menu/fixtures/option.json
$ python manage.py loaddata menu/fixtures/order.json
```

```shell
$ chmod +x one_click.sh
$ ./one_click.sh
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

## Login
ADMIN cornershop:cornershop <br />
USER nora:lavendedora

## Menu
http://localhost:8000/menu/886313e1-3b8a-5372-9b90-0c9aee199e5d

## Test
$ python manage.py test menu

## Youtube Vídeo
[https://youtu.be/_T3Q_wvCns0](https://youtu.be/_T3Q_wvCns0)
