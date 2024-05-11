import os
# Verificar se o n. é Par ou Ímpar
numero = int(input('Escolha um número: '))
if numero % 2 == 0:
  print('O número é par.')
else:
  print('O número é ímpar.')

# Classificação de Idade
idade = int(input('Informe a idade para avaliação: '))
if 0 < idade <= 12:
  print('Criança: 0 a 12 anos.')
elif 12 < idade < 18:
  print('Adolescente: 13 a 18 anos.')
elif idade > 18:
  print('Adulto: acima de 18 anos.')
else:
  print('Valor inválido.')

# Solicitar usuário e senha para verificação
login = input('Informe um login de 5 caracteres: ')
senha = input('Informe uma senha de 4 caracteres: ')

if len(login) == 5 and len(senha) == 4:
  print('Login e Senha válidos, aproveite a plataforma.')
else: 
  os.system('clear')
  print('Login e Senha inválidos, tente novamente. \n')
  
# Verificação das coordenadas X e Y
print('Informe as coordenadas X e Y: ')
x = float(input('X: '))
y = float(input('Y: '))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")