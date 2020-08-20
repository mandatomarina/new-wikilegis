from django.shortcuts import render
from django.db.models import Count
from django.views import View
from django.views.generic.edit import CreateView, FormView
from django.http import HttpResponseRedirect
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

    def form_valid(self, form):
        self.object = form.save()
        # do something with self.object
        self.object.autor = self.request.user
        self.object.apoiador.add(self.request.user)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ProjetoList(View):
    def get(self, request, *args, **kwargs):
        projetos = Projeto.objects.all().annotate(apoios=Count('apoiador'))

        context = { 'projetos' : projetos }
        return render(request, 'sugestoes/lista_projetos.html', context)

class ProjetoView(View):
    def get(self, request, *args, **kwargs):
        
        projeto_id = kwargs['projeto_id']
        projeto = Projeto.objects.get(id=projeto_id)
        context = { 'projeto' : projeto }
        return render(request, 'sugestoes/projeto.html', context)
    
class ProjetoVote(View):
    def get(self, request, *args, **kwargs):
        projeto_id = kwargs['projeto_id']
        vote = kwargs['vote']
        projeto = Projeto.objects.get(id=projeto_id)
        user = request.user
        if vote == 'up':
            projeto.apoiador.add(user)
        elif vote == 'down':
            projeto.apoiador.remove(user)
        return render(request, 'sugestoes/obrigado.html')
