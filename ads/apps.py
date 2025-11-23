from __future__ import unicode_literals

from django.apps import AppConfig

from ads.compat import gettext_lazy as _


class AdsConfig(AppConfig):
    name = 'ads'
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = _('Ads Management System')
