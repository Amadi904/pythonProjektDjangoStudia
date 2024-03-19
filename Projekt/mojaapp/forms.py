from django import forms
from .models import Ustawienia

class UstawieniaForm(forms.ModelForm):
    class Meta:
        model = Ustawienia
        fields = ['kolor', 'tytul']
