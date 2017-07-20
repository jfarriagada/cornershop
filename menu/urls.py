from django.conf.urls import url

from menu.views import *

urlpatterns = [
    url(r'^$', list_menu, name='list_menu'),
    url(r'^add/$', create_menu, name='create_menu'),
    url(r'^edit/(?P<pk>\d+)/$', update_menu, name='update_menu'),

    # pk = menu id
    url(r'^option/(?P<pk>[0-9]+)/$', list_option, name='list_option'),
    url(r'^option/add/(?P<pk>[0-9]+)/$', create_option, name='create_option'),
    url(r'^option/edit/(?P<pk>[0-9]+)/$', update_option, name='update_option'),
]
