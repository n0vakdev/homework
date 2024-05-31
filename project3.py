# Mensagem de Boas-Vindas
def boas_vindas(mensagem):
    comprimento_mensagem = len(mensagem)
    borda = '+' + '-' * (comprimento_mensagem + 2) + '+'

    print(borda)
    print('| ' + mensagem + ' |')
    print(borda)

boas_vindas('Bem-vindo a copiadora de Rodrigo')
print('DIG - Digitalização ')
print('ICO - Impressão Colorida ')
print('IPB - Impressão Preto e Branco')
print('FOT - Fotocópia')


# Função para escolher o Serviço Desejado.
def escolha_servico():
    while True:
        servico = input('Escolha o serviço desejado (DIG/ICO/IPB/FOT): ').upper()
        if servico in ['DIG', 'ICO', 'IPB', 'FOT']:
            return servico
        else:
            print('Opção inválida! escolha entre DIG, ICO, IPB ou FOT.')

# Função para obter o Número de Páginas com Desconto
def num_pagina():
    while True:
        try:
            num_pagina = int(input('Digite o número de páginas: '))
            if num_pagina < 20:
                return num_pagina
            elif num_pagina >= 20 and num_pagina < 200:
                return int(num_pagina * 0.85)
            elif num_pagina >= 200 and num_pagina < 2000:
                return int(num_pagina * 0.80)
            elif num_pagina >= 2000 and num_pagina < 20000:
                return int(num_pagina * 0.75)
            else:
                print('Número de páginas muito grande! insira um valor menor.')
        except ValueError:
            print('Entrada inválida! insira um número válido.')

# Função para escolher o Serviço Extra
def servico_extra():
    while True:
        servico_extra = input('Deseja algum serviço extra? \n1 - Encadernação Simples - R$ 15.00\n2 - Encadernação de Capa Dura R$ 40.00\n0 - Nenhum:\n')
        if servico_extra in ['1', '2', '0']:
            return int(servico_extra)
        else:
            print('Opção inválida! escolha entre 1, 2 ou 0.')

try:
    # detalhes do pedido
    servico = escolha_servico()
    num_paginas = num_pagina()
    servico_adicional = servico_extra()

    # Cálculo do custo total
    custo_pagina = {'DIG': 1.10, 'ICO': 1.00, 'IPB': 0.40, 'FOT': 0.20}
    custo_extra = {1: 15, 2: 40, 0: 0}
    total = (custo_pagina[servico] * num_paginas) + custo_extra[servico_adicional]

    # Exibindo o resultado
    print('\nDetalhes do Pedido:')
    print(f'Serviço: {servico}')
    print(f'Número de Páginas: {num_paginas}')
    print(f'Serviço Adicional: {servico_adicional}')
    print(f'Total a Pagar: R$ {total:.2f}')

except:
    print('Ocorreu um erro')
