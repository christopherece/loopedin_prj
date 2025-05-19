from django.db import models
from django.contrib.auth.models import User

class SiteConfig(models.Model):
    logo = models.ImageField(upload_to='site_config/', null=True, blank=True)
    logo_name = models.CharField(max_length=50, default='LoopedIn')
    favicon = models.ImageField(upload_to='site_config/', null=True, blank=True)
    
    def __str__(self):
        return "Site Configuration"
    
    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if self.pk is None:
            try:
                existing = SiteConfig.objects.get()
                self.pk = existing.pk
            except SiteConfig.DoesNotExist:
                pass
        super().save(*args, **kwargs)
