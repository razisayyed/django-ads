Django Ads Management System
============================

a Django Application to make it easy to add Simple (Image) Advertisements to your project.

Each Ad has a **title**, a **URL** to redirect to, an **image** to be displayed in the template as a link, a **start & end dates**, and a **weight** relative to other Ads in the same zone. The higher the weight, the more frequently the Ad will be displayed.

Each time an Ad is displayed an **Impression** will be saved to the database about it with session id and source ip address, and each time it will be clicked a **click** will be saved in the database about it with the same info.

Installation:
-------------

Install the package using pip:

.. code-block:: python

  pip install django-ads

Run django Migration to add tables to your database:

.. code-block:: python

  python manage.py migrate ads

Configuration:
--------------

Add ``'ads'`` to your ``INSTALLED_APPS``

Make sure ``django.template.context_processors.request`` is included in ``context_processors``

.. code-block:: python

  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  ...
                  'django.template.context_processors.request',
                  ...
              ],
          },
      },
  ]


Make sure ``django.contrib.sessions.middleware.SessionMiddleware`` is included to ``MIDDLEWARE_CLASSES/MIDDLEWARE``

Prior to Django 1.10

.. code-block:: python

  MIDDLEWARE_CLASSES = [
      ...
      'django.contrib.sessions.middleware.SessionMiddleware',
      ...
  ]

Django 1.10 (new style)

.. code-block:: python

  MIDDLEWARE = [
      ...
      'django.contrib.sessions.middleware.SessionMiddleware',
      ...
  ]

Add the following to your settings file:

.. code-block:: python

    ADS_GOOGLE_ADSENSE_CLIENT = None  # 'ca-pub-xxxxxxxxxxxxxxxx'

    ADS_ZONES = {
        'header': {
            'name': gettext('Header'),
            'ad_size': {
                'xs': '720x150',
                'sm': '800x90',
                'md': '800x90',
                'lg': '800x90',
                'xl': '800x90'                
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
                'lg': '800x90',
                'xl': '800x90'                
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
                'lg': '800x90',
                'xl': '800x90'
            }
        }
    }

    ADS_DEFAULT_AD_SIZE = '720x150'

    ADS_DEVICES = (
        ('xs', _('Extra small devices')),
        ('sm', _('Small devices')),
        ('md', _('Medium devices (Tablets)')),
        ('lg', _('Large devices (Desktops)')),
        ('xl', _('Extra large devices (Large Desktops)')),
    )
    
    ADS_VIEWPORTS = {
        'xs': 'd-block img-fluid d-sm-none',
        'sm': 'd-none img-fluid d-sm-block d-md-none',
        'md': 'd-none img-fluid d-md-block d-lg-none',
        'lg': 'd-none img-fluid d-lg-block d-xl-none',
        'xl': 'd-none img-fluid d-xl-block',
    }


Where each element in ``ADS_ZONES`` defines a ``zone`` that can be used in your templates to display ads. Each zone must have a name to be used in the admin interface when adding ads, and sizes to be used to display the ad images in templates.

This app has one template: ``ads/tags/render_ads_zone.html``. It makes some assumptions:

#. Your project uses Bootstrap (the ``visible-*`` and ``img-responsive`` CSS classes are used).

#. If you are using Google AdSense‎, it is assumed that you have ``'sekizai'`` in your ``INSTALLED_APPS`` and that your base template contains ``{% render_block "js" %}``.

If either of the above assumptions will cause a problem in your project, feel free to override the template.

Create a URL pattern in your urls.py:

.. code-block:: python

  from django.conf.urls import include, url

  urlpatterns = [
      ...
      url(r'^ads/', include('ads.urls')),
      ...
  ]

Usage:
------

Add Advertisers, Categories, and Ads using Django admin interface.

load ``ads_tags`` in your template:

.. code-block:: python

  {% load ads_tags %}

use ``render_ads_zone`` in your template where you want your ads to appear:

.. code-block:: python

  {% render_ads_zone 'zone_name' %}

use ``get_ads_count`` in your template to check if any zone has active ads.

.. code-block:: python

  {% get_ads_count 'zone1' as ads_count %}
  {{ get_ads_count 'zone1,zone2,zone3' as ads_count %}

Changelog:
----------

1.1.1 (2020-03-20):

- remove @python_2_unicode_compatible (removed in Django 3.0)

1.1.0 (2019-07-28):

- get_ads_count template tag added.
- fixed setup dependency (django-js-reverse has been added).

1.0.0 (2019-03-26):

- major change in functionality (switch to JS approach in rendering templates). You need jquery to be installed in frontend to use django-ads.
- Note: templates/ads/tags/render_ads_zone.html has been changed. If you use a custom template, then please take a look at the new version.

0.2.1 (2018-07-26): (Special Thanks to `@GabrielDumbrava <https://github.com/GabrielDumbrava>`_
)

- get_zones_choices now return choices sorted based on key
- Ad, Category, and Advertizer now stay on DB after deleting `created_by` user.
- fix get_absolute_url in Ad model.
- Add `ad` and `ad__zone` filters to impressions and clicks admin pages.
- Fix clicks and impressions admin search.

0.2.1 (2018-02-05):

- add long_description to setup.py

0.2.0 (2018-02-05): (Special Thanks to `@ataylor32 <https://github.com/ataylor32>`_
)

- add Django 2.0 support
- add missing dependency (Pillow)
- update README

0.1.8 (2017-06-24):

- fix googleads script tags to load multiple ad units in the same page

0.1.7 (2017-06-24):

- Please do not use this version

0.1.6 (2017-06-24):

- fix django-sekizai dependency version

0.1.5 (2017-06-24):

- add google adsense fallback

0.1.4 (2017-03-01):

- get client ip address from HTTP_X_FORWARDED_FOR if it exists.

0.1.3 (2017-02-08):

- remove dependency on easy-thumbnails.
- add Image validation to validate image size on upload using Admin interface.

0.1.2 (2017-02-08):

- add AdImage model to allow responsive ads.

0.1.1 (2016-12-20):

- add missing templates directory.
