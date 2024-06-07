from django import forms
from .models import Fornecedor, Contato
from .validators import validar_cnpj

class FornecedorForm(forms.ModelForm):
    cnpj = forms.CharField(
        label='CNPJ',
        widget=forms.TextInput(attrs={'data-mask': "00.000.000/0000-00"})
    )
    razao_social = forms.CharField(label='Razão Social', max_length=100)
    nome_fantasia = forms.CharField(label='Nome Fantasia', max_length=100)
    CEP = forms.CharField(
        label='CEP',
        max_length=9,
        widget=forms.TextInput(attrs={'data-mask': "00000-000"})
    )
    logradouro = forms.CharField(
        label='Logradouro',
        max_length=100,
        required=False
    )
    numero = forms.CharField(
        label='Número',
        max_length=10,
        required=False
    )
    complemento = forms.CharField(
        label='Complemento',
        max_length=100,
        required=False
    )
    cidade = forms.CharField(
        label='Cidade',
        max_length=100,
        required=False
    )
    estado = forms.CharField(
        label='Estado',
        max_length=2,
        required=False
    )
    agencia = forms.CharField(label='Agência', max_length=4)
    banco = forms.CharField(label='Banco', max_length=3)
    conta = forms.CharField(label='Conta', max_length=20,  widget=forms.TextInput(attrs={'data-mask': "00000000-0"}))
    
    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if not validar_cnpj(cnpj):
            raise forms.ValidationError("CNPJ inválido.")
        return cnpj

    
    class Meta:
        model = Fornecedor
        fields = '__all__'
        widgets = {
            'cnpj': forms.TextInput(attrs={'data-mask': "00.000.000/0000-00"}),
            'razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_fantasia': forms.TextInput(attrs={'class': 'form-control'}),
            'CEP': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'agencia': forms.TextInput(attrs={'class': 'form-control'}),
            'banco': forms.TextInput(attrs={'class': 'form-control'}),
            'conta': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['tipo_contato', 'valor_contato']
        widgets = {
            'tipo_contato': forms.Select(attrs={'class': 'form-select'}),
            'valor_contato': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ContatoForm(forms.ModelForm):
    valor_contato = forms.CharField(label='Valor do Contato', widget=forms.TextInput(attrs={'data-mask': "00000-000"}))

    class Meta:
        model = Contato
        fields = ['tipo_contato', 'valor_contato']