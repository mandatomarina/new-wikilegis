from django.shortcuts import render, redirect
from django.views import View
from .models import Emenda, Review
from .forms import MutiraoForm
from django.db.models import Count


class MutiraoRnd(View):
    def get(self, request, *args, **kwargs):
        emenda = Emenda.objects.filter(pl__tipo=self.kwargs['tipo'],pl__numero=self.kwargs['numero'],pl__ano=self.kwargs['ano']).annotate(r_count=Count('review'))
        e= emenda.filter(r_count__lte=2).order_by('?').first()
        return redirect('mutirao', tipo=self.kwargs['tipo'], ano=self.kwargs['ano'], numero=self.kwargs['numero'], ano_emenda=e.ano, numero_emenda=e.numero)


class MutiraoView(View):
    def post(self, request, *args, **kwargs):

        form = MutiraoForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.emenda = Emenda.objects.get(pk=form.cleaned_data['emenda_id'])
            obj.save()
            return redirect('mutirao_rnd', tipo=self.kwargs['tipo'], ano=self.kwargs['ano'], numero=self.kwargs['numero'])

    
    def get(self, request, *args, **kwargs):
        emenda = Emenda.objects.filter(pl__tipo=self.kwargs['tipo'],pl__numero=self.kwargs['numero'],pl__ano=self.kwargs['ano']).annotate(r_count=Count('review'))
        
        emenda_revisar = emenda.filter(numero=self.kwargs['numero_emenda'],ano=self.kwargs['ano_emenda']).first()
        emenda_revisada = emenda.filter(r_count__gte=1)
        if not emenda_revisar:
            return render(request, 'mutirao/obrigado.html', { 'tipo' : self.kwargs['tipo'], 'numero' : self.kwargs['numero'], 'ano' : self.kwargs['ano']})
        
        form = MutiraoForm({'emenda_id' : emenda_revisar.id, 'apoiar':False})
        context = {
            'emenda' : emenda_revisar,
            'form' : form,
            'emendas_total' : len(emenda),
            'emendas_analisadas' : len(emenda_revisada)
        }
        return render(request, 'mutirao/emenda.html', context)
