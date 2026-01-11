import os
#snake_case = urderline para separar cada palavras / Variaveis, funções e métodos4
#SCREAMING_SNAKE_CASE = em capslock urderline para separar cada palavras / constantes
#PascalCase = cada palavra começa com maius4cula / classes
#Motivo da aula
#criando Sabor Express (?) / menu para cadastrar restaurantes

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False},
                {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo':True},
                {'nome': 'Acai muito bom', 'categoria': 'Doces', 'ativo':False}]

def limpa_e_msg(texto):
    os.system
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def voltar_menu():
    input('Digite uma tecla para voltar ao menu principal:')
    main()

def exibir_nome_do_programa():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar status restaurante')
    print('4. Sair\n')

def alternar_estado_restaurante():
    limpa_e_msg('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurente que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            msg = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(msg)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_menu()

def finalizar_app():
    limpa_e_msg('Finalizando o app\n')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu()

def cadastrar_novo_restaurante():
    limpa_e_msg('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('\nDigite o nome do restaurante que deseja cadastrar: ')
    categoria =  input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    limpa_e_msg('Listando os restaurantes\n')
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        categoria_restaurante = restaurante['categoria']

        print(f'{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo.ljust(20)}')
    voltar_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
    #print('Você escolheu a opção', opcao_escolhida)
    #print(f'Você escolheu a opção {opcao_escolhida}')
    #opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 1:
            #print('Cadastrar restaurante:')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            #print('Listar restaurante')
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
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

#deixar o arquivo como principal
if __name__ == '__main__':
        main()