from appconf import AppConf
from django.utils.translation import ugettext_lazy as _

gettext = lambda s: s

class AdsConf(AppConf):

    class Meta:
        prefix = 'ads'

    ZONES = {
        'header': {
            'name': gettext('Header'),
            'ad_size': {
                'xs': '720x150',
                'sm': '800x90',
                'md': '800x90',
                'lg': '800x90'
            }
        },
        'content': {
            'name': gettext('Content'),
            'ad_size': {
                'xs': '720x150',
                'sm': '800x90',
                'md': '800x90',
                'lg': '800x90'
            }
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
