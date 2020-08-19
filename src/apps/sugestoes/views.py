from django.shortcuts import render
from django.db.models import Count
from django.views import View
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from .models import Projeto
from .forms import ProjetoForm

class ObrigadoView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'sugestoes/obrigado.html', context)

class ProjetoCreateView(CreateView):
    template_name = "sugestoes/sugestoes.html"
    model = Projeto
    form_class = ProjetoForm

    success_url = reverse_lazy('obrigado')

class ProjetoList(View):
    def get(self, request, *args, **kwargs):
        projetos = Projeto.objects.all().annotate(apoios=Count('apoiador'))

        context = { 'projetos' : projetos }
        return render(request, 'sugestoes/lista_projetos.html', context)

class ProjetoView(View):
    def get(self, request, *args, **kwargs):
        
        projeto_id = kwargs['projeto_id']
        print(projeto_id)
        projeto = Projeto.objects.get(id=projeto_id)
        context = { 'projeto' : projeto }
        return render(request, 'sugestoes/projeto.html', context)
    
class ProjetoVote(View):
    def get(self, request, *args, **kwargs):
        return None