# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from datetime import datetime, time
from menu.models import Menu


class MenuTest(TestCase):

    fixtures = [
        "test/menu_menu",
    ]

    def setUp(self):
        # Menu's instance
        self.menu = Menu(pk=1)
        self.menu.save()

    def test_is_updated(self):
        # No updated
        get_updated = self.menu.is_updated()
        self.assertEquals(get_updated, False)

    def test_is_send(self):
        # Send False
        get_send = self.menu.is_send()
        self.assertEquals(get_send, False)