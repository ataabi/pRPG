from django.forms import ModelForm
from .models import BasePersonagem

class FormTeste(ModelForm):
    class Meta:
        model = BasePersonagem
        fields = ('__all__')