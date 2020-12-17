from django.contrib import admin

from alienclouds_app.models import Project, ShopItem


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image',)
    list_filter = ('id', 'title', 'image',)


class ShopItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image',)
    list_filter = ('id', 'name', 'image',)


admin.site.register(Project, ProjectsAdmin)
admin.site.register(ShopItem, ShopItemsAdmin)
