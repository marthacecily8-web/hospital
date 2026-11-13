from django.forms import forms, widgets

from patients.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

        widgets = {
            'patient_id': widgets.TextInput(attrs={'class': 'form-control'}),
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'age': widgets.NumberInput(attrs={'class': 'form-control'}),
            'gender': widgets.Select(attrs={'class': 'form-control'}),
            'address': widgets.Textarea(attrs={'class': 'form-control'}),
            'phone_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'medical_history': widgets.Textarea(attrs={'class': 'form-control'}),
        }


        