# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=128)
    user_age = models.IntegerField()
    created_at = models.DateTimeField()
    class Meta:
        db_table = 'user_info'