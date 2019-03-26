from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ads.models import Click, Impression


def get_zones_choices():
    for key in sorted(settings.ADS_ZONES):
        yield (key, _(settings.ADS_ZONES[key].get('name', 'Undefined')))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', '')
    return ip


def update_clicks(ad, request):
    if ad is not None:
        if request.session.session_key:
            impression, created = Click.objects.get_or_create(
                ad=ad,
                session_id=request.session.session_key,
                defaults={
                    'click_date': timezone.now(),
                    'source_ip': get_client_ip(request),
                })


def update_impressions(ad, request):
    if ad is not None:
        if request.session.session_key:
            impression, created = Impression.objects.get_or_create(
                ad=ad,
                session_id=request.session.session_key,
                defaults={
                    'impression_date': timezone.now(),
                    'source_ip': get_client_ip(request),
                })
