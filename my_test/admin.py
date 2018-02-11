# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
    fields = ['user_name', 'user_age','created_at']
    list_display = ('user_name', 'user_age','created_at')
    list_filter = ['user_name','user_age']
admin.site.register(User,UserAdmin)