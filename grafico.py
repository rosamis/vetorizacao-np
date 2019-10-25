import math
import matplotlib.pyplot as plt
import random


def f(x):
    return (math.sin(x) - 7**(-6) + math.cos(math.sqrt(abs(x)))) * (1 + random.randrange(0,50)/100)


N_PONTOS = 1000000
lista_x = []
inicio = -1000
fim = 1000

passo = (fim - inicio)/N_PONTOS
x_inicial = inicio
for i in range(N_PONTOS):
    lista_x.append(x_inicial)
    x_inicial += passo

lista_y = []
for i in lista_x:
    lista_y.append(f(i))

#plt.plot(lista_x, lista_y)
#plt.show()


