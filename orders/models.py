from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from events.models import Event

class OrderManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(OrderManager, self).filter(publish__lte=timezone.now())

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    payment_form = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    details = models.TextField()
    
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = OrderManager()

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









