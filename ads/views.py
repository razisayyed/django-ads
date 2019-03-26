from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import View
from django.views.generic.detail import SingleObjectMixin

from braces.views import JSONResponseMixin

from ads.models import Ad, Click
from ads.utils import update_clicks, update_impressions


class AdImpressionView(JSONResponseMixin, View):
    json_dumps_kwargs = {u"indent": 2}

    def get_object(self):
        zone = self.kwargs.get('zone', None)
        return Ad.objects.random_ad(zone)

    def get_ad_context_dict(self, zone):
        ad = Ad.objects.random_ad(zone)
        if ad:
            context_dict = {
                'url': ad.get_absolute_url(),
                'images': {}
            }
            for image in ad.images.all():
                context_dict['images'].update({
                    image.device: {
                        'url': image.image.url,
                        'size': image.size
                    }
                })
            return context_dict
        return None
        
    def get(self, request, *args, **kwargs):
        data = {}
        zones = request.GET.getlist('zones[]', []);
        # print(zones)
        for zone in zones:
            zone_conf = settings.ADS_ZONES.get(zone, {})
            ad = self.get_ad_context_dict(zone)
            if zone_conf:
                data.update({
                    zone: {
                        'ad': ad,
                        'conf': zone_conf
                    }
                })
        context_dict = {
            'google_adsense_client': settings.ADS_GOOGLE_ADSENSE_CLIENT,
            'viewports': settings.ADS_VIEWPORTS,
            'zones': data
        }
        return self.render_json_response(context_dict)
    
        """
        context_dict = {
            'zone': self.kwargs.get('zone', None)
        }
        ad = self.get_object()
        if ad:
            ct = context_dict.update({
                'url': ad.url,
                'images': {}
            })
            for image in ad.images.all():
                context_dict['images'].update({
                    image.device: {
                        'image': image.image.url,
                        'size': image.size
                    }
                })
        return self.render_json_response(context_dict)
        """

class AdClickView(SingleObjectMixin, View):

    def get_queryset(self):
        return Ad.objects.all()

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        update_clicks(ad, request)
        return HttpResponseRedirect(ad.url)
