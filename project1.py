def boas_vindas(mensagem):
    comprimento_mensagem = len(mensagem)
    borda = '+' + '-' * (comprimento_mensagem + 2) + '+'

    print(borda)
    print('| ' + mensagem + ' |')
    print(borda)

boas_vindas('Bem vindo a Loja de Rodrigo')

valor_produto = float(input('Entre com o valor do produto: '))
qtd_produto = int(input('Entre com a quantidade do produto: '))

#Pega o valor total calculando a Quantidade * o Valor do produto
total = qtd_produto * valor_produto

#verifica as condições de desconto conforme as informações fornecidas
if total < 2500:
    desconto = 0 # desconto de 0%
elif total >= 2500 and total < 6000:
    desconto = 0.04 # desconto de 4%
elif total >= 6000 and total < 10000:
    desconto = 0.07 # desconto de7%
else:
    desconto = 0.11 # desconto de 11%

#Calcula o valor do desconto
valor_desconto = total * desconto
#Calcula o preço final com o desconto
preco_final = total - valor_desconto

print(f'O valor SEM desconto: {total:.2f}')
print(f'O valor COM desconto: {preco_final:.2f}')

