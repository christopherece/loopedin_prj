from django.contrib import admin
from .models import SiteConfig

@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('logo_name', 'logo', 'favicon')
    fieldsets = (
        (None, {
            'fields': ('logo', 'logo_name', 'favicon')
        }),
    )
    
    def has_add_permission(self, request):
        # Only one instance of SiteConfig should exist
        return not SiteConfig.objects.exists()
