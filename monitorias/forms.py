from django import forms
from monitorias.models import Monitoria, Inscricao


class MonitoriaModelForm(forms.ModelForm):
    
    class Meta:
        model = Monitoria

        exclude = ['owner']   

        widgets = {

            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Excel Avançado'
                }
            ),

            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Descreva a monitoria'
                }
            ),

            'categoria': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'beneficio': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'data': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'vagas': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': '1',
                    'placeholder': 'Número de vagas'
                }
            ),
        }


class InscricaoModelForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['nome', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seu nome completo'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'email@exemplo.com'
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '(71) 99999-9999'
                }
            ),
        }

    def __init__(self, *args, monitoria=None, **kwargs):
        self.monitoria = monitoria
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.monitoria and Inscricao.objects.filter(monitoria=self.monitoria, email__iexact=email).exists():
            raise forms.ValidationError('Este email já está inscrito nesta monitoria.')
        return email
