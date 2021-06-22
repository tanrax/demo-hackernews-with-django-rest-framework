from django.contrib import admin
from app.api.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('votes',)
    list_display = ('title', 'url')

