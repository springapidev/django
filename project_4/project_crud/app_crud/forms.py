from django import forms

from app_crud.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

        # Add widgets for specific fields
        widgets = {
            'gender': forms.RadioSelect,
            'hobbies': forms.CheckboxSelectMultiple,
            'country': forms.Select
        }
