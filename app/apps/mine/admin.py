from django.contrib import admin

from apps.mine.models import Text


@admin.register(Text)
class BasicAdmin(admin.ModelAdmin):
    pass
