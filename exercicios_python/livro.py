class Livro:
    livros = []  # Lista para manter todos os livros criados

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)  # Adiciona esta instância à lista de livros

    def __str__(self):
        return f'{self.titulo} | {self.autor} | {self.ano_publicacao}'
    
    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis



        





