# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from task import send_employee_mail, send_slack
import datetime
from django.utils import timezone


class TraderProfile(models.Model):
    trader = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        verbose_name = 'Trader Profile'

    def __str__(self):
        return self.trader.username


class EmployeeProfile(models.Model):
    employee = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        verbose_name = 'Employee Profile'

    def __str__(self):
        return self.employee.username


class Menu(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class Option(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    description = models.CharField(max_length=370, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


"""
    SIGNALS to send email and slack
"""
@receiver(post_save, sender=Menu)
def post_menu(instance, **kwargs):
    option = Option.objects.filter(menu__id=instance.id)

    send_employee_mail(option)
    send_slack(option)