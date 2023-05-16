from django.forms import ModelForm
from .models import Nota

class createForm(ModelForm):
    class Meta:
        model = Nota
        fields = [ 'nombre', 'contenido']
        