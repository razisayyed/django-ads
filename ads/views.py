from ads.models import Ad, Click
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import View
from django.views.generic.detail import SingleObjectMixin

from ads.utils import get_client_ip


class AdClickView(
        SingleObjectMixin, View):

    def get_queryset(self):
        return Ad.objects.all()

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        if request.session.session_key:
            click, created = Click.objects.get_or_create(
                ad=ad,
                session_id=request.session.session_key,
                defaults={
                    'click_date': timezone.now(),
                    'source_ip': get_client_ip(request),
                })
        return HttpResponseRedirect(ad.url)
