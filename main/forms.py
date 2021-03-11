from django.forms import ModelForm, TextInput, CheckboxInput, NumberInput
from .models import Animal


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'family', 'healthy', 'legs']
        widgets = {
            'name': TextInput(attrs={
                'id': 'post-name',
                'name' : 'post-name',
                'placeholder': 'name',
            }),
            'healthy': CheckboxInput(attrs={
                'id': 'post-healthy',
                'name' : 'post-healthy',
                'placeholder': 'healthy',
            }),
            'legs': NumberInput(attrs={
                'id': 'post-legs',
                'name' : 'post-legs',
                'placeholder': 'legs',
            }),
        }