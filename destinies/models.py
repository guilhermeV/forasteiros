from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone

class DestinyManager(models.Manager):
    def active(self, *args, **kwargs):
        # Destiny.objects.all() = super(DestinyManager, self).all()
        return super(DestinyManager, self).filter(publish__lte=timezone.now())

class Destiny(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    details = models.TextField()
    
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = DestinyManager()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]

    @property
    def get_user(self):
        instance = self
        user = settings.AUTH_USER_MODEL.objects.get_for_model(instance.__class__)
        return user
        
    