# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from task import send_employee_mail, send_slack
from django.utils import timezone
from datetime import datetime, time


class TraderProfile(models.Model):
    trader = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        verbose_name = 'Trader Profile'

    def __str__(self):
        return self.trader.username


class Employee(models.Model):
    rut = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=70, null=True, blank=True)

    class Meta:
        verbose_name = 'Employee'

    def __str__(self):
        return self.email


class Menu(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    send = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Menu'

    def __str__(self):
        return self.send

    def choose_menu(self):
        """
            Choose their preferred meal (until 11 AM CLT)
        """
        today_date = datetime.now()
        today_time = time(today_date.hour, today_date.minute, today_date.second)
        qs = True if today_time.hour <= 10 and today_time.minute <= 60 else False
        return qs

    def is_updated(self):
        """
            Show if the menu has been updated
        """
        created_at_time = time(self.created_at.hour, self.created_at.minute, self.created_at.second)
        updated_at_time = time(self.updated_at.hour, self.updated_at.minute, self.updated_at.second)

        qs = False if created_at_time == updated_at_time else True
        return qs

    def is_send(self):
        """
            Show if the menu has been sending
        """
        qs = True if self.send == True else False
        return qs


class Option(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    description = models.CharField(max_length=370, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Option'

    def __str__(self):
        return self.description

    def is_update(self):
        """
            Show if the option has been updated
        """
        created_at_time = time(self.created_at.hour, self.created_at.minute, self.created_at.second)
        updated_at_time = time(self.updated_at.hour, self.updated_at.minute, self.updated_at.second)

        qs = False if created_at_time == updated_at_time else True
        return qs


class Order(models.Model):
    rut_employee = models.CharField(max_length=10, null=True, blank=True)
    option = models.IntegerField(default=0, null=True, blank=True)
    customization = models.CharField(max_length=170, null=True, blank=True)
    extra_large = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Employee Order'

    def __str__(self):
        return self.rut_employee


"""
    SIGNALS to send email and slack
"""


@receiver(post_save, sender=Menu)
def post_menu(instance, **kwargs):
    """
        Menu slack and email send when Boolean send is True
    """
    if instance.send == True:
        option = Option.objects.filter(menu__id=instance.id)

        send_employee_mail(option)
        send_slack(option)