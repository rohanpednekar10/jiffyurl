from django.db import models
from django.utils import timezone
from django.conf import settings
from datetime import timedelta, date
from django.urls import reverse
from .utils import create_shortcode
from .validators import validate_url

# create your variables here
SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

# Create your models here.
class URL(models.Model):
    url = models.CharField(max_length = 2000, validators=[validate_url])
    shortcode = models.CharField(max_length = SHORTCODE_MAX, unique=True, blank=True)
    date_of_creation = models.DateTimeField(default = timezone.now())
    date_of_expiry = models.DateTimeField(default = timezone.now() + timedelta(days=365))

    @property
    def active(self):
        return timezone.now() < self.date_of_expiry

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if "http" not in self.url:
            self.url = "http://" + self.url
        super(URL, self).save(*args, **kwargs)

    def get_url(self):
        return self.url

    def get_short_url(self):
        return 'http://127.0.0.1:8000/' + self.shortcode

    def get_url_length(self):
        return len(self.url)

    def get_short_url_length(self):
        return len(self.shortcode)

    def get_date_of_creation(self):
        return self.date_of_creation.date()

    def get_date_of_expiry(self):
        return self.date_of_expiry.date()