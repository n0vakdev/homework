# função para exibir uma mensagem de Boas-Vindas
def boas_vindas(mensagem):
    comprimento_mensagem = len(mensagem)
    borda = '+' + '-' * (comprimento_mensagem + 2) + '+'

    print(borda)
    print('| ' + mensagem + ' |')
    print(borda)

boas_vindas('       Bem vindo à Livraria de Rodrigo        ')

# função para cadastrar um novo livro
def cadastrar_novo_livro(identificador):
    print("-" * 50)
    print("-" * 14, "MENU CADASTRAR LIVRO", "-" * 14)
    print()

    global identificador_global # uso da variável global

    identificador = identificador_global + 1 # incremento do identificador global
    
    # entrada de informações do novo livro
    print(f"ID do Livro: {identificador}")
    nome = input("Nome do LIVRO: ").upper()
    autor = input("Nome do AUTOR: ").upper()
    editora = input("Nome da EDITORA: ").upper()
    identificador_global += 1 # atualização do identificador global

    livro = {"ID": identificador, "NOME": nome, "AUTOR": autor, "EDITORA": editora}

    print()

    return livro # retorna representando o novo livro

# função para consultar informações sobre os livros
def consultar_livro():
    while True:
        try:
            print("-" * 50)
            print("-" * 14, "MENU CONSULTAR LIVRO", "-" * 14)
            print()

            # menu para escolher a opção de consulta
            ec = int(input("""
            1 - Consultar Todos os Livros
            2 - Consultar Livro por ID
            3 - Consultar Livro(s) por Autor
            4 - Retornar ao Menu\n\n
            """))

            if ec == 1:
                # opção para consultar TODOS os livros 
                if not lista_livros:
                    print("Não foi cadastrado nenhum livro.")
                    break
                else:
                    for nome in lista_livros:
                        print(f"{nome['ID']}º Livro:")
                        print(f"ID: {nome['ID']}")
                        print(f"NOME: {nome['NOME']}")
                        print(f"AUTOR: {nome['AUTOR']}")
                        print(f"EDITORA: {nome['EDITORA']}")
                        print()
            
            # opção para consultar o livro pelo seu ID
            elif ec == 2:
                if not lista_livros:
                    print("Não foi cadastrado nenhum livro.")
                    break

                escolha = int(input("Informe o ID do livro que deseja consultar: "))

                if escolha <= 0 or escolha > len(lista_livros):
                    print("Não existe nenhum livro com esse ID.")

                for id in lista_livros:
                    if escolha == id["ID"]:
                        print(f"ID: {id['ID']}")
                        print(f"NOME: {id['NOME']}")
                        print(f"AUTOR: {id['AUTOR']}")
                        print(f"EDITORA: {id['EDITORA']}")
            
            # opção para consultar os livros pelo seu AUTOR
            elif ec == 3:
                if not lista_livros:
                    print("Não foi cadastrado nenhum livro.")
                    break
                
                # solicita um autor ao usuário
                escolha = input("Qual autor deseja consultar? ").upper()

                livro_encontrado = False

                for livro in lista_livros:
                    if escolha == livro["AUTOR"]:
                        print(f"ID: {livro['ID']}")
                        print(f"NOME: {livro['NOME']}")
                        print(f"AUTOR: {livro['AUTOR']}")
                        print(f"EDITORA: {livro['EDITORA']}")
                        print()

                        # ao encontrar, muda a variável de controle para TRUE
                        livro_encontrado = True
            
                # Se não encontrar apresenta essa mensagem ao usuário
                if not livro_encontrado:
                    print("Não existe nenhum livro desse autor.")

            # retorna ao Menu Principal
            elif ec == 4:
                break
            
            # se o usuário informar algum valor que não esteja entre as opções
            else:
                print("Opção inválida. Tente novamente.\n")

        #caso o usuário digite um valor inválido
        except ValueError:
            print("Valor inválido. Tente novamente.\n")

# Função que remove livro da lista
def remover_livro():
    print("-" * 50)
    print("-" * 15, "MENU REMOVER LIVRO", "-" * 15)
    print()

    while True:
        try:
            # verifica se a lista de livros está vazia
            if not lista_livros:
                print("Não foi cadastrado nenhum livro.")
                break

            # solicita ao usuário o ID do livro que ele deseja remover
            er = int(input("Deseja remover o livro com qual ID: "))

            # inicia a variável como FALSE para realizar o controle
            id_encontrado = False

            if er <= 0 or er > len(lista_livros):
                print("ID Inválido. Por favor, insira um ID válido.")
                print()
                continue
            
            # busca na lista de livros o ID informado
            for id in lista_livros:
                # se encontrar o ID fornecido, mostra uma mensagem de confirmação
                if er == id["ID"]:
                    id_encontrado = True
                    escolha = input("Tem certeza que deseja excluir esse livro? (S/N) ").upper()
                    
                    # se o usuário confirmar, a remoção será realizada
                    if escolha == 'S':
                        lista_livros.remove(id)
                        print(f"Livro {id['NOME']} removido com sucesso.")
                        print()
            if not id_encontrado:
                print("Não existe nenhum livro com esse ID.")
                print()
            
            # Sai do loop
            break

        # caso o usuário digite um valor inválido
        except ValueError:
            print("Opção inválida. Tente novamente.\n")
            print()

# PROGRAMA PRINCIPAL

# declarando variável global e a lista vazia
lista_livros = []
identificador_global = 0

# estrutura de Menu fora da Função
while True:
    print("-" * 50)
    print("-" * 17, "MENU PRINCIPAL", "-" * 17)
    print()

    try:
        # Menu Principal
        menu = int(input("""Escolha a opção desejada:
        1 - Cadastrar Livro
        2 - Consultar Livro(s)
        3 - Remover Livro
        4 - Sair \n\n"""))

       # opção para CADASTRAR novo livro
        if menu == 1:
            novo_livro = cadastrar_novo_livro(identificador_global)

            for livro in lista_livros:
                if novo_livro["NOME"] == livro["NOME"] and novo_livro["AUTOR"] == livro["AUTOR"]:
                    print(f"{novo_livro['NOME']} já existe na lista.") # exibe se o nome e autor do livro já existe
                    identificador_global -= 1

                    # sai do loop
                    break
            # Se não existir nenhum livro com mesmo nome e autor realiza o cadastro do novo livro
            else:
                lista_livros.append(novo_livro)
                print(f"Livro {novo_livro['NOME']} cadastrado com sucesso.")

        # opção para CONSULTAR os livros cadastrados
        elif menu == 2:
            consultar_livro()

        # opção para REMOVER o livro desejado
        elif menu == 3:
            remover_livro()

        # opção para SAIR do programa
        elif menu == 4:
            print("Programa Finalizado.")
            break
        else:
            print("Opção Inválida. Escolha uma das opções do Menu.\n")
    except ValueError:
        print("Valor inválido. Tente novamente.\n")