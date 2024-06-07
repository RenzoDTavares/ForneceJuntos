# nome_do_app/views.py

from django.shortcuts import render, redirect
from .forms import FornecedorForm, ContatoForm
from .models import Fornecedor, Contato
from django.forms import formset_factory
from .models import Fornecedor
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse 

from django.shortcuts import render, redirect
from .forms import FornecedorForm
from .models import Fornecedor, Contato
import json
import re


import json

def incluir_fornecedor(request):
    if request.method == 'POST':
        fornecedor_form = FornecedorForm(request.POST)
        print(request.POST)
        
        if fornecedor_form.is_valid():
            cnpj_unmasked = request.POST['cnpj'].replace('.', '').replace('/', '').replace('-', '')

            if Fornecedor.objects.filter(cnpj=cnpj_unmasked).exists():
                print("DEBUG: CNPJ duplicado detectado")
                
                contatos_json = request.POST.get('contatosExistentesJSON', '{}')
                contatos = json.loads(contatos_json)

                for key, value in request.POST.items():
                    if key.startswith('tipo_contato_'):
                        contato_numero = key.split('_')[2]
                        if contato_numero not in contatos:
                            contatos[contato_numero] = {}
                        # Converte o número para o tipo correspondente
                        tipo = int(value)
                        if tipo == 1:
                            tipo_contato = 'Telefone'
                        elif tipo == 2:
                            tipo_contato = 'Celular'
                        elif tipo == 3:
                            tipo_contato = 'Email'
                        else:
                            tipo_contato = 'Desconhecido'
                        contatos[contato_numero]['tipo'] = tipo_contato
                    elif key.startswith('valor_contato_'):
                        contato_numero = key.split('_')[2]
                        contatos[contato_numero]['valor'] = value

                return render(request, 'incluir_fornecedor.html', {
                    'fornecedor_form': fornecedor_form,
                    'contatosExistentesJSON': contatos_json,
                    'error_message': 'Um fornecedor com este CNPJ já foi adicionado.',
                    'contatos_nao_salvos': contatos
                })
            else:
                fornecedor = fornecedor_form.save(commit=False)
                fornecedor.cnpj = cnpj_unmasked
                fornecedor.save()
                
                contatos_json = request.POST.get('contatosExistentesJSON', '{}')
                contatos = json.loads(contatos_json)
                print("1 ---")
                print(contatos)
                
                contatos_json = request.POST.get('contatosExistentesJSON', '[]')
                contatos = json.loads(contatos_json)

                for contato in contatos:
                    tipo_contato = None
                    if contato['tipo'] == 'Telefone':
                        tipo_contato = 1
                    elif contato['tipo'] == 'Celular':
                        tipo_contato = 2
                    elif contato['tipo'] == 'Email':
                        tipo_contato = 3
                    else:
                        tipo_contato = 'Desconhecido'

                    valor_contato = contato['valor'].replace('(', '').replace(')', '').replace(' ', '').replace('-', '')

                    Contato.objects.create(
                        cnpj=fornecedor,
                        tipo_contato=tipo_contato,
                        valor_contato=valor_contato,
                    )

                return redirect('home')

    else:
        fornecedor_form = FornecedorForm()

    return render(request, 'incluir_fornecedor.html', {'fornecedor_form': fornecedor_form})










def buscar_contatos(request):
    cnpj = request.GET.get('cnpj').replace('.', '').replace('/', '').replace('-', '')
    # Encontrar o fornecedor pelo CNPJ
    fornecedor = get_object_or_404(Fornecedor, cnpj=cnpj)
    # Buscar contatos relacionados ao fornecedor
    contatos = Contato.objects.filter(cnpj=fornecedor)
    contatos_data = [
        {
            'tipo_contato': contato.tipo_contato,
            'valor_contato': contato.valor_contato
        } for contato in contatos
    ]
    return JsonResponse(contatos_data, safe=False)  

def detalhes_fornecedor(request, cnpj):
    # Certifique-se de limpar o CNPJ
    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
    fornecedor = get_object_or_404(Fornecedor, cnpj=cnpj)
    return render(request, 'detalhes_fornecedor.html', {'fornecedor': fornecedor})


