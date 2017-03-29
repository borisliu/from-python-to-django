from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<pagename>\w+)/$', views.index),
    url(r'^(?P<pagename>\w+)/edit/$', views.edit),
    url(r'^(?P<pagename>\w+)/save/$', views.save),
]