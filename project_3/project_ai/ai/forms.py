from django import forms

from ai.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'  # Use all fields in the form
