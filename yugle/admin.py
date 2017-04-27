from django.contrib import admin

from models import Keyword, SiteInfo


class KeywordInline(admin.TabularInline):
    model = SiteInfo.keywords.through


class KeywordAdmin(admin.ModelAdmin):
    list_display = ['word', 'frequency']
    search_fields = ['word']


class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ['url']
    inlines = [KeywordInline]
    search_fields = ['keyword']


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(SiteInfo, SiteInfoAdmin)
