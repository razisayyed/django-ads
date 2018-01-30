from ads.views import AdClickView
from django.conf.urls import url


app_name = 'ads'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', AdClickView.as_view(), name='ad-click'),
]
