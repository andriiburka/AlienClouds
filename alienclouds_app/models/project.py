from django.db import models


class Project(models.Model):
    project_title = models.CharField(max_length=50)
    project_main_image = models.ImageField(default='', blank=False)
    project_description = models.TextField(blank=False)

    def __str__(self):
        return f'{self.project_title}'
