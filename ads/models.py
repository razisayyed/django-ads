from __future__ import unicode_literals

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from ads.conf import settings
from ads.managers import AdManager


class Advertiser(models.Model):
    """ A Model for our Advertiser.  """
    company_name = models.CharField(
        verbose_name=_(u'Company Name'), max_length=255)
    website = models.URLField(verbose_name=_(u'Company Site'))
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
        verbose_name=_('Created By'))

    class Meta:
        verbose_name = _('Advertiser')
        verbose_name_plural = _('Advertisers')
        ordering = ('company_name',)

    def __str__(self):
        return self.company_name

    def get_website_url(self):
        return self.website


class Category(models.Model):
    """ a Model to hold the different Categories for adverts """
    title = models.CharField(
        verbose_name=_('Title'), max_length=255)
    description = models.TextField(
        verbose_name=_('Description'), blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
        verbose_name=_('Created By'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('title',)

    def __str__(self):
        return self.title


def now_plus_1_day():
    return timezone.now() + timezone.timedelta(days=1)


class Ad(models.Model):
    """
    This is our base model, from which all ads will inherit.
    The manager methods for this model will determine which ads to
    display return etc.
    """
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    url = models.URLField(verbose_name=_('Advertised URL'))

    publication_date = models.DateTimeField(
        verbose_name=_('Start showing'),
        default=timezone.now)
    publication_date_end = models.DateTimeField(
        verbose_name=_('Stop showing'),
        default=now_plus_1_day)

    # Relations
    advertiser = models.ForeignKey(
        Advertiser, on_delete=models.CASCADE, verbose_name=_("Ad Provider"))
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name=_("Category"), blank=True, null=True)
    zone = models.CharField(
        verbose_name=_('Zone'), max_length=100)
    weight = models.IntegerField(
        verbose_name=_('Weight'),
        help_text=_('Weight of the ad relative to other ads '
                    'in the same zone.<br />'
                    'Ad with higher weight will be '
                    'displayed more frequently.'),
        default=1,
        validators=[MinValueValidator(1)])

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
        verbose_name=_('Created By'))

    objects = AdManager()

    class Meta:
        verbose_name = _('Ad')
        verbose_name_plural = _('Ads')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ads:ad-click', kwargs={
            'pk': self.id})


class AdImage(models.Model):
    ad = models.ForeignKey(
        Ad, on_delete=models.CASCADE, verbose_name=_('Ad'),
        related_name='images')
    device = models.CharField(
        verbose_name=_('Device'), max_length=2, choices=settings.ADS_DEVICES)
    image = models.ImageField(verbose_name=_('Image'), max_length=255)

    @property
    def size(self):
        size = settings.ADS_ZONES.get(self.ad.zone, {}). \
            get('ad_size', {}). \
            get(self.device, None)
        return size or settings.ADS_DEFAULT_AD_SIZE

    def __str__(self):
        return self.get_device_display()


class Impression(models.Model):
    """
    The AdImpression Model will record every time the ad is loaded on a page
    """
    ad = models.ForeignKey(
        Ad, on_delete=models.CASCADE, verbose_name=_('Ad'),
        related_name='impressions')
    impression_date = models.DateTimeField(
        verbose_name=_('When'), auto_now_add=True)
    source_ip = models.GenericIPAddressField(
        verbose_name=_('Source IP Address'), null=True, blank=True)
    session_id = models.CharField(
        verbose_name=_('Source Session ID'),
        max_length=40, null=True, blank=True)

    class Meta:
        verbose_name = _('Ad Impression')
        verbose_name_plural = _('Ad Impressions')
        index_together = (
            ('ad', 'session_id', )
        )

    def __str__(self):
        return force_text(self.ad)


class Click(models.Model):
    """
    The AdClick model will record every click that a add gets
    """
    ad = models.ForeignKey(
        Ad, on_delete=models.CASCADE, verbose_name=_('Ad'),
        related_name='clicks')
    click_date = models.DateTimeField(
        verbose_name=_('When'), auto_now_add=True)
    source_ip = models.GenericIPAddressField(
        verbose_name=_('Source IP Address'), null=True, blank=True)
    session_id = models.CharField(
        verbose_name=_('Source Session ID'),
        max_length=40, null=True, blank=True)

    class Meta:
        verbose_name = _('Ad Click')
        verbose_name_plural = _('Ad Clicks')
        index_together = (
            ('ad', 'session_id', )
        )

    def __str__(self):
        return force_text(self.ad)
