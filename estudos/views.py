from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Disciplina, Avaliacao, MaterialEstudo


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
