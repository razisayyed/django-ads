from django.db.models import QuerySet
from django.utils import timezone


class AdQuerySet(QuerySet):

    def public(self):
        return self.filter(
            publication_date__lte=timezone.now(),
            publication_date_end__gt=timezone.now())

    def zone_ads(self, zone):
        return self.filter(
            zone=zone)
