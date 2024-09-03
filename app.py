import os

#restaurantes = ['Pizza', 'Sushi']
restaurantes = [
    {'nome':'Praça', 'categoria':'Japonesa','ativo':False},
    {'nome':'Pizza Suprema','categoria':'Italiana','ativo':True},
    {'nome':'Cantina','categoria':'Brasileira','ativo':False}
]   

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
    print('3. Alterar estado do restaurante')
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
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('Encerrando o programa.')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria_do_restaurante,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Estado do restaurante')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso.'
                if restaurante['ativo']
                else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            )
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')

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
            alterar_estado_restaurante()
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