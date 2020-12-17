from django.forms import ModelForm
from alienclouds_app.models import Project, ShopItem


class UploadProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class UploadItemForm(ModelForm):
    class Meta:
        model = ShopItem
        fields = '__all__'
