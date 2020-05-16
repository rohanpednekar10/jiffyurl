from django.core.management.base import BaseCommand
from shortener.models import URL

class Command(BaseCommand):
    help = 'Deletes all the existing links.'

    def handle(self, *args, **options):
        URL.objects.all().delete()