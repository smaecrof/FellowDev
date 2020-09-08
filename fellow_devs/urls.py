"""Defines URL patterns for fellow_devs"""

from django.conf.urls import url

from . import views

urlpatterns = [
        # Home Page
        url(r'^$', views.index, name='index'),
]
