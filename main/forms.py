from django.forms import NumberInput, ModelForm, TextInput

from .models import Arithmetic, Conversion


class ArithmeticOperationForm(ModelForm):
    class Meta:
        model = Arithmetic
        fields = ['number1', 'number2','operation']
        widgets = {
            'number1': NumberInput(),
            'number2': NumberInput(),
            'operation': TextInput()
        }

class ConversionForm(ModelForm):
    class Meta:
        model = Conversion
        fields = ['kilometers']
        widgets = {'kilometers': NumberInput()}
