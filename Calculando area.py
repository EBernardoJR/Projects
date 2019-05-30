def quadrado(larg, comp):
    area = larg * comp
    print(f'A área do quadrado/retangulo {larg}x{comp} é igual a: {area:.2f}')


def triangulo(bas, alt):
    area = (alt * bas) / 2
    print(f'A área do triângulo é igual a: {area:.2f}')


def circulo(raio):
    area = 3.1415 * raio
    print(f'A área do circulo é igual a: {area:.2f}')



def trianguloretan(larg, comp):
    area = (larg * comp) / 2
    print(f'A area do triângulo retângulo é: {area:.2f}')



def trapezio(Bmaior, bmenor, alt):
    area = (Bmaior + bmenor) * alt / 2
    print(f'A área do trapézio é igual a: {area:.2f}')

while True:
    print('='*25)
    print('     Calculando area     ')
    print('='*25)
    print('Escolha qual area calcular:')
    print('[A] Quadrado / Retângulo  ')
    print('[B] Triângulo ')
    print('[C] Triângulo Retângulo ')
    print('[D] Trapézio ')
    print('[E] Circulo  ')
    print('[F] Cancelar ')
    resp = str(input('Resposta: ')).upper()
    if resp not  in 'ABCDEF':
        print('Resposta inválida, digite novamente ')
    if resp in 'F':
        print('Processo finalizado')
        break
    if resp in 'A':
        largura = float(input('Digite a largura da area: '))
        comprimento = float(input('Digite o comprimento da area: '))
        quadrado(largura, comprimento)
    elif resp in 'C':
        largura = float(input('Digite a largura da area do triângulo retângulo: '))
        comprimento = float(input('Digite o comprimento da area: '))
        trianguloretan(largura, comprimento)
    elif resp in 'B':
        base = float(input('Digite o valor da base do triângulo: '))
        altura = float(input('Digite o valor da altura: '))
        triangulo(base, altura)
    elif resp in 'D':
        basemenor = float(input('Digite o valor da base menor: '))
        basemaior = float(input('Digite o valor da base maior: '))
        alturat = float(input('Digite o valor da altura: '))
        trapezio(basemaior, basemenor, alturat)
    elif resp in 'E':
        raio = float(input('Digite o valor do raio: '))
        circulo(raio)
    print('')