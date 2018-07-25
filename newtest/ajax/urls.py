from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="ajax/ajax.html")),
    url(r'^input/$', views.input),
]