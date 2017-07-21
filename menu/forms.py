# -*- coding: utf-8 -*-
from django.forms import ModelForm
from menu.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'