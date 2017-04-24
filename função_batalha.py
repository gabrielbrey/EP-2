def batalha(jogador, adversario):
    vida_jogador = jogador["vida"]
    vida_adversario = adversario["vida"]
    dano_jogador = poder_jogador(jogador) - adversario["defesa"]
    if dano_jogador < 0:
        dano_jogador=0
    dano_adversario = poder_adversario(adversario) - jogador["defesa"]
    if dano_adversario < 0:
        dano_adversario = 0
    while vida_jogador > 0 and vida_adversario > 0:
        atacar_fugir = input("Para atacar o inspermon selvagem aperte 'Enter' , ou para tentar fugir dessa batalha digite 'fugir' :  ")
        if atacar_fugir == "fugir" :
            fuga = random.choice(lista_fuga)
            if fuga > 2:
                print("Você conseguiu escapar desse inspermon selvagem!")
                break
            else:
                print("Ixi , hoje não é o seu dia de sorte :( ")
        else :
            if dano_critico(x) == True:
                vida_adversario = vida_adversario - dano_jogador * 1.5
                if vida_adversario < 1:
                    vida_adversario = 0
                print("Ataque critico de {0} no {1} ".format(dano_jogador * 1.5,adversario["nome"]))
                print("A vida do {0} é {1}".format(adversario["nome"],vida_adversario))
            else:
                vida_adversario = vida_adversario - dano_jogador
                print("{0} sofreu {1} de dano ".format(adversario["nome"],dano_jogador))
                if vida_adversario < 1:
                    vida_adversario = 0
                print("A vida do {0} é {1}".format(adversario["nome"],vida_adversario))
            if vida_adversario <= 0:
                print("voce ganhou o jogo e recebeu xp")
                return "xp"
            if dano_critic(v) == True:
                vida_jogador = vida_jogador - dano_adversario * 1.5
                if vida_jogador <1:
                    vida_jogador = 0   
                print("Ataque critico de {0} no {1} ".format(dano_adversario*1.5,jogador["nome"]))
                print("A vida do {0} é {1}".format(jogador["nome"],vida_jogador))
            else:
                vida_jogador = vida_jogador - dano_adversario
                print("{0} sofreu {1} de dano ".format(jogador["nome"],dano_adversario))
                if vida_jogador <1:
                    vida_jogador = 0    
                print("A vida do {0} é {1}".format(jogador["nome"],vida_jogador))
            if vida_jogador <= 0 :
                print("ixi , o seu inspermon é muito fraco e precisa de treino")
                return "fim" 