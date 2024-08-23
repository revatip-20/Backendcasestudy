from django import forms
from customers.models import ServiceRequest

class UpdateRequestStatusForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean_status(self):
        status = self.cleaned_data.get('status')
        if not status:
            raise forms.ValidationError("Status must be selected.")
        return status
