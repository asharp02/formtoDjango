from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^poster/new/$', views.poster_new, name='poster_new'),
	url(r'^course/new/$', views.course_new, name='course_new'),

]
