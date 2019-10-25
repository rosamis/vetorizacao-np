from random import randrange

N_SIMULACOES = 1000000

hits = 0

for _ in range(N_SIMULACOES):
    jogadas = [randrange(0,2) for _ in range(10)]
    if sum(jogadas) == 5:
        hits+=1

print(hits/N_SIMULACOES)