from django import forms
from .models import LostFoundItem

class LostFoundItemForm(forms.ModelForm):
    class Meta:
        model = LostFoundItem
        fields = ['title', 'description', 'location', 'status']
