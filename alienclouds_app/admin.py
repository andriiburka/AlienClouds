from alienclouds_app.models import Project, ShopItem
from django.contrib import admin
#
#
#  ███████╗██╗██╗  ████████╗███████╗██████╗ ███████╗
#  ██╔════╝██║██║  ╚══██╔══╝██╔════╝██╔══██╗██╔════╝
#  █████╗  ██║██║     ██║   █████╗  ██████╔╝███████╗
#  ██╔══╝  ██║██║     ██║   ██╔══╝  ██╔══██╗╚════██║
#  ██║     ██║███████╗██║   ███████╗██║  ██║███████║____________________________________________________________________
#  ╚═╝     ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝
#   Filters on admin page, the right side


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'id')
    list_filter = ('title', 'image',)


class ShopItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'id',)
    list_filter = ('name', 'price', 'image',)
#
#
#
#
#
#   ██████╗ ██████╗ ███╗   ██╗████████╗███████╗███╗   ██╗████████╗
#  ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔════╝████╗  ██║╚══██╔══╝
#  ██║     ██║   ██║██╔██╗ ██║   ██║   █████╗  ██╔██╗ ██║   ██║
#  ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██║╚██╗██║   ██║
#  ╚██████╗╚██████╔╝██║ ╚████║   ██║   ███████╗██║ ╚████║   ██║_________________________________________________________
#   ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝   ╚═╝
#   Shows Projects and Shop items in admin page


admin.site.register(Project, ProjectsAdmin)
admin.site.register(ShopItem, ShopItemsAdmin)
