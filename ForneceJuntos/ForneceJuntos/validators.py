# nome_do_app/validators.py

import re

def validar_cnpj(cnpj):
    # Aqui você pode implementar a lógica de validação do CNPJ
    # Por exemplo, usar uma expressão regular para verificar o formato
    # e calcular os dígitos verificadores
    # Este é apenas um exemplo de verificação de formato
    if not re.match(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', cnpj):
        return False
    # Adicione aqui a lógica de cálculo dos dígitos verificadores
    # ...
    return True
