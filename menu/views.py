# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.views.generic import *
from django.shortcuts import render, redirect
from datetime import datetime, time
from models import *
from forms import OrderForm

"""
    MENU
"""


class ListMenu(ListView):
    template_name = "menu.html"
    model = Menu
    context_object_name = 'menu'

    def get_queryset(self):
        if self.request.user.is_authenticated():
            qs = Menu.objects.filter(user=self.request.user)
            return qs

list_menu = ListMenu.as_view()


class CreateMenu(CreateView):
    template_name = 'menu_add.html'
    model = Menu
    fields = ('created_at','send',)
    success_url = reverse_lazy('list_menu')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateMenu, self).form_valid(form)

create_menu = CreateMenu.as_view()


class UpdateMenu(UpdateView):
    model = Menu
    fields = ('updated_at','send',)
    template_name = 'menu_add.html'
    success_url = reverse_lazy('list_menu')

update_menu = UpdateMenu.as_view()


"""
    OPTION
"""


class ListOption(ListView):
    """
        get_queryset : filter menu options
        get_context_data :  get menu context with foreign key in .html
    """
    template_name = "option.html"
    model = Option
    context_object_name = 'option'

    def get_queryset(self):
        qs = Option.objects.filter(menu__id=self.kwargs['pk'])
        return qs

    def get_context_data(self, **kwargs):
        ctx = super(ListOption, self).get_context_data(**kwargs)
        ctx['menu'] = Menu.objects.get(pk=self.kwargs['pk'])
        return ctx

list_option = ListOption.as_view()


class CreateOption(CreateView):
    """
        get_success_url :  reserve lazy for list option (option/menu_id)
    """
    template_name = 'option_add.html'
    model = Option
    fields = ('description',)

    def form_valid(self, form):
        menu = Menu.objects.get(pk=self.kwargs['pk'])
        form.instance.menu = menu
        return super(CreateOption, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_option', kwargs={'pk': self.object.menu.pk})

create_option = CreateOption.as_view()


class UpdateOption(UpdateView):
    """
        get_success_url :  reserve lazy for list option (option/menu_id)
    """
    model = Option
    fields = ('description',)
    template_name = 'option_add.html'

    def get_success_url(self):
        return reverse_lazy('list_option', kwargs={'pk': self.object.menu.pk})

update_option = UpdateOption.as_view()


"""
    MENU TODAY
"""


def menu_today(request, uuid):
    """
        Menu's today
    """
    date = datetime.today()
    menu = Menu.objects.get(created_at__year=date.year,
                            created_at__month=date.month,
                            created_at__day=date.day)

    options = Option.objects.filter(menu=menu)

    # Choose their preferred meal (until 11 AM CLT) and employee order form.
    if request.method == 'POST' :
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/#')
    else:
        form = OrderForm()

    context = {'options': options, 'form':form, 'menu':menu}
    template = "menu_today.html"
    return render(request, template, context)

