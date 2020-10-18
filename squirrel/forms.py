from django.forms import ModelForm
from crispy_forms import helper, layout

from .models import SquirrelSighting


class SightingForm(ModelForm):
    class Meta:
        model = SquirrelSighting
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = helper.FormHelper()
        self.helper.add_input(layout.Submit('save', 'Save'))
