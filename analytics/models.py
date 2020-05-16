from django.db import models
from shortener.models import URL
# Create your models here.

class ClickEventManager(models.Manager):
    def create_event(self, URLInstance):
        if isinstance(URLInstance, URL):
            obj, created = self.get_or_create(url_model_tuple = URLInstance)
            obj.click_count += 1
            obj.save()
            return obj.click_count
        return None

class ClickEvent(models.Model):
    url_model_tuple = models.OneToOneField(URL, primary_key=True, on_delete=models.CASCADE)
    click_count = models.IntegerField(default=0)

    objects = ClickEventManager()

    def __str__(self):
        return '{count}'.format(count = self.click_count)