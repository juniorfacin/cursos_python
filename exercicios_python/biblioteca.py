from livro import Livro

# Adiciona mais livros para teste
livro1 = Livro("Python Basics", "John Doe", 2020)
livro2 = Livro("Advanced Python", "Jane Smith", 2020)
livro3 = Livro("Python in Practice", "Emily Coder", 2021)

# Empresta um dos livros de 2020
livro1.emprestar()

# Verifica a disponibilidade dos livros de 2020
ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {[str(livro) for livro in livros_disponiveis_ano]}")
