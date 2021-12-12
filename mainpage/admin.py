from django.contrib import admin
from .models import NewsModels

class NewsAdmin(admin.ModelAdmin):
    list_display = ('NewsID', 'NewsDate', 'NewsTitle')
    list_display_links = ('NewsID', 'NewsDate', 'NewsTitle')
    search_fields = ('NewsDate', 'NewsTitle')


admin.site.register(NewsModels, NewsAdmin)
