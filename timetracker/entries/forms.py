from django import forms
from django.utils import timezone

from .models import Project, Client, Entry


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ()

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ()

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ()
        labels = {
            'start': 'Start Time',
            'stop': 'Stop Time',
        }

    def clean_start(self):
        """
        Validation for start field
        """
        start = self.cleaned_data['start']
        if start >= timezone.now():
            raise forms.ValidationError('Start time must be in the past')

        # Must return the value, regardless of whether we changed it or not
        return start

    def clean(self):
        """
        This method handles the validation of the form overall and is useful for
        handling scenarios like when a field relies on another field
        """
        # Call parent's clean method to ensure any validation logic in parent class
        # is preserved
        cleaned_data = super(EntryForm, self).clean()

        # Get the start and end values from the cleaned_data dictionary, or None
        # if the dictionary keys are missing
        start = cleaned_data.get('start', None)
        end = cleaned_data.get('end', None)

        if end and start and (end < start):
            raise forms.ValidationError('End time must come after start time')
        # No need to return anything (Django 1.7 and above)
