from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
    
    def __str__(self):
        status = 'ligado' if self._ligado else 'delisgado'
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Tipo: {self.tipo} | Status: {status}' 