from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Disciplina, Avaliacao, MaterialEstudo
from .forms import DisciplinaForm, AvaliacaoForm


@login_required
def dashboard(request):
    hoje = timezone.now().date()
    disciplinas = Disciplina.objects.filter(usuario=request.user)
    proximas_avaliacoes = (
        Avaliacao.objects
        .filter(usuario=request.user, estudo_concluido=False, data_prova__gte=hoje)
        .order_by('data_prova')[:5]
    )
    pendentes_count = Avaliacao.objects.filter(
        usuario=request.user,
        estudo_concluido=False
    ).count()
    materiais_count = MaterialEstudo.objects.filter(
        disciplina__usuario=request.user
    ).count()

    context = {
        'disciplinas': disciplinas,
        'proximas_avaliacoes': proximas_avaliacoes,
        'pendentes_count': pendentes_count,
        'materiais_count': materiais_count,
        'hoje': hoje,
    }
    return render(request, 'estudos/dashboard.html', context)


@login_required
def adicionar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.usuario = request.user
            disciplina.save()
            return redirect('dashboard')
    else:
        form = DisciplinaForm()
    return render(request, 'estudos/adicionar_disciplina.html', {'form': form})


@login_required
def adicionar_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, usuario=request.user)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.save()
            return redirect('dashboard')
    else:
        form = AvaliacaoForm(usuario=request.user)
    return render(request, 'estudos/adicionar_avaliacao.html', {'form': form})
