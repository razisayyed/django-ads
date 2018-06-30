from __future__ import unicode_literals

from django import forms
from django.conf import settings
from django.core.files.images import get_image_dimensions
from django.utils.translation import ugettext as _


class AdImageInlineForm(forms.ModelForm):

    def clean(self):
        super(AdImageInlineForm, self).clean()
        device = self.cleaned_data.get('device', None)
        image = self.cleaned_data.get('image', None)
        ad = self.cleaned_data.get('ad', None)
        if image and device and ad:
            allowed_size = settings.ADS_ZONES.get(ad.zone, {}). \
                get('ad_size', {}). \
                get(device, settings.ADS_DEFAULT_AD_SIZE)
            allowed_w, allowed_h = allowed_size.split('x')
            w, h = get_image_dimensions(image.file)
            if (allowed_w and w != int(allowed_w)) or (allowed_h and h != int(allowed_h)):
                self.add_error(
                    'image', _('Image size must be %(size)s') % {
                        'size': allowed_size, })
