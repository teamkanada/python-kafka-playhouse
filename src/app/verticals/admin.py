from django.contrib import admin

from .models import Vertical


class VerticalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vertical, VerticalAdmin)
