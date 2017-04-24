while True:
    funsao = input("você quer 'dormir' , 'hunt '  ou 'insperdex' : ")
    if funsao == "dormir":
        break
    
    elif funsao == "insperdex":
        print("o seu Inspermon : {0} , Vida: {1} , Poder Minimo :{2}, Poder maximo {3} , Defesa {4} ".format(inspermon_jogador["nome"],inspermon_jogador["vida"],inspermon_jogador["poder minimo"],inspermon_jogador["poder maximo"],inspermon_jogador["defesa"]))
        
        print("INSPERDÉX")
        for ipmon in insperdex :
            print ("Inspermon : {0} , Vida: {1} , Poder Minimo :{2}, Poder maximo {3} , Defesa {4}".format(ipmon["nome"],ipmon["vida"],ipmon["poder minimo"],ipmon["poder maximo"],ipmon["defesa"]))

    elif funsao == "hunt":
        inspermon_adversario = random.choice(inspermons)
        if inspermon_adversario not in insperdex:
            insperdex.append(inspermon_adversario)
        print ("Inspermon : {0} , Vida: {1} , Poder Minimo :{2}, Poder maximo {3} , Defesa {4}".format(inspermon_adversario["nome"],inspermon_adversario["vida"],inspermon_adversario["poder minimo"],inspermon_adversario["poder maximo"],inspermon_adversario["defesa"]))
        resultado_batalha = batalha(inspermon_jogador,inspermon_adversario)
        if resultado_batalha == "fim":
            print("jogo acabou , o seu inspermon era muito fraco e acabou morrendo ")
            break
        elif resultado_batalha == "xp":
            print("Voce derrotou o inspermon selvagem e ganhou xp")
    else:
        print ("digite algum comando valido ")