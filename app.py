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
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair')

#print('Voce escolheu a opção', opcao_escolhida)
#print(f'Voce escolheu a opção {opcao_escolhida}')
#print(opcao_escolhida == 1)
#print(type(opcao_escolhida))
#print(type(1))

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal. ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('Encerrando o programa.\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        #opcao_escolhida = input('Escolha uma opção: ')
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        #print('Voce escolheu a opção', opcao_escolhida)
        #print(f'Voce escolheu a opção {opcao_escolhida}')
        #print(opcao_escolhida == 1)
        #print(type(opcao_escolhida))
        #print(type(1))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            print('Encerrando o programa')
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()      
    
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()