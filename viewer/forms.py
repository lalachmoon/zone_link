from django import forms
from .models import PolygonModel

class PolygonForm(forms.ModelForm):
    class Meta:
        model = PolygonModel
        fields = ['name', 'coordinates']
        widgets = {
            'coordinates': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter coordinates as JSON'}),
        }
