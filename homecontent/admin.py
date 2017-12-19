from django.contrib import admin

from homecontent.models import Introduction, \
    DownloadSection, KeyLink, Highlight, \
    Subscriber, NavLink


# class DownloadInline(admin.StackedInline):
#     model = Download


# class DownloadSectionAdmin(admin.ModelAdmin):
#     inlines = [DownloadInline]


admin.site.register(Introduction)
# admin.site.register(DownloadSection, DownloadSectionAdmin)
admin.site.register(DownloadSection)
admin.site.register(KeyLink)
admin.site.register(Highlight)
admin.site.register(Subscriber)
admin.site.register(NavLink)
