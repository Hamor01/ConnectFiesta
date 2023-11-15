from django import forms
from .models import Event


class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'category', 'tags', 'description', 'image']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'datetime-local'}),
            'tags': forms.CheckboxSelectMultiple(),
        }


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'category', 'tags', 'description', 'image']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'datetime-local'}),
            'tags': forms.CheckboxSelectMultiple(),
        }