Django Ads Management System
============================

a Django Application to make it easy to add Simple (Image) Advertisements to your project.

Each Ad has a **title**, a **URL** to redirect to, an **image** to be displayed in the template as a link, a **start & end dates**, and a **weight** relative to other Ads in the same zone. The higher the weight, the more frequently the Ad will be displayed.

Each time an Ad is displayed an **Impression** will be saved to the database about it with session id and source ip address, and each time it will be clicked a **click** will be saved in the database about it with the same info.

Installation:
-------------

Install the package using pip:

    pip install django-ads

Run django Migration to add tables to your database:

    python manage.py migrate ads

Configuration:
--------------

make sure ``django.template.context_processors.request`` is included in ``context_processors``

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


make sure ``django.contrib.sessions.middleware.SessionMiddleware`` is included to ``MIDDLEWARE_CLASSES/MIDDLEWARE``

prior to Django 1.10

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

  ADS_ZONES = {
      'header': {
          'name': _('Header'),
          'ad_size': '800x90'
      },
      'content': {
          'name': _('Content'),
          'ad_size': '500x90',
      },
      'sidebar': {
          'name': _('Sidebar'),
          'ad_size': '270x270'
      },
  }

Where each element in ``ADS_ZONES`` defines a ``zone`` that can be used in your templates to display ads. Each zone must have a name to be used in admin interface when adding ads, and a size to be used to resize images in tempaltes using ``easy-thumbnails``.

Usage:
------

Add Advertisers, Categories, and Ads using Django admin interface.

load ``ads_tags`` in your template:

.. code-block:: python

  {% load ads_tags %}

use ``render_zone`` in your template where you want your ads to appear:

.. code-block:: python

  {% render_zone 'zone_name' %}

    
Changelog:
----------

0.1.1 (2016-12-20):
- add missing templates directory.

