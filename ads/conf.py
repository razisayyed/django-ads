from django.conf import settings
from appconf import AppConf
from django.utils.translation import ugettext_lazy as _


gettext = lambda s: s


class AdsConf(AppConf):

    class Meta:
        prefix = 'ads'

    GOOGLE_ADSENSE_CLIENT = None  # 'ca-pub-xxxxxxxxxxxxxxxx'

    ZONES = {
        'header': {
            'name': gettext('Header'),
            'ad_size': {
                'xs': '720x150',
                'sm': '800x90',
                'md': '800x90',
                'lg': '800x90'
            },
            'google_adsense_slot': None,  # 'xxxxxxxxx',
            'google_adsense_format': None,  # 'auto'
        },
        'content': {
            'name': gettext('Content'),
            'ad_size': {
                'xs': '720x150',
                'sm': '800x90',
                'md': '800x90',
                'lg': '800x90'
            },
            'google_adsense_slot': None,  # 'xxxxxxxxx',
            'google_adsense_format': None,  # 'auto'
        },
        'sidebar': {
            'name': gettext('Sidebar'),
            'ad_size': {
                'xs': '720x150',
                'sm': '800x90',
                'md': '800x90',
                'lg': '800x90'
            }
        }
    }

    DEFAULT_AD_SIZE = '720x150'

    DEVICES = (
        ('xs', _('Smartphones')),
        ('sm', _('Tablets')),
        ('md', _('Small Desktops')),
        ('lg', _('Large Desktops'))
    )
