import os
def separador_de_codigo():
  print('='* 50)

numeros = []
for i in range(1, 11):
    numeros.append(i)
print('\n', numeros)

separador_de_codigo()

# Lista de 4 nomes:
lista_de_nomes = ['Junior', 'Bia', 'Leo', 'Irani']
for nome in lista_de_nomes:
  print(f'.{nome}')

separador_de_codigo()

# # Solicitação de 4 nomes ao usuário
# # nomes = []
# for nome in range(4):
#   nome = input("Digite um nome: ")
#   nomes.append(nome)
# print('Lista de nomes: ', nomes)

# lista com Ano de Nascimento e Ano Atual
anos = [1994, 2024]
for ano in anos:
  print(f'-{ano}')
  
separador_de_codigo()

# For que percorra todos os elementos da lista
lista_de_compras = ['Banana', 'Arroz', 'Frango', 'Ovo', 'Queijo']
for item in lista_de_compras:
  print(f'.{item}')

separador_de_codigo()

numeros_impares = []

for numero in range(1, 11):
  if numero % 2 != 0:
    numeros_impares.append(numero);

print('Lista de números impáres: ', numeros_impares)

somar_numeros_impares = sum(numeros_impares)
print('Soma dos números ímpares: ', somar_numeros_impares)

separador_de_codigo()

# Imprimir números de 1 a 10 de forma decrescente
numeros_decrescentes= []
for numero in range(10,0,-1):
  numeros_decrescentes.append(numero)

print(numeros_decrescentes)

separador_de_codigo()

# Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
separador_de_codigo()

# Um modo de solucionar essa questão com uma validação de lista vazia é do seguinte modo:
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

separador_de_codigo()

# Testes
import random

try:
    # Solicita um número inteiro ao usuário
    tamanho = int(input("Digite um número inteiro entre 5 e 20: "))
    
    # Verifica se o número está dentro do intervalo desejado
    if 5 <= tamanho <= 20:
      # Cria uma lista com números aleatórios de 1 a 10
      lista = [random.randint(5, 20) for _ in range(tamanho)]
      print("Lista criada:", lista)
      somar_lista = sum(lista)
      print('Total dos elementos da lista: ', somar_lista)
    else:
      print('Error: O número deve estar entre 5 e 20.')

except ValueError as e:
    print("Erro:", e)