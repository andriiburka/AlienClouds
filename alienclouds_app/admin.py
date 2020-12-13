from django.contrib import admin

from alienclouds_app.models import Project


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', )
    list_filter = ('title', )


admin.site.register(Project, ProjectsAdmin)
