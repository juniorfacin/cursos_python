class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
         # Transformando em um atributo privado / acessado apenas com a Property
        self._ativo = False
        Restaurante.restaurantes.append(self)
        
    # Método str para retornar em string
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    # Estamos puxando as informações direto da lista que armazena o objeto.
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()