#parte 2

totnotas = int(input("Quantas notas você quer colocar? "))
pesotot = 0
notafinal = 0
for c in range(1, totnotas + 1):
    nota = float(input(f'Qual sua nota {c}? '))
    pesonota = int(input(f'Qual o peso da nota {c}? '))
    notatot = nota * pesonota
    pesotot += pesonota
    notafinal += notatot
media = notafinal / pesotot
print(f'Sua media é: {media:.2f}')
#arquivo alterado em 15/12/2019