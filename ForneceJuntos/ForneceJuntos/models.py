from django.db import models
from .validators import validar_cnpj

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=18, primary_key=True,  blank=True)
    razao_social = models.CharField(max_length=100, blank=True)
    nome_fantasia = models.CharField(max_length=100, blank=True)
    CEP = models.CharField(max_length=9, null=True)  # Permitindo valores nulos para o campo CEP
    logradouro = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    agencia = models.CharField(max_length=4, blank=True)
    banco = models.CharField(max_length=3, blank=True)
    conta = models.CharField(max_length=20, blank=True) 
    # Adicione o campo tipo_bebida
    TIPO_BEBIDA_CHOICES = [
        ('Destilados', 'Destilados'),
        ('Vinhos', 'Vinhos'),
        ('Cervejas', 'Cervejas'),
        ('Espumantes', 'Espumantes'),
        ('Licores', 'Licores'),
        ('Refrescos', 'Refrescos'),
        ('Água', 'Água'),
        # Adicione mais opções conforme necessário
    ]
    tipo_bebida = models.CharField(max_length=20, choices=TIPO_BEBIDA_CHOICES,  default='Destilados')
    
    
    
    
class Contato(models.Model):
    TIPO_CONTATO_CHOICES = [
        (1, 'Telefone'),
        (2, 'Celular'),
        (3, 'Email'),
    ]
    cnpj = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, db_column='cnpj_id')
    tipo_contato = models.IntegerField(choices=TIPO_CONTATO_CHOICES)
    valor_contato = models.CharField(max_length=255)

    
    
