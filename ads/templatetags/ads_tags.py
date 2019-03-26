from __future__ import unicode_literals

from django import template
from django.conf import settings
from django.utils import timezone

from ads.models import Ad

register = template.Library()


@register.inclusion_tag('ads/tags/render_ads_zone.html', takes_context=True)
def render_ads_zone(context, zone):
    """
    Returns an advertise for a ``zone``.
    Tag usage:
    {% load ads_tags %}
    {% render_zone 'zone' %}
    """
    context.update({
        'google_adsense_client': settings.ADS_GOOGLE_ADSENSE_CLIENT,
        'zone': zone,
        'zone_info': settings.ADS_ZONES.get(zone, None)
    })
    return context


@register.simple_tag
def get_ads_count(zone):
    """
    Returns ads count for ``zone``.
    Tag usage:
    {% load ads_tags %}
    {% get_ads_count 'zone' as ads_count %}
    {% get_ads_count 'zone1,zone2,zone3' as ads_count %}
    """
    zone = zone.split(',')
    return Ad.objects.public().filter(zone__in=zone).count()
