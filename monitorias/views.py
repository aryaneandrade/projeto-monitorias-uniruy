from monitorias.models import Monitoria, Categoria, Inscricao
from monitorias.forms import MonitoriaModelForm, InscricaoModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Count

class MonitoriaListView(ListView):
    model = Monitoria
    template_name = 'monitorias.html'
    context_object_name = 'monitorias'

    def get_queryset(self):
        monitorias = (
                super()
                .get_queryset()
                .annotate(total_inscricoes=Count('inscricoes'))
                .order_by('titulo')
        )

        # busca 
        busca = self.request.GET.get('search')

        # categoria 
        categoria_id = self.request.GET.get('categoria')

        if busca:
            monitorias = monitorias.filter(titulo__icontains=busca)
        
        if categoria_id:
            monitorias = monitorias.filter(categoria_id=categoria_id)
        
        return monitorias
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


class NovaMonitoriaCreateView(LoginRequiredMixin, CreateView):
    model = Monitoria
    form_class = MonitoriaModelForm
    template_name = 'criar_monitoria.html'
    success_url = reverse_lazy('painel')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Monitoria criada com sucesso!')
        return response
    

class MonitoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Monitoria
    form_class = MonitoriaModelForm
    template_name = 'editar_monitoria.html'
    success_url = reverse_lazy('painel')
    login_url = 'login'

    def get_queryset(self):
        return Monitoria.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Monitoria atualizada com sucesso!')
        return response
    def form_valid(self, form):
        print("DATA:", form.cleaned_data.get("data"))
        return super().form_valid(form)


class MonitoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Monitoria
    template_name = 'excluir_monitoria.html'
    success_url = reverse_lazy('painel')
    login_url = 'login'
    
    def get_queryset(self):
        return Monitoria.objects.filter(owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, 'Monitoria excluída com sucesso!')
        return response


class MonitoriaInscricaoView(View):
    template_name = 'inscricao.html'
    form_class = InscricaoModelForm

    def get(self, request, pk):
        monitoria = get_object_or_404(Monitoria, pk=pk)
        form = self.form_class(monitoria=monitoria)
        return render(request, self.template_name, {
            'monitoria': monitoria,
            'form': form,
        })

    def post(self, request, pk):
        monitoria = get_object_or_404(Monitoria, pk=pk)

        if request.user.is_authenticated and monitoria.owner == request.user:
            messages.error(request, 'Você não pode inscrever-se em sua própria monitoria.')
            return redirect('monitorias_list')

        if monitoria.monitoria_lotada:
            return render(request, self.template_name, {
                        'monitoria': monitoria,
                        'form': self.form_class(monitoria=monitoria),
                        'erro': 'Esta monitoria já está lotada.'
                    })
        
        form = self.form_class(request.POST, monitoria=monitoria)

        if form.is_valid():
            inscricao = form.save(commit=False)
            inscricao.monitoria = monitoria
            inscricao.save()
            messages.success(request, 'Inscrição realizada com sucesso!')
            return redirect('monitorias_list')

        return render(request, self.template_name, {
            'monitoria': monitoria,
            'form': form,
        })


class MonitoriaInscritoListView(LoginRequiredMixin, ListView):
    model = Inscricao
    template_name = 'inscritos_monitoria.html'
    context_object_name = 'inscritos'
    login_url = 'login'

    def get_queryset(self):
        self.monitoria = get_object_or_404(Monitoria, pk=self.kwargs['pk'], owner=self.request.user)
        return self.monitoria.inscricoes.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['monitoria'] = self.monitoria
        return context


@login_required(login_url='login')
def painel_view(request):
    return render(request, 'painel_monitor.html')
