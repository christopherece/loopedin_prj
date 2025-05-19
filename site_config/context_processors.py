from .models import SiteConfig

def site_config(request):
    try:
        config = SiteConfig.objects.get()
    except SiteConfig.DoesNotExist:
        # Create default config if none exist
        config = SiteConfig.objects.create()
    return {'site_config': config}
