        inspermon_adversario = random.choice(inspermons)
        if inspermon_adversario not in insperdex:
            insperdex.append(inspermon_adversario)
        print ("Inspermon : {0} , Vida: {1} , Poder Minimo :{2}, Poder maximo {3} , Defesa {4}".format(inspermon_adversario["nome"],inspermon_adversario["vida"],inspermon_adversario["poder minimo"],inspermon_adversario["poder maximo"],inspermon_adversario["defesa"]))
        resultado_batalha = batalha(inspermon_jogador,inspermon_adversario)