from appconf import AppConf
from django.utils.translation import ugettext_lazy as _

gettext = lambda s: s

class AdsConf(AppConf):

    class Meta:
        prefix = 'ads'

    ZONES = {
        'header': {
            'name': gettext('Header'),
            'ad_size': '800x90',
        },
        'content': {
            'name': gettext('Content'),
            'ad_size': '500x270',
        },
        'sidebar': {
            'name': gettext('Sidebar'),
            'ad_size': '270x270',
        }
    }