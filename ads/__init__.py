import django

if django.VERSION < (3, 2):  # pragma: no cover - compatibility shim
    default_app_config = 'ads.apps.AdsConfig'

__version__ = '1.2.0'
