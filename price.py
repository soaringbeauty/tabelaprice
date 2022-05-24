# [DECLARANDO AS VARIÁVEIS INICIAIS DE ACORDO COM O ENUNCIADO]
# VALOR A FINANCIAR = R$1.000
valor = 100000
# TAXA DE JUROS = 3% (já sendo convertida para decimal)
i = 5 / 100
# Nº DE PARCELAS/TEMPO PARA PAGAR = 5 meses
n = 5

# [DECLARANDO AS VARIÁVEIS PARA A TABELA PRICE]
# A variável PARCELA recebe o resultado da fórmula de PMT
parcela = valor * (pow(1+i, n)) * i / (pow(1+i, n) - 1)
saldoanterior = valor
juros = saldoanterior * i
amortizacao = parcela - juros
saldodevedor = saldoanterior - amortizacao

# MOSTRANDO A TABELA NA TELA
print('-'*20, 'TABELA PRICE', '-'*20)
print('N | PRESTAÇÃO  | AMORTIZAÇÃO|  JUROS    | SALDO DEVEDOR')
print(f'1 | R${parcela:.2f} | R${(amortizacao):.2f} | R${juros:.2f} | R${saldodevedor:.2f}')

# Iniciando o loop para fazer o cálculo de amortizações durante 5 meses
# A variável MESES inicia com o valor de 2, pois o 1º mês já foi definido anteriormente
meses = 2
while meses < 6:
    juros = saldodevedor * i
    amortizacao = parcela - juros
    saldodevedor = saldodevedor - amortizacao
    print(f'{meses} | R${parcela:.2f} | R${(amortizacao):.2f} | R${juros:.2f} | R${saldodevedor:.2f}')
    meses += 1
    if meses == 5:
        valoramorizacao = amortizacao
print(f'O valor da AMORTIZAÇÃO na 4ª prestação será de: R${valoramorizacao:.2f}')
print('-'*60)

# Feito por Ana Luiza Gonzaga
