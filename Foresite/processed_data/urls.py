from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.processed_data, name='processed'),
    url(r'^(?P<csv_file>[-\w]+.txt)/$', views.detail, name='detail')
]
