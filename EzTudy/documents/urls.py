from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^school/(?P<sc_id>[0-9]+)/$', views.mainsc, name='mainsc'),
    url(r'^school/world', views.worldsc, name='worldsc'),
    url(r'^tm', views.text_tm, name='text_tm'),
]