# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro:
    def __init__(self, modelo, cor, ano = 0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro('Tracker', 'Azul', 2023)

print(vars(carro1))

# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, regiao, ativo=False, delivery=False, ):
        self.nome = nome
        self.categoria = categoria
        self.regiao = regiao
        self.ativo = ativo
        self.delivery = delivery

novo_restaurante = Restaurante(nome = 'Busguer', categoria = 'Lanche', regiao = 'Zona Sul', ativo = True, delivery = True)

print(vars(novo_restaurante))

# 3 Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante2:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
    
    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria}'

novo_restaurante = Restaurante2(nome = 'Busguer', categoria = 'Lanche', ativo = True)

print(novo_restaurante)

class Cliente:
    def __init__(self, nome, idade, telefone, email):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
    
    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade} | Telefone: {self.telefone} | Email: {self.email}'

cliente1 = Cliente('Alice', 25, 'alice@gmail.com', '123-456-7890')
cliente2 = Cliente('Bob', 30, 'bob@gmail.com', '987-654-3210')
cliente3 = Cliente('Charlie', 22, 'charlie@gmail.com', '555-123-4567')

print(cliente1)
print(cliente2)
print(cliente3)