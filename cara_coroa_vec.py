import numpy as np

N_SIMULACOES = 1000000

matriz = np.random.randint(0, 2, (N_SIMULACOES,10))
soma = np.sum(matriz,axis=1)
v_resposta = soma == 5
s_true = np.sum(v_resposta)

print(s_true/N_SIMULACOES)