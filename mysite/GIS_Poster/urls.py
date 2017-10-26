from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^poster/new/$', views.poster_new, name='poster_new'),
]
