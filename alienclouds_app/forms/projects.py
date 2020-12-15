from django.forms import ModelForm

from alienclouds_app.models import Project


class UploadForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
