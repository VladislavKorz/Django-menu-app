from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MenuItemInline]

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'url', 'parent')
    list_filter = ('menu', 'parent',)
    search_fields = ('title', 'menu__name', 'url')

admin.site.register(Menu, MenuAdmin)
# admin.site.register(MenuItem, MenuItemAdmin)
