from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^show/(?P<productID>[0-9]+)$', views.show, name = "show"),
    url(r'^edit/(?P<productID>[0-9]+)$', views.edit, name = "edit"),
	url(r'^update/(?P<productID>[0-9]+)$', views.update, name = "update"),
	url(r'^new$', views.new, name = "new"),
    url(r'^create$', views.create, name = "create"),
    url(r'^remove/(?P<productID>[0-9]+)$', views.destroy, name = "remove"),
]