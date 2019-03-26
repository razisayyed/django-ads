from ads.views import AdImpressionView, AdClickView
from django.conf.urls import url


app_name = 'ads'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$',
        AdClickView.as_view(), name='ad-click'),
    url(r'^get-ads-by-zones/$',
        AdImpressionView.as_view(), name='ad-impression'),
]
