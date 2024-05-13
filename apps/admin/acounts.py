from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.model import Account


@admin.register(Account)
class AccountModelAdmin(ModelAdmin):
    pass
