from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:

        model = Application

        fields = [
            "company",
            "position",
            "status",
            "application_date",
            "notes",
        ]

        widgets = {
            "application_date": forms.DateInput(attrs={"type": "date"}),
        }