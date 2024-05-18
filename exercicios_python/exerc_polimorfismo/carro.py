from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
    
    def __str__(self):
        return f'{self.marca} | {self.modelo} | {self.cor}'
    
    def ligar(self):
        print(f"O carro {self.modelo} está ligado.")