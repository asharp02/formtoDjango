from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^poster/new/$', views.Poster_add.poster_new, name='poster_new'),
	url(r'^course/new/$', views.Course_add.course_new, name='course_new'),
	url(r'^poster/update/(?P<pk>\d+)/$', views.PosterUpdate.as_view(), name='poster_edit'),
	url(r'^poster/update/$', views.PosterSearch.poster_search, name='poster_search'),
	url(r'^poster/success/$', views.PosterSuccess.poster_success, name='poster_succ'),
]
