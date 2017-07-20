# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime


class TraderProfile(models.Model):
    trader = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        verbose_name = 'Trader Profile'

    def __str__(self):
        return self.trader.username


class Menu(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())


class Option(models.Model):
    menu = models.ForeignKey(Menu)
    description = models.CharField(max_length=370, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

