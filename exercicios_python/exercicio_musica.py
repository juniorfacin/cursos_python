''''
Exercício -  Refaça a classe abaixo de uma forma mais concisa
class Musica:
    nome = ''
    artista = ''
    duracao = int

'''

class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self. artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')


nova_musica = Musica('Link Park ft. Jay-z', 'Numb', 120)

Musica.listar_musicas()

# Exemplo do Instrutor
class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

print(vars(musica1))