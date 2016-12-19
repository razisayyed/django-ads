from ads.querysets import AdQuerySet
from django.db.models import Manager, Count


class AdManager(Manager):
    def get_queryset(self):
        return AdQuerySet(self.model)

    def public(self):
        return self.get_queryset().public()

    def zone_ads(self, zone):
        return self.get_queryset().zone_ads(zone)

    def current_ad(self, zone):
        ads = list(self.zone_ads(zone).public().annotate(
            impressions_count=Count('impressions')
        ))
        if not ads:
            return None
        total_weight = 0
        total_impressions = 0
        for ad in ads:
            total_weight += ad.weight
            total_impressions += ad.impressions_count
        for ad in ads:
            allowed_impressions = (float(ad.weight) / float(total_weight)) * float(total_impressions)
            if ad.impressions_count <= allowed_impressions:
                return ad
        return ads[0]
