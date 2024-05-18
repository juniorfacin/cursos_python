from abc import ABC, abstractmethod

# Se estamos usando a classe ABC, é como se tivesses herdando ela. Por isso, colocar como parâmetro de ItemCardapio:
class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass