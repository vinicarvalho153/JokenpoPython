import random
print('''Escolha um modo de jogo:
[1]- Jogador x Jogador
[2]- Jogador x IA
[3]- IA x IA''')
inserirOpcao = int(input("Escolha uma opção: "))
valoresComputador = ('pedra', 'papel', 'tesoura')
continuarJogo = True
score1 = 0
score2 = 0
while inserirOpcao == 1 and continuarJogo:
    print('''Faça sua jogada:
[0]- Pedra
[1]- Papel
[2]- Tesoura''')
    inserirValorJogador1 = int(input("Jogada do jogador(1):"))
    inserirValorJogador2 = int(input("Jogada do jogador(2):"))

    if inserirValorJogador1 == 0 and inserirValorJogador2 == 1:
        score2 += 1
        print("Jogador(2) Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif inserirValorJogador1 == 0 and inserirValorJogador2 == 2:
        score1 += 1
        print("Jogador(1) Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif inserirValorJogador1 == 1 and inserirValorJogador2 == 0:
        score1 += 1
        print("Jogador(1) Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif inserirValorJogador1 == 1 and inserirValorJogador2 == 2:
        score2 += 1
        print("Jogador(2) Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif inserirValorJogador1 == 2 and inserirValorJogador2 == 0:
        score2 += 1
        print("Jogador(2) Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif inserirValorJogador1 == 2 and inserirValorJogador2 == 1:
        score1 += 1
        print("Jogador(1) Ganhou!")
        print(str(score1) + " X " + str(score2))
    else:
        print("O jogo deu empate!")
        print(str(score1) + " X " + str(score2))

    print('''Quer continuar jogando? 
[1]- Sim
[2]- Não''')
    continuarJogo = input("Continuar jogo? ")

    if continuarJogo == "1":
        continuarJogo = True
    elif continuarJogo == "2":
        if score1 > score2:
            print("Jogador 1 ganhou a partida!")
        elif score1 < score2:
            print("Jogador 2 ganhou a partida!")
        else:
            print("O Terminou empatado!")
            print("Jogador 1: " + str(score1))
            print("Jogador 2: " + str(score2))
            print("Obrigado por jogar o meu jogo! feito por Vinícius Faria da Silva Carvalho")
            continuarJogo = False

while inserirOpcao == 2 and continuarJogo:
    print('''Faça sua jogada:
[0]- Pedra
[1]- Papel
[2]- Tesoura''')
    inserirValorJogador1 = int(input("Jogada do jogador:"))
    computador1 = random.randint(0, 2)
    print("computador jogou {}".format(valoresComputador[computador1]))

    if inserirValorJogador1 == 0 and computador1 == 1:
        score2 += 1
        print("O Computador Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif inserirValorJogador1 == 0 and computador1 == 2:
        score1 += 1
        print("Jogador(1) Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif inserirValorJogador1 == 1 and computador1 == 0:
        score1 += 1
        print("Jogador(1) Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif inserirValorJogador1 == 1 and computador1 == 2:
        score2 += 1
        print("O Computador Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif inserirValorJogador1 == 2 and computador1 == 0:
        score2 += 1
        print("O Computador Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif inserirValorJogador1 == 2 and computador1 == 1:
        score1 += 1
        print("Jogador(1) Ganhou!")
        print(str(score1) + " X " + str(score2))
    else:
        print("O jogo deu empate!")
        print(str(score1) + " X " + str(score2))

    print('''Quer continuar jogando? 
[1]- Sim
[2]- Não''')
    continuarJogo = input("Continuar jogo? ")

    if continuarJogo == "1":
        continuarJogo = True
    elif continuarJogo == "2":
        if score1 > score2:
            print("Jogador 1 é o vencedor final do jogo!")
        elif score1 < score2:
            print("Jogador 2 é o vencedor final do jogo!")
        else:
            print("O Terminou empatado!")
            print("Jogador 1: " + str(score1))
            print("Jogador 2: " + str(score2))
            print("Obrigado por jogar o meu jogo! feito por Vinícius Faria da Silva Carvalho")
            continuarJogo = False

while inserirOpcao == 3 and continuarJogo:
    computador1 = random.randint(0, 2)
    computador2 = random.randint(0, 2)

    if computador2 == 0 and computador1 == 1:
        score2 += 1
        print("O Computador 2 Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif computador2 == 0 and computador1 == 2:
        score1 += 1
        print("O Computador 1 Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif computador2 == 1 and computador1 == 0:
        score1 += 1
        print("O Computador 1  Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif computador2 == 1 and computador1 == 2:
        score2 += 1
        print("O Computador 2 Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif computador2 == 2 and computador1 == 0:
        score2 += 1
        print("O Computador 2 Ganhou!")
        print(str(score1) + " X " + str(score2))
    elif computador2 == 2 and computador1 == 1:
        score1 += 1
        print("O Computador 1  Ganhou!")
        print(str(score1) + " X " + str(score2))
    else:
        print("O jogo deu empate!")
        print(str(score1) + " X " + str(score2))

    print('''Quer continuar jogando? 
[1]- Sim
[2]- Não''')
    continuarJogo = input("Continuar jogo? ")

    if continuarJogo == "1":
        continuarJogo = True
    elif continuarJogo == "2":
        if score1 > score2:
            print("Jogador 1 ganhou a partida!")
        elif score1 < score2:
            print("Jogador 2 ganhou a partida!")
        else:
            print("O Terminou empatado!")
            print("Jogador 1: " + str(score1))
            print("Jogador 2: " + str(score2))
            print("Obrigado por jogar o meu jogo! feito por Vinícius Faria da Silva Carvalho")
            continuarJogo = False
