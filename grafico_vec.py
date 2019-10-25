import numpy as np
import matplotlib.pyplot as plt


N_PONTOS = 1000000
lista_x = []
inicio = -1000
fim = 1000

lista_x = np.linspace(inicio,fim,N_PONTOS)
lista_y = np.sin(lista_x) -7**(-6) + np.cos(np.sqrt(np.abs(lista_x)))
lista_aleat = 1 + np.random.randint(0,50,size=N_PONTOS)/100
lista_y = lista_y * lista_aleat

#plt.plot(lista_x, lista_y)
#plt.show()
