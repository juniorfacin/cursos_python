class Contador:
    '''
    Classe que representa um contador.
    A instância mantém um contador específico, enquanto um contador global é compartilhado por todas as instâncias.
    '''

    contador_global = 0

    def __init__(self):
        self.valor = 0

    def __str__(self):
        return f'Contador: {self.valor}'

    def incrementar(self, incremento = 1):
        self.valor += incremento
        
    @classmethod
    def zerar_contador_global(cls):
        cls.contador_global = 0
        return 'Contador global foi zerado.'

contador1 = Contador()
contador2 = Contador()

contador1.incrementar(3)
contador2.incrementar(5)

print(contador1)
print(contador2)

print(Contador.zerar_contador_global())

###################################################################

class Pessoa:
    def __init__(self, nome, idade, profissao=''):
        self.nome = nome
        self.idade = idade
        self._profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self._profissao if self._profissao else "sem profissão"}'

    @property
    def profissao(self):
        return self._profissao

    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self._profissao}.'
        else:
            return f'Olá, sou {self.nome}!'

    def aniversario(self):
        self.idade += 1


# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa('Alice', 25, 'Engenheira')
pessoa2 = Pessoa('Luiza', 30, 'Desenvolvedor')
pessoa3 = Pessoa('Jaque', 22)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)