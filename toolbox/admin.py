from django.contrib import admin
from toolbox.models import Format, ToolList, Category, Tool


class ToolInline(admin.TabularInline):
    model = Tool


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ToolInline]


admin.site.register(Format)
admin.site.register(ToolList)
admin.site.register(Category, CategoryAdmin)
