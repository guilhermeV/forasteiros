from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import User
from destinies.models import Destiny

class EventManager(models.Manager):
    def active(self, *args, **kwargs):
        # Event.objects.all() = super(EventManager, self).all()
        return super(EventManager, self).filter(publish__lte=timezone.now())

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE)
    initial_date = models.DateField(auto_now=False, auto_now_add=False)
    final_date = models.DateField(auto_now=False, auto_now_add=False)
    details = models.TextField()
    payment_options = models.CharField(max_length=120)
    meeting_point = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = EventManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp", "-updated"]

    @property
    def get_user(self):
        instance = self
        user = settings.AUTH_USER_MODEL.objects.get_for_model(instance.__class__)
        return user









