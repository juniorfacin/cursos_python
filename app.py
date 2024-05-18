from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa


def main():
    restaurante_praca = Restaurante('Praça', 'Gourmet')

    # Bebida
    bebida_suco = Bebida('Suco de Melancia', 5.00, 'G')
    bebida_suco.aplicar_desconto()

    # Prato
    prato_lanche = Prato('X-Burguer', 20.00, 'Melhor lanche da cidade.')
    prato_lanche.aplicar_desconto()

    # Sobremesa
    brownie_sobremesa = Sobremesa('Brownie', 15.00,'Bolo', 'G')
    brownie_sobremesa.aplicar_desconto()

    restaurante_praca.adicionar_no_cardapio(bebida_suco)
    restaurante_praca.adicionar_no_cardapio(prato_lanche)
    restaurante_praca.adicionar_no_cardapio(brownie_sobremesa)

    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()