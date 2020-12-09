
from django.forms import ModelForm

from projects_app.models import Project


class ProjectUploadForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
