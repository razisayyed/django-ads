from django.conf import settings
from django.utils.translation import gettext_lazy


def get_zones_choices():
    for key in sorted(settings.ADS_ZONES):
        yield (key, gettext_lazy(settings.ADS_ZONES[key].get('name', 'Undefined')))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', '')
    return ip
