from django import forms
from .models import PracovniPozice
from ckeditor.widgets import CKEditorWidget 

class PracovniPoziceFormular(forms.ModelForm):
    class Meta:
        model = PracovniPozice
        fields = ['nazev', 'mzda', 'popis', 'misto_prace' ,'firma']
    widgets = {
        'popis': CKEditorWidget(),
    } 
