from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
user = models.ForeignKey(User, null=True, blank=True, default=None)
uuid = models.CharField(max_length=50, unique=True)
uuid2 = models.CharField(max_length=50)
name = models.CharField(max_length=255)
description = models.TextField(max_length=255)
keywords = models.TextField(null=True)
slug = models.SlugField(max_length=250, null=True, unique=True, default=None)
price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
duration = models.IntegerField(null=True)

STATUS_CHOICES = (
('A', 'Active'),
('P', 'Processing'),
('D', 'Disabled')
)

status = models.CharField(max_length=1, choices=STATUS_CHOICES)
featured = models.NullBooleanField()
created = models.DateTimeField(auto_now_add=True)
modified = models.DateTimeField(auto_now=True)
ip_created = models.IPAddressField(null=True)

def __unicode__(self):
return self.name
