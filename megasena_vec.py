import numpy as np
N_SIMULACOES = 100000000

meu_jogo = np.random.randint(1,61,(N_SIMULACOES,6))
jogo_sorteado = np.random.randint(1,61,(N_SIMULACOES,6))

meu_jogo = np.sort(meu_jogo)
jogo_sorteado = np.sort(jogo_sorteado)

resultado = meu_jogo == jogo_sorteado
v_true = np.sum(resultado,axis=1)
l_ganhou = v_true == 6
ganhou = np.sum(l_ganhou)
