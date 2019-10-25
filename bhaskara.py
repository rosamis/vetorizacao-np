from random import randrange
import math


N_SIMULACOES = 1000000

lista_a_b_c = [[randrange(1,5), randrange(10,20), randrange(1,5)] for _ in range(N_SIMULACOES)]
resultados = []

for a,b,c in lista_a_b_c:
    delta = b**2 - 4 * a * c
    raiz_positiva = (-b + math.sqrt(delta)) / 2*a
    raiz_negativa = (-b - math.sqrt(delta)) / 2*a
    resultados.append([raiz_positiva, raiz_negativa])
