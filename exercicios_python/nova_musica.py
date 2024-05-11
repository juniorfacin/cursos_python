class Musica:
	nome = ''
	artista = ''
	duracao = float

musica1 = Musica()
musica1.nome = 'Numb'
musica1.artista = 'Link Park'
musica1.duracao = 3.5

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 4.0

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 3.5


print(vars(musica1))
print(vars(musica2))
print(vars(musica3))


musicaTeste = Musica()
musicaTeste.nome = 'Bohemian Rhapsody'
musicaTeste.duracao = 355

print(f'Música: {musicaTeste.nome} - Banda: {musicaTeste.artista} - {musicaTeste.duracao} segundos')