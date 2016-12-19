from ads.views import AdClickView
from django.conf.urls import url


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', AdClickView.as_view(), name='ad-click'),
]
