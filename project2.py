print('   Bem vindo a Loja de Gelados do Rodrigo')
print('------------------ Cardapio -----------------')
print('---| Tamanho | Cupuaçu (CP) |  Açai (AC) |---')
print('---|    P    |   R$  9,00   |  R$ 11,00  |---')
print('---|    M    |   R$ 14,00   |  R$ 16,00  |---')
print('---|    G    |   R$ 18,00   |  R$ 20,00  |---')
print('---------------------------------------------')

total = 0  #acumulador
while True:  #esse Loop vai permanecer ate o Break ser chamado
    sabor = input('Qual o sabor? (AC/CP):').upper()

    if sabor != 'AC' and sabor != 'CP':
        print('sabor nao existe, tente novamente')
        continue  # repete a pergunta até que seja respondida conforme o anunciado
    elif sabor == 'AC':
        tamanho = input('Qual o tamanho? (P/M/G):').upper()
        while tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
            print('Tamanho errado, tente novamente')
            tamanho = input('Qual o tamanho? (P/M/G):').upper()

        if tamanho == 'P':
            total += 11
            print(f'um ACAI tamanho P de R$ 11,00 reais, o total da sua compra até o momento é de R$ {total:.2f}')
        elif tamanho == 'M':
            total += 16
            print(f'um ACAI tamanho M de R$ 16,00 reais, o total da sua compra até o momento é de R$ {total:.2f}')
        else:
            total = total + 20
            print(f'um ACAI tamanho G de R$ 20,00 reais, o total da sua compra até o momento é de R$ {total:.2f}')

    elif sabor == 'CP':
        tamanho = input('Qual o tamanho? (P/M/G):').upper()
        while tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
            print('Tamanho errado, tente novamente')
            tamanho = input('Qual o tamanho? (P/M/G):').upper()

        if tamanho == 'P':
            total += 9
            print(f'um CUPUACU tamanho P de R$ 9,00 reais, o total da sua compra até o momento é de R$ {total:.2f}')
        elif tamanho == 'M':
            total += 14
            print(f'um CUPUACU tamanho M de R$ 14,00 reais, o total da sua compra até o momento é de R$ {total:.2f}')
        else:
            total = total + 18
            print(f'um CUPUACU tamanho G de R$ 18,00 reais, o total da sua compra até o momento é de R$ {total:.2f}')

    sair = input('Deseja mais alguma coisa? (S/N):').upper() #A cada pedido essa pergunta é feita
    while sair != 'S' and sair != 'N':
        sair = input('Deseja mais alguma coisa? (S/N):').upper()
    if sair == 'S':
        continue
    else:
        print(f'o valor a ser pago R${total:.2f}.') #Valor total do pedido
        break