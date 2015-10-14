"""ez_migrate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from web.configurations.views.configuration import ConfigurationViewSet
from web.configurations.views.new_configuration import NewConfigurationViewSet
from web.constants import METHOD_POST_CREATE, METHOD_GET_LIST, METHOD_PUT_UPDATE

urlpatterns = [
    url(r'^new/$', NewConfigurationViewSet.as_view(METHOD_POST_CREATE), name='new_configuration'),
    url(r'^fetch/$', ConfigurationViewSet.as_view(METHOD_GET_LIST), name='configuration'),
    url(r'^edit/$', ConfigurationViewSet.as_view(METHOD_PUT_UPDATE), name='edit_configuration'),
]