# ForneceJuntos/views.py

def home(request):
    # Consulta o banco de dados para obter todos os fornecedores
    fornecedores = Fornecedor.objects.all()

    # Parâmetros de pesquisa
    cnpj = request.GET.get('cnpj')
    razao_social = request.GET.get('razao_social')
    cidade = request.GET.get('cidade')
    tipo_bebida = request.GET.get('tipo_bebida')

    # Remover caracteres não numéricos do CNPJ
    if cnpj:
        cnpj = re.sub(r'\D', '', cnpj)

    # Lista para armazenar os itens formatados
    itens_formatados = []

    # Se nenhum critério de pesquisa for fornecido, retornar todos os fornecedores
    if not (cnpj or razao_social or cidade or tipo_bebida):
        itens_formatados = [{'cnpj': formatar_cnpj(fornecedor.cnpj), 'razao_social': fornecedor.razao_social,
                             'cidade': fornecedor.cidade, 'tipo_bebida': fornecedor.tipo_bebida}
                            for fornecedor in fornecedores]

    # Se pelo menos um critério de pesquisa for fornecido, filtrar os fornecedores
    else:
        # Filtrar fornecedores de acordo com os critérios fornecidos
        query_params = {}
        if cnpj:
            query_params['cnpj__icontains'] = cnpj
        if razao_social:
            query_params['razao_social__icontains'] = razao_social
        if cidade:
            query_params['cidade__icontains'] = cidade
        if tipo_bebida:
            query_params['tipo_bebida'] = tipo_bebida

        fornecedores = fornecedores.filter(**query_params)

        # Iterar sobre os fornecedores filtrados e formatar os dados
        itens_formatados = [{'cnpj': formatar_cnpj(fornecedor.cnpj), 'razao_social': fornecedor.razao_social,
                             'cidade': fornecedor.cidade, 'tipo_bebida': fornecedor.tipo_bebida}
                            for fornecedor in fornecedores]

    # Renderizar o template com os dados formatados e o formulário de pesquisa
    return render(request, 'home.html', {'itens': itens_formatados, 'cnpj': cnpj, 'cidade': cidade, 'tipo_bebida': tipo_bebida})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

