from django.core.management.base import BaseCommand, CommandError
from shortener.models import URL
from django.utils import timezone

class Command(BaseCommand):
    help = 'Deletes all the expired links.'

    def handle(self, *args, **options):
        URL.objects.filter(date_of_expiry__lte= timezone.now()).delete()