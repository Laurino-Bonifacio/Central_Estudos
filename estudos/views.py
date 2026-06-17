from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.utils import timezone
from .models import Disciplina, Avaliacao, MaterialEstudo
from .forms import DisciplinaForm, AvaliacaoForm


@login_required
def dashboard(request):
    hoje = timezone.now().date()
    disciplinas = Disciplina.objects.filter(usuario=request.user)
    todas_avaliacoes = (
        Avaliacao.objects
        .filter(usuario=request.user)
        .order_by('estudo_concluido', 'data_prova')
    )
    pendentes_count = todas_avaliacoes.filter(estudo_concluido=False).count()
    materiais_count = MaterialEstudo.objects.filter(
        disciplina__usuario=request.user
    ).count()

    context = {
        'disciplinas': disciplinas,
        'todas_avaliacoes': todas_avaliacoes,
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


@login_required
def concluir_avaliacao(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk, usuario=request.user)
    avaliacao.estudo_concluido = True
    avaliacao.save()
    return redirect('dashboard')


@login_required
def remover_disciplina(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk, usuario=request.user)
    disciplina.delete()
    return redirect('dashboard')


def cadastrar_usuario(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'estudos/signup.html', {'form': form})
