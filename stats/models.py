from django.db import models
from shortener.models import URL

# Create your models here.
class StatisticsManager(models.Manager):
    def new_redirect(self, URLInstance):
        if isinstance(URLInstance, URL):
            obj, created = self.get_or_create(pk = 1)
            obj.total_redirect_count += 1
            obj.save()
            return obj.total_redirect_count
        return None

    def new_link_shortened(self, URLInstance):
        if isinstance(URLInstance, URL):
            if isinstance(URLInstance, URL):
                obj, created = self.get_or_create(pk=1)
                obj.total_link_shortened_count += 1
                obj.save()
                return obj.total_link_shortened_count
            return None

class Statistics(models.Model):
    total_link_shortened_count = models.BigIntegerField(default=0)
    total_redirect_count = models.BigIntegerField(default=0)

    object = StatisticsManager()

    def get_total_link_shortened_count(self):
        return self.total_link_shortened_count

    def get_total_redirect_count(self):
        return self.total_redirect_count