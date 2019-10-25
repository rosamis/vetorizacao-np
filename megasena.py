from random import randrange

N_SIMULACOES = 1000000

hits = 0

for i in range(N_SIMULACOES):
    meu_jogo = []
    for _ in range(6):
        novo_num = randrange(1,61)
        while novo_num in meu_jogo:
            novo_num = randrange(1,61)
        meu_jogo.append(novo_num)

    jogo_sorteado = []
    for _ in range(6):
        novo_num = randrange(1,61)
        while novo_num in jogo_sorteado:
            novo_num = randrange(1,61)
        jogo_sorteado.append(novo_num)
    
    resultado = [i in jogo_sorteado for i in meu_jogo]
    # for i in meu_jogo:
    #     if i in jogo_sorteado:
    #         resultado.append(True)
    #     else:
    #         resultado.append(False)
    if all(resultado):
        hits += 1
print(hits)
