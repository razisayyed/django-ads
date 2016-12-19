from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AdsConfig(AppConfig):
    name = 'ads'
    verbose_name = _('Ads Management System')
