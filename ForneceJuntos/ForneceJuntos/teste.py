from graphviz import Digraph

# Criação do grafo
dot = Digraph()

# Definição da classe Fornecedor
dot.node('Fornecedor', '''Fornecedor
+-----------------+
| - cnpj: String  |
| - razao_social: String |
| - nome_fantasia: String |
| - cep: String   |
| - logradouro: String |
| - numero: int   |
| - complemento: String |
| - cidade: String|
| - estado: String|
| - agencia: String |
| - banco: String |
| - conta: String |
| - tipo_bebida: String |
+-----------------+
| +getContatos(): List<Contato> |
+-----------------+''')

# Definição da classe Contato
dot.node('Contato', '''Contato
+----------------+
| - id: int      |
| - tipo: String |
| - valor: String|
+----------------+
| +getFornecedor(): Fornecedor |
+----------------+''')

# Definição do relacionamento
dot.edge('Fornecedor', 'Contato', constraint='true', arrowhead='crow', label='1..*')

# Renderização do diagrama para um arquivo
diagram_path = 'diagrama_classes.png'
dot.render(diagram_path, format='png', cleanup=True)

print(f"Diagrama salvo em: {diagram_path}")
