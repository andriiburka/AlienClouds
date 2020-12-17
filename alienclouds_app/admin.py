from django.contrib import admin

from alienclouds_app.models import Project, ShopItem


#   █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗    ███████╗██╗██╗  ████████╗███████╗██████╗ ███████╗
#  ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║    ██╔════╝██║██║  ╚══██╔══╝██╔════╝██╔══██╗██╔════╝
#  ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║    █████╗  ██║██║     ██║   █████╗  ██████╔╝███████╗
#  ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║    ██╔══╝  ██║██║     ██║   ██╔══╝  ██╔══██╗╚════██║
#  ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║    ██║     ██║███████╗██║   ███████╗██║  ██║███████║________________________
#  ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝
#
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'id', )
    list_filter = ('title', 'image', )


class ShopItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'id',)
    list_filter = ('name', 'price', 'image', )


admin.site.register(Project, ProjectsAdmin)
admin.site.register(ShopItem, ShopItemsAdmin)