def formatar_cnpj(cnpj):
    # Verificar se o CNPJ já possui a máscara
    if re.match(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', cnpj):
        return cnpj
    
    # Adicionar a máscara ao CNPJ
    cnpj_formatado = '{}.{}.{}/{}-{}'.format(
        cnpj[:2], cnpj[2:5], cnpj[5:8],
        cnpj[8:12], cnpj[12:]
    )
    return cnpj_formatado

def editar_fornecedor(request, cnpj):
    fornecedor = Fornecedor.objects.get(cnpj=cnpj)
    contatos_existentes = Contato.objects.filter(cnpj=fornecedor)

    if request.method == 'POST':
        fornecedor_form = FornecedorForm(request.POST, instance=fornecedor)
        
        if fornecedor_form.is_valid():
            fornecedor = fornecedor_form.save(commit=False)
            fornecedor.cnpj = fornecedor.cnpj.replace('.', '').replace('/', '').replace('-', '')
            fornecedor.save()

            # Processamento dos contatos
            contatos_json = request.POST.get('contatosExistentesJSON', '[]')
            contatos = json.loads(contatos_json)

            # Limpa os contatos existentes
            contatos_existentes.delete()

            # Adiciona os novos contatos
            for contato in contatos:
                tipo_contato = None
                if contato['tipo'] == 'Telefone':
                    tipo_contato = 1
                elif contato['tipo'] == 'Celular':
                    tipo_contato = 2
                elif contato['tipo'] == 'Email':
                    tipo_contato = 3
                else:
                    tipo_contato = 'Desconhecido'

                valor_contato = contato['valor'].replace('(', '').replace(')', '').replace(' ', '').replace('-', '')

                Contato.objects.create(
                    cnpj=fornecedor,
                    tipo_contato=tipo_contato,
                    valor_contato=valor_contato,
                )

            return redirect('home')

    else:
        fornecedor_form = FornecedorForm(instance=fornecedor)

    contatos_nao_salvos = []
    for contato in contatos_existentes:
        tipo_contato = None
        if contato.tipo_contato == 1:
            tipo_contato = 'Telefone'
        elif contato.tipo_contato == 2:
            tipo_contato = 'Celular'
        elif contato.tipo_contato == 3:
            tipo_contato = 'Email'
        else:
            tipo_contato = 'Desconhecido'

        valor_contato = contato.valor_contato
        if contato.tipo_contato in [1, 2]:  # Adiciona a máscara se for telefone ou celular
            valor_contato = formatar_contato(valor_contato, contato.tipo_contato)

        contatos_nao_salvos.append({'tipo': tipo_contato, 'valor': valor_contato})

    contatos_nao_salvos_json = json.dumps(contatos_nao_salvos)

    return render(request, 'editar_fornecedor.html', {
        'fornecedor_form': fornecedor_form,
        'contatosExistentesJSON': contatos_nao_salvos_json,
        'contatos_nao_salvos': contatos_nao_salvos,
    })

def formatar_contato(valor, tipo_contato):
    if tipo_contato == 1:  # Telefone
        return f"({valor[:2]}) {valor[2:6]}-{valor[6:]}"
    elif tipo_contato == 2:  # Celular
        return f"({valor[:2]}) {valor[2:7]}-{valor[7:]}"
    return valor

from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

def remover_fornecedor(request, cnpj):
    if request.method == "POST":
        # Verifica se o fornecedor com o CNPJ fornecido existe
        try:
            fornecedor = Fornecedor.objects.get(cnpj=cnpj)

            # Exclui os contatos relacionados ao fornecedor
            Contato.objects.filter(cnpj=fornecedor).delete()

            # Remove o fornecedor do banco de dados
            fornecedor.delete()  

            # Redireciona para a página inicial
            return HttpResponseRedirect(reverse('home'))
        except Fornecedor.DoesNotExist:
            return JsonResponse({'error': 'Fornecedor não encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

def relatorios(request):
    tipo_bebida = request.GET.get('tipo_bebida')
    regiao = request.GET.get('regiao')
    
    # Filtrar os fornecedores com base nos parâmetros fornecidos
    fornecedores = Fornecedor.objects.all()
    if tipo_bebida:
        fornecedores = fornecedores.filter(tipo_bebida=tipo_bebida)
    if regiao:
        fornecedores = fornecedores.filter(regiao=regiao)
    
    # Outras operações para gerar o relatório...
    
    return render(request, 'relatorios.html', {'fornecedores': fornecedores})


from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.text import get_valid_filename

def pesquisar_fornecedor(request):
    cnpj_raw = request.GET.get('cnpj', '')
    razao_social = request.GET.get('razao_social')

    # Remove a máscara do CNPJ
    cnpj = cnpj_raw.replace(".", "").replace("/", "").replace("-", "")

    if cnpj or razao_social:
        # Se pelo menos um dos campos de pesquisa estiver preenchido,
        # filtramos os fornecedores de acordo com os critérios fornecidos
        fornecedores = Fornecedor.objects.filter(
            cnpj__contains=cnpj, razao_social__icontains=razao_social
        )
    else:
        # Se nenhum critério de pesquisa for especificado, retornamos todos os fornecedores
        fornecedores = Fornecedor.objects.all()

    # Lista para armazenar os itens formatados
    itens_formatados = []

    # Itera sobre os fornecedores e formata os dados
    for fornecedor in fornecedores:
        # Adiciona os dados formatados à lista de itens formatados
        itens_formatados.append({
            'cnpj': fornecedor.cnpj,  # Mantenha o CNPJ sem máscara
            'razao_social': fornecedor.razao_social,
            'cidade': fornecedor.cidade,
        })

    # Renderiza o template com os dados formatados
    html_resultados = render_to_string('pesquisar.html', {'itens': itens_formatados})

    # Retornar a página HTML renderizada
    return HttpResponse(html_resultados)
