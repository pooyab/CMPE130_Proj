from __future__ import unicode_literals

from django.db import models


class Keyword(models.Model):
    word = models.CharField(max_length=100)
    frequency = models.IntegerField()


class SiteInfo(models.Model):
    url = models.URLField(max_length=500)
    keywords = models.ManyToManyField(Keyword)

