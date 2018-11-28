from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.processed_data, name='processed'),
    url(r'^(?P<csv_name>[-\w]+)/$', views.detail, name='detail')
]
