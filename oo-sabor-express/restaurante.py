# Sintaxe
class Restaurante:
	nome = ''  # Esses são os atributos das classes
	categoria = ''
	ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
restaurante_praca.ativo = True

# 1
print(f'Nome: {restaurante_praca.nome}')

# 2
print(restaurante_praca.ativo)
if restaurante_praca.ativo == True:
	print('O restaurante está ativo!')
else:
	print('O restaurante está inativo.')

# 3 e 4
# Alterar o atributo da classe fora dela - Não é uma boa prática
Restaurante.categoria = 'Italiana'
categoria = Restaurante.categoria
print(categoria)

# 5
restaurante_praca.nome = 'Bistrô'
print(restaurante_praca.nome)

# 6
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
print(f'Esse é o novo restaurante "{restaurante_pizza.nome}" na categoria "{restaurante_pizza.categoria}"')

# 7
if restaurante_pizza.categoria == 'Fast Food':
	print(f'Categoria correta: "{restaurante_pizza.categoria}"')
else:
	print('Categoria incorreta, verificar.')

# 8
restaurante_pizza.ativo = True

# 9
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')
