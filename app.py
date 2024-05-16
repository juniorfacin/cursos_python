from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'G')
prato_lanche = Prato('X-Burguer', 20.00, 'Melhor lanche da cidade.')

def main():
    print(bebida_suco)
    print(prato_lanche)

if __name__ == '__main__':
    main()