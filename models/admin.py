from django.contrib import admin
from .models import *
from django import forms




@admin.register(User)
class JoyLinkUserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'total_score', 'is_active', 'telegram_id', 'is_ban', 'is_superadmin', 'is_admin']
    ordering = ['-create_time']
    list_editable = ['is_ban', 'is_superadmin', 'is_admin']
    search_fields = ['telegram_id']
    list_filter = ['total_score', 'olimpiada']