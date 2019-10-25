import numpy as np

N_SIMULACOES = 1000000

v_aleat_a = np.random.randint(1,5,size=N_SIMULACOES)
v_aleat_b = np.random.randint(10,20,size=N_SIMULACOES)
v_aleat_c = np.random.randint(1,5,size=N_SIMULACOES)

lista_delta = v_aleat_b**2 - 4*v_aleat_a*v_aleat_c
lista_raiz_positiva = (-v_aleat_b + np.sqrt(lista_delta)) / 2*v_aleat_a
lista_raiz_negativa = (-v_aleat_b - np.sqrt(lista_delta)) / 2*v_aleat_a
lista_raiz_positiva = lista_raiz_positiva.reshape(N_SIMULACOES,1)
lista_raiz_negativa = lista_raiz_negativa.reshape(N_SIMULACOES,1)
resultados = np.concatenate([lista_raiz_positiva,lista_raiz_negativa],axis=1)
