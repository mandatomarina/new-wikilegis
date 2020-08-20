from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'tema', 'ementa', 'descritivo', 'justificativa', 'concordo']
        labels = {"concordo" : "Li o manual legislativo antes de submeter esse projeto." }

    
    concordo = forms.CheckboxInput()
    ementa = forms.CharField(widget=forms.Textarea(attrs={'rows':8, 'placeholder' : 'A Ementa é um espécie de "tweet". Uma curta explicação do que trata o projeto.'}))
    descritivo = forms.CharField(widget=forms.Textarea(attrs={'rows':8, 'placeholder' : 'Aqui você vai desenvolver a ideia do projeto. Se você quiser pode fazer já na forma de lei, com artigos, paragrafos e incisos. Mas também pode só detalhar a ideia e o que acha que o projeto precisa conter e depois organizamos isso juntos.'}))
    justificativa = forms.CharField(widget=forms.Textarea(attrs={'rows':8, 'placeholder' : 'A justificativa deve explicar por que esse projeto faz sentido e é importante para o Estado. Traga dados e argumentos que comprovem a necessidade da medida e a eficiência da solução proposta.'}))
