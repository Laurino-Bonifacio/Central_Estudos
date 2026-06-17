from django import forms
from .models import Disciplina, Avaliacao

NIVEL_CHOICES = [(i, str(i)) for i in range(1, 6)]


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'cor_identificacao', 'dificuldade', 'quantidade_conteudo', 'peso']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Matemática'}),
            'cor_identificacao': forms.TextInput(attrs={'class': 'form-control form-control-color', 'type': 'color'}),
            'dificuldade': forms.Select(choices=NIVEL_CHOICES, attrs={'class': 'form-select'}),
            'quantidade_conteudo': forms.Select(choices=NIVEL_CHOICES, attrs={'class': 'form-select'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0.1', 'max': '10'}),
        }
        labels = {
            'nome': 'Nome da Matéria',
            'cor_identificacao': 'Cor de Identificação',
            'dificuldade': 'Dificuldade (1 = fácil, 5 = muito difícil)',
            'quantidade_conteudo': 'Volume de Conteúdo (1 = pouco, 5 = muito)',
            'peso': 'Peso / Prioridade',
        }


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        exclude = ['usuario']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Prova de Cálculo 1'}),
            'data_prova': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_prazo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Tópicos, capítulos, dicas...'}),
            'estudo_concluido': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'disciplina': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'titulo': 'Título da Avaliação',
            'data_prova': 'Data da Prova',
            'data_prazo': 'Prazo de Estudo',
            'conteudo': 'Conteúdo / Observações',
            'estudo_concluido': 'Estudo já concluído?',
            'disciplina': 'Matéria',
        }

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        if usuario:
            self.fields['disciplina'].queryset = Disciplina.objects.filter(usuario=usuario)
        else:
            self.fields['disciplina'].queryset = Disciplina.objects.none()
        self.fields['disciplina'].required = False
        self.fields['data_prazo'].required = False
        self.fields['conteudo'].required = False
