valor = float(input('Digite o valor: '))
juros = [0.94, 0.93, 0.91, 0.89, 0.88, 0.87, 0.85, 0.83, 0.82, 0.80, 0.79, 0.77]
print(f'valor a vista {valor}')
for i, v in enumerate(juros):
    valortot = valor / v
    parcela = valortot / (i + 1)
    print(f'{i + 1}X de {parcela:.2f}. Total: {valortot:.2f}')

#arquivo alterado em 15/12/2019!!
