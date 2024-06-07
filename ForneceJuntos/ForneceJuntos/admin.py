# ForneceJuntos/admin.py

from django.contrib import admin
from .models import Fornecedor

class FornecedorAdmin(admin.ModelAdmin):
    # Adicione personalizações aqui, como campos a serem exibidos, filtros, etc.
    pass

admin.site.register(Fornecedor, FornecedorAdmin)
