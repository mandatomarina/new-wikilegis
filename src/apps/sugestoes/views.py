from django.shortcuts import render
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

