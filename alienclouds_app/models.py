from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='images', null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        # shows the object title
        return f'{self.id} --- {self.title}'

