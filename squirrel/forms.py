from django.forms import ModelForm
from .models import SquirrelSighting


class AddSightingForm(ModelForm):
    class Meta:
        model = SquirrelSighting
        fields = '__all__'
