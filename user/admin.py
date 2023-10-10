from django.contrib import admin
from jalali_date import datetime2jalali

from .models import User
from jalali_date.admin import ModelAdminJalaliMixin


def created_time_fa(obj):
    return datetime2jalali(obj.created_time).strftime('%Y/%m/%d - %H:%M:%S')


@admin.register(User)
class UserAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('id', 'username', 'firstname', 'lastname', 'is_active', created_time_fa)
    search_fields = ('username', 'firstname', 'lastname')
    list_filter = ['created_time']
    # not show in admin site
    exclude = ('password', 'groups', 'is_staff', 'is_superuser', 'apiToken', 'code', 'last_login', 'introducer')
