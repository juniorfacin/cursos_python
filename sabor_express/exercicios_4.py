# Como acessar o preco e alterar o valor
livro = {
    'titulo': 'Aprendendo Python',
    'autor': 'Fabrício Silva',
    'ISBN': '12345',
    'preco': 59.90,
    'em_estoque': True
}

print(livro['preco'])

# Primeira forma
livro ['preco'] = 69.90
print(livro['preco'])

# Segunda forma: O método update() é outra forma válida de atualizar o valor de uma chave em um dicionário em Python
livro.update({'preco': 79.90})
print(livro['preco'])

credenciais_clientes = {
    'alice123': {'username': 'alice123', 'password': 'alic3P@ssw0rd', 'status': 'active'},
    'bob456': {'username': 'bob456', 'password': 'b0bP@ssword!', 'status': 'inactive'},
    'charlie789': {'username': 'charlie789', 'password': 'Ch@rlieP@ss9', 'status': 'active'}
}

# Este código verifica corretamente o status do usuário 'bob456' utilizando um operador ternário, onde se o status for 'inactive', a variável alerta recebe 'Enviar alerta!', caso contrário, recebe 'Sem alerta'.
alerta = 'Enviar alerta!' if credenciais_clientes['bob456']['status'] == 'inactive' else 'Sem alerta'

print(alerta)

# 1- Informações pessoais
inf_pessoais = {'nome': 'Junior', 'Idade': 30, 'Cidade': 'São Paulo-SP'}

print(type(inf_pessoais))

# 2- Manipular o Dicionário
## Alterar um elemento
inf_pessoais['Idade'] = 40
print(inf_pessoais['Idade'])
## Adicionar um elemento
inf_pessoais['Profissão'] = 'Dev'
print(inf_pessoais)
## Remoção de um Elemento
del inf_pessoais['Idade']
print(inf_pessoais)

# 3 - Criar um dicionário usando de 1 a 5 como chaves, e seus respectivos quadrados.
## Dicionário vazio
meu_dicionario = {}

## Um for para iterar cada "chave" e atribuir o valor de "chave ** 2"(quadrado)
for chave in range(1, 6):
  meu_dicionario[chave] = chave ** 2

print(meu_dicionario)

## Forma compressada de dicionário
numeros_quadrados = {chave: chave ** 2 for chave in range(1, 6)}
print(numeros_quadrados)

# 4- Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
ficha_de_registro = {'Nome': 'Bia', 'Idade': 30, 'Profissao': 'Médica'}
if 'Nome' in ficha_de_registro:
  print('A chave "Nome" foi preenchida!')
else:
  print('Chave "Nome" inexistente. Favor preencher.')

## Com um operador ternário
mensagem = 'A chave "Nome" foi preenchida com sucesso!' if 'Nome' in ficha_de_registro else 'Chave "Nome" inexistente.'
print(mensagem)

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
def contar_palavras(frase):
  # Variável que irá armazenar cada palavra - O split() vai dividir a frase em uma lista de palavras.
  palavras = frase.split()
  qtd_de_palavras = len(palavras)
  return qtd_de_palavras

frase = 'Esse mês de Maio será muito bom!'
print(f'A frase possui {contar_palavras(frase)} palavras.')
