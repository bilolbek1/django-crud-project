from django import forms

from crud.models import People


class PeopleCreateForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['name', 'surname', 'city', 'job', 'age']
