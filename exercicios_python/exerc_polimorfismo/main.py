from carro import Carro

def main():
    """
    Função principal que cria instâncias de Carro e executa ações sobre elas.
    """
    carro1 = Carro("Ford", "Focus", "Preto")
    carro2 = Carro("Chevrolet", "Cruze", "Prata")
    carro3 = Carro("Honda", "Civic", "Vermelho")

    print(carro1)
    print(carro2)
    print(carro3)
    
    carro1.ligar()

if __name__ == '__main__':
    main()