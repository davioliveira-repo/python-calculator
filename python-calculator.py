# Área de importação de bibliotecas
import math

# Área de funções para todos os cálculos de polígonos
def cilindro(raio, comprimento):
    area_base = (math.pi) * (raio * raio)
    area_total = 2 * ((math.pi) * (raio * raio)) + 2 * ((math.pi) * raio * comprimento)
    volume = area_base * comprimento
    return f'\033[32mÁrea da Base igual a {area_base:.1f}\nÁrea Total igual a {area_total:.1f}\nVolume igual a {volume:.1f}\033[m'

def triangulo(base, altura, comprimento):
    area_base = (base * altura) / 2
    area_lateral = (base + base + base) * comprimento
    area_total = (2 * area_base) + area_lateral
    volume = area_base * comprimento
    return f'\033[32mÁrea da Base igual a {area_base:.1f}\nÁrea Total igual a {area_total}\nVolume igual a {volume:.1f}\033[m'

def quadrado(base, altura, comprimento):
    area_base = base * altura
    area_total = 2 * (altura * base + altura * comprimento + base * comprimento)
    volume = base * altura * comprimento
    return f'\033[32mÁrea da Base igual a {area_base:.1f}\nÁrea Total igual a {area_total:.1f}\nVolume igual a {volume:.1f}\033[m'

def pentagono(apotema, lado, comprimento):
    area_base = (5 * lado * apotema) / 2
    area_lateral = (5 * lado) * comprimento
    area_total = (2 * area_base) + area_lateral
    volume = area_base * comprimento
    return f'\033[32mÁrea da Base igual a {area_base:.1f}\nÁrea Total igual a {area_total:.1f}\nVolume igual a {volume:.1f}\033[m'

def hexagono(lado, comprimento):
    area_base = ((3 * math.sqrt(3)) / 2) * (lado * lado)
    area_lateral = (6 * lado) * comprimento
    area_total = (2 * area_base) + area_lateral
    volume = area_base * comprimento
    return f'\033[32mÁrea da Base igual a {area_base:.1f}\nÁrea Total igual a {area_total:.1f}\nVolume igual a {volume:.1f}\033[m'

def heptagono(lado, apotema, comprimento):
    area_base = ((7 * lado) * apotema) / 2
    area_lateral = (7 * lado) * comprimento
    area_total = (2 * area_base) + area_lateral
    volume = area_base * comprimento
    return f'\033[32mÁrea da Base igual a {area_base:.1f}\nÁrea Total igual a {area_total:.1f}\nVolume igual a {volume:.1f}\033[m'

# Área de Área de funções para todos os cálculos de funções
def funcao_afim(a, b, x=None):
    if x != None:
        x = (a * x) + b
    if b > 0:
        b = -b
    elif b < 0:
        b = b + (b * -2)
    else:
        b = b
    raiz = b / a
    return x, raiz

# Área de interface com o usuário
print('''\033[33mTabela de Tipos de Cálculos:
Função Afim
Polígonos\033[m''')
pergunta_categoria = str(input('Qual tipo de cálculo deseja executar?: ')).strip().upper()[0]
if pergunta_categoria == 'F':
    pergunta_funcao = str(input('Deseja Calcular a Raiz ou o Valor da Função?: ')).strip().upper()
    if pergunta_funcao == 'RAIZ':
        a = float(input('Digite o valor de A: '))
        b = float(input('Digite o valor de B: '))
        _, raiz = funcao_afim(a, b)
        print(raiz)
    else:
        a = float(input('Digite o valor de A: '))
        b = float(input('Digite o valor de B: '))
        x = float(input('Digite o valor de X: '))
        x, _ = funcao_afim(a, b, x)
        print(x)
elif pergunta == 'P':
    print('''\033[33mTabela de Polígonos:
    Prisma de Base Circular: C
    Prisma de Base Triangular: T
    Prisma de Base Quadrada: Q
    Prisma de Base Pentagonal: P
    Prisma de Base Hexagonal: HX
    Prisma de Base Heptagonal: HP \033[m''')
    pergunta = str(input('Qual polígono deseja calcular as medidas? [C, T, Q, P, HX, HP]: ')).strip().upper()[0:2]
    # Área de lógica de condicionais
    if pergunta == 'Q':
        base = float(input('Digite a medida da base do quadrilátero em cm: '))
        altura = float(input('Digite a medida da altura do quadrilátero em cm: '))
        comprimento = float(input('Digite a medida do comprimento do prisma em cm: '))
        resposta = quadrado(base, altura, comprimento)
        print(resposta)
    elif pergunta == 'T':
        base = float(input('Digite a medida da base do triângulo em cm: '))
        altura = float(input('Digite a medida da altura do triângulo em cm: '))
        comprimento = float(input('Digite a medida do comprimento do prisma em cm: '))
        resposta = triangulo(base, altura, comprimento)
        print(resposta)
    elif pergunta == 'C':
        raio = float(input('Digite a medida do raio do círculo em cm: '))
        comprimento = float(input('Digite a medida do comprimento do prisma em cm: '))
        resposta = cilindro(raio, comprimento)
        print(resposta)
    elif pergunta == 'P':
        apotema = float(input('Digite a medida do apótema do pentágono em cm: '))
        lado = float(input('Digite a medida do lado do pentágono em cm: '))
        comprimento = float(input('Digite a medida do comprimento do prisma em cm: '))
        resposta = pentagono(apotema, lado, comprimento)
        print(resposta)
    elif pergunta == 'HX':
        lado = float(input('Digite a medida do lado do hexágono em cm: '))
        comprimento = float(input('Digite a medida do comprimento do prisma em cm: '))
        resposta = hexagono(lado, comprimento)
        print(resposta)
    elif pergunta == 'HP':
        lado = float(input('Digite a medida do lado do heptágono em cm: '))
        apotema = float(input('Digite a medida do apótema do heptágono em cm: '))
        comprimento = float(input('Digite a medida do comprimento do prisma em cm: '))
        resposta = heptagono(lado, apotema, comprimento)
        print(resposta)
