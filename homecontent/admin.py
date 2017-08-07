from django.contrib import admin

from homecontent.models import Introduction, \
    DownloadSection, Download, KeyLink


class DownloadInline(admin.StackedInline):
    model = Download


class DownloadSectionAdmin(admin.ModelAdmin):
    inlines = [DownloadInline]


admin.site.register(Introduction)
admin.site.register(DownloadSection, DownloadSectionAdmin)
admin.site.register(KeyLink)
