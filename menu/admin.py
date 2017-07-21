# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from menu.models import *

@admin.register(Menu, Option, TraderProfile, EmployeeProfile)
class MenuAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'
