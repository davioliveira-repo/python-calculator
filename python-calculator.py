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

def funcao_quadratica(a, b, c, x=None):
    delta = (b * b) - 4 * a * c
    if pergunta_funcao_quadratica == 'V':
        valor = a * (x * x) + b * x + c
        return valor
    else:
        if delta < 0:
            return f'\033[32mA Função não possui raízes reais exatas, em razão de Delta = {delta}\033[m'
        elif delta == 0:
            x1 = (-b + math.sqrt(delta)) / 2 * a
            return f'\033[32mA Função possui duas raízes reais exatas iguais, em razão de Delta = {delta}, temos X = {x1}\033[m'
        else:
            x1 = (-b + math.sqrt(delta)) / 2 * a
            x2 = (-b - math.sqrt(delta)) / 2 * a
            return f'\033[32mA Função possui duas raízes reais exatas, em razão de Delta = {delta}, temos X1 = {x1} e X2 = {x2}\033[m'


# Área de interface com o usuário
print('-' * 30)
print('''\033[33mTabela de Tipos de Cálculos:

Função Afim: FA
Função Quadrática: FQ
Polígonos: P
\033[m''')
print('-' * 30)
pergunta_categoria = str(input('Qual tipo de cálculo deseja executar?: ')).strip().upper()[0:2]
print('-' * 30)
if pergunta_categoria == 'FA':
    pergunta_funcao_afim = str(input('Deseja Calcular a Raiz ou o Valor da Função?: ')).strip().upper()[0]
    print('-' * 30)
    if pergunta_funcao_afim == 'R':
        a = float(input('Digite o valor de A: '))
        b = float(input('Digite o valor de B: '))
        print('-' * 30)
        _, raiz = funcao_afim(a, b)
        print(f'\033[32mA Função afim em questão tem como raíz: {raiz}\033[m')
        print('-' * 30)
    else:
        a = float(input('Digite o valor de A: '))
        b = float(input('Digite o valor de B: '))
        x = float(input('Digite o valor de X: '))
        print('-' * 30)
        x, _ = funcao_afim(a, b, x)
        print(f'\033[32mA Função afim em questão tem como valor: {x}\033[m')
        print('-' * 30)
elif pergunta_categoria == 'FQ':
    pergunta_funcao_quadratica = str(input('Deseja Calcular o valor da função ou as raízes?: ')).strip().upper()[0]
    print('-' * 30)
    if pergunta_funcao_quadratica == 'V':
        a = float(input('Digite o valor de A: '))
        b = float(input('Digite o valor de B: '))
        c = float(input('Digite o valor de C: '))
        x = float(input('Digite o valor de X: '))
        print('-' * 30)
        valor = funcao_quadratica(a, b, c, x)
        print(f'\033[32mO Valor da função quadrática é igual a: {valor}\033[m')
        print('-' * 30)
    elif pergunta_funcao_quadratica == 'R':
        a = float(input('Digite o valor de A: '))
        b = float(input('Digite o valor de B: '))
        c = float(input('Digite o valor de C: '))
        print('-' * 30)
        raiz = funcao_quadratica(a, b, c)
        print('-' * 30)
        print(raiz)

elif pergunta_categoria == 'P':
    print('''\033[33mTabela de Polígonos:

Prisma de Base Circular: C
Prisma de Base Triangular: T
Prisma de Base Quadrada: Q
Prisma de Base Pentagonal: P
Prisma de Base Hexagonal: HX
Prisma de Base Heptagonal: HP
\033[m''')
    print('-' * 30)
    pergunta_poligonos = str(input('Qual polígono deseja calcular as medidas? [C, T, Q, P, HX, HP]: ')).strip().upper()[0:2]
    print('-' * 30)
    # Área de lógica de condicionais dos poligonos
    if pergunta_poligonos == 'Q':
        base = float(input('Digite a medida da base do quadrilátero em cm: '))
        altura = float(input('Digite a medida da altura do quadrilátero em cm: '))
        comprimento = float(input('Digite a medida do comprimento do prisma em cm: '))
        print('-' * 30)
        resposta = quadrado(base, altura, comprimento)
        print(resposta)
        print('-' * 30)
    elif pergunta_poligonos == 'T':
        base = float(input('Digite a medida da base do triângulo em cm: '))
        altura = float(input('Digite a medida da altura do triângulo em cm: '))
        comprimento = float(input('Digite a medida do comprimento do prisma em cm: '))
        print('-' * 30)
        resposta = triangulo(base, altura, comprimento)
        print(resposta)
        print('-' * 30)
    elif pergunta_poligonos == 'C':
        raio = float(input('Digite a medida do raio do círculo em cm: '))
        comprimento = float(input('Digite a medida do comprimento do prisma em cm: '))
        print('-' * 30)
        resposta = cilindro(raio, comprimento)
        print(resposta)
        print('-' * 30)
    elif pergunta_poligonos == 'P':
        apotema = float(input('Digite a medida do apótema do pentágono em cm: '))
        lado = float(input('Digite a medida do lado do pentágono em cm: '))
        comprimento = float(input('Digite a medida do comprimento do prisma em cm: '))
        print('-' * 30)
        resposta = pentagono(apotema, lado, comprimento)
        print(resposta)
        print('-' * 30)
    elif pergunta_poligonos == 'HX':
        lado = float(input('Digite a medida do lado do hexágono em cm: '))
        comprimento = float(input('Digite a medida do comprimento do prisma em cm: '))
        print('-' * 30)
        resposta = hexagono(lado, comprimento)
        print(resposta)
        print('-' * 30)
    elif pergunta_poligonos == 'HP':
        lado = float(input('Digite a medida do lado do heptágono em cm: '))
        apotema = float(input('Digite a medida do apótema do heptágono em cm: '))
        comprimento = float(input('Digite a medida do comprimento do prisma em cm: '))
        print('-' * 30)
        resposta = heptagono(lado, apotema, comprimento)
        print(resposta)
        print('-' * 30)
