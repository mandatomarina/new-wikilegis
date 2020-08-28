from django import forms
from .models import Review

TRUE_FALSE_CHOICES = (
    (True, 'Sim'),
    (False, 'Não')
)

class MutiraoForm(forms.ModelForm):
    apoiar = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label="Devemos apoiar essa emenda?", 
        initial=False, widget=forms.Select(), required=True)
    justificativa = forms.CharField(required=False, label="Justificativa (300 caracteres):", widget=forms.Textarea(attrs={'autofocus': 'autofocus', 'maxlength' : 300}))
    
    class Meta:
        model = Review
        fields = ['apoiar', 'justificativa']
     