from .models import Lead
from django.forms import ModelForm

class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['mail',]