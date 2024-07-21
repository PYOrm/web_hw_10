from django.forms import models

from .models import Tag


class TagForm(models.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
