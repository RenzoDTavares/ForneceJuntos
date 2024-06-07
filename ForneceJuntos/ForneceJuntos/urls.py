"""ForneceJuntos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# nome_do_app/urls.py
# ForneceJuntos/urls.py

# ForneceJuntos/urls.py

from django.urls import path, include, re_path
from django.views.generic import RedirectView
from .views import incluir_fornecedor, home, pesquisar_fornecedor, buscar_contatos, detalhes_fornecedor, editar_fornecedor, remover_fornecedor, relatorios

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('incluir/', incluir_fornecedor, name='incluir_fornecedor'),
    path('pesquisar/', pesquisar_fornecedor, name='pesquisar_fornecedor'),
    path('caminho/para/buscar/contatos/', buscar_contatos, name='buscar_contatos'),
    path('fornecedor/<str:cnpj>/', detalhes_fornecedor, name='detalhes_fornecedor'),
    path('fornecedor/editar/<str:cnpj>/', editar_fornecedor, name='editar_fornecedor'),
    path('fornecedor/remover/<str:cnpj>/', remover_fornecedor, name='remover_fornecedor'),
    path('accounts/', include('django.contrib.auth.urls')),  # Adiciona URLs de autenticação
    path('relatorios/', relatorios, name='relatorios'),
]