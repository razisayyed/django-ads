from django.conf import settings
from django.utils.translation import gettext_lazy


def get_zones_choices():
    for key in settings.ADS_ZONES:
        yield (key, gettext_lazy(settings.ADS_ZONES[key].get('name', 'Undefined')))
