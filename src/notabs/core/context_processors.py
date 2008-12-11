from django.conf import settings

def site_config(request):
    return {
        'SITE_URL': settings.SITE_URL,
        'MEDIA_URL': settings.MEDIA_URL,
        'DEBUG': settings.TEMPLATE_DEBUG,
    }
