#!/bin/bash

echo "## LOAD INITIAL DATA ## "

python manage.py loaddata menu/fixtures/users.json
python manage.py loaddata menu/fixtures/trader_profile.json
python manage.py loaddata menu/fixtures/employees.json
python manage.py loaddata menu/fixtures/menu.json
python manage.py loaddata menu/fixtures/option.json
python manage.py loaddata menu/fixtures/order.json
