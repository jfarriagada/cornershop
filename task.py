# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from cornershop.celery_app import app
from cornershop import settings
from slackclient import SlackClient
import uuid
# https://nora.cornershop.io/menu/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

uuid = uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
url_menu_today = "http://localhost:8000/menu/%s" % str(uuid)

@app.task
def send_employee_mail(option):
    options = []

    for o in option:
        options.append(str(o.description))

    option_description = str(options)

    msg = "Estimado.\n El menu de hoy es : "+ option_description +". \nurl : "+ url_menu_today +" \nSaludos !"

    results = send_mail("Menu del dia.", str(msg),
                        settings.EMAIL_HOST_USER, ["jfarriagada91@gmail.com"],
                        fail_silently = False)
    print(results)


@app.task
def send_slack(option):
    slack_token = 'xoxp-215586501828-214994485553-215730040437-445c933bad60035ce2771ff6bdd851f4'
    sc = SlackClient(slack_token)

    options = []
    for o in option:
        options.append(str(o.description))

    #menu_created = instance.created_at
    option_description = str(options)

    sc.api_call(
        "chat.postMessage",
        channel="#almuerzo",
        text="Estimado. \nEl menu de hoy es :"+ option_description + "\nurl : "+ url_menu_today +" \nSaludos ! "
    )