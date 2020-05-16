import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=SHORTCODE_MIN):
    shortcode = code_generator(size=size)
    url_model = instance.__class__
    shortcode_exist = url_model.objects.filter(shortcode=shortcode).exists()
    if shortcode_exist:
        return create_shortcode(size=size)
    return shortcode



