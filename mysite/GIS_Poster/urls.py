from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^poster/new/$', views.Poster_add.poster_new, name='poster_new'),
	url(r'^course/new/$', views.Course_add.course_new, name='course_new'),
	url(r'^poster/edit', views.Poster_update.edit_poster, name='poster_edit'),


]
