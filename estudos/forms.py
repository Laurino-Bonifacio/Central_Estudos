from django import forms
from .models import Disciplina, Avaliacao


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        exclude = ['usuario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Matemática'}),
            'cor_identificacao': forms.TextInput(attrs={'class': 'form-control form-control-color', 'type': 'color'}),
        }
        labels = {
            'nome': 'Nome da Matéria',
            'cor_identificacao': 'Cor de Identificação',
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
