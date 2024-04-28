import os
restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
      print("""
      ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
      ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
      ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
      ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
      ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
      ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
      """)
      
def exibir_opcoes():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Ativar restaurante')
      print('4. Sair \n')

def voltar_ao_menu_principal():
      input('\nDigite qualquer tecla para retornar ao Menu Principal: ')
      main()

def finalizar_app():
      exibir_subtitulo('Finalizando o App!')
      # os.system('cls') P/ sistema operacional Windows

def opcao_invalida():
      print('Opção inválida! \n')
      voltar_ao_menu_principal()

def exibir_subtitulo(texto):
      os.system('clear')
      print(texto, '\n')

def cadastrar_novo_restaurante():
      exibir_subtitulo('Cadastros de novos restaurantes: ')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      restaurantes.append(nome_do_restaurante)
      print(f'O restaurante: {nome_do_restaurante}, foi cadastrado com sucesso! \n')
      voltar_ao_menu_principal()

def escolher_opcao():
      try:      
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()   
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:
                  print('Ativar restaurante')
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()
            
def listar_restaurantes():
      exibir_subtitulo('Listando os Restaurantes: ')
      for restaurante in restaurantes:
            print(f'.{restaurante}') 
      voltar_ao_menu_principal()

def main():
      os.system('clear')
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()

if __name__ == '__main__':
      main()