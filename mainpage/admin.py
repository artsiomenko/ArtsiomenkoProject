from django.contrib import admin
from .models import NewsModels, AdModels


class NewsAdmin(admin.ModelAdmin):
    list_display = ('NewsID', 'NewsDate', 'NewsTitle')
    list_display_links = ('NewsID', 'NewsDate', 'NewsTitle')
    search_fields = ('NewsDate', 'NewsTitle')


admin.site.register(NewsModels, NewsAdmin)


class AdAdmin(admin.ModelAdmin):
    list_display = ('AdID', 'AdDate', 'AdTitle')
    list_display_links = ('AdID', 'AdDate', 'AdTitle')
    search_fields = ('AdDate', 'AdTitle')

admin.site.register(AdModels, AdAdmin)

